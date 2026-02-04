#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <termios.h>
#include <stdlib.h>

#define SERIAL_PORT "/dev/serial0"
#define BAUDRATE B9600
#define BUF_SIZE 256

// Check if GPGGA sentence has a fix (fix quality > 0)
int gpgga_has_fix(char *line) {
    if (strncmp(line, "$GPGGA", 6) != 0)
        return 0;

    char *line_copy = strdup(line);
    if (!line_copy) return 0;

    char *token = strtok(line_copy, ",");
    int field = 0;
    int fix = 0;
    while (token != NULL) {
        field++;
        if (field == 7) { // 7th field = fix quality
            fix = atoi(token);
            break;
        }
        token = strtok(NULL, ",");
    }
    free(line_copy);
    return fix > 0;
}

// Extract latitude and longitude from GPGGA
void gpgga_get_latlon(char *line, char *lat, char *ns, char *lon, char *ew) {
    char *line_copy = strdup(line);
    if (!line_copy) return;

    char *token = strtok(line_copy, ",");
    int field = 0;
    while (token != NULL) {
        field++;
        if (field == 3) strcpy(lat, token);
        if (field == 4) strcpy(ns, token);
        if (field == 5) strcpy(lon, token);
        if (field == 6) strcpy(ew, token);
        token = strtok(NULL, ",");
    }
    free(line_copy);
}

int main() {
    int fd = open(SERIAL_PORT, O_RDONLY | O_NOCTTY);
    if (fd < 0) {
        perror("open");
        return 1;
    }

    struct termios options;
    tcgetattr(fd, &options);

    // Set baud rate
    cfsetispeed(&options, BAUDRATE);
    cfsetospeed(&options, BAUDRATE);

    options.c_cflag |= (CLOCAL | CREAD);
    options.c_cflag &= ~CSIZE;
    options.c_cflag |= CS8;
    options.c_cflag &= ~PARENB;
    options.c_cflag &= ~CSTOPB;
    // remove CRTSCTS line
    options.c_lflag &= ~(ICANON | ECHO | ECHOE | ISIG);
    options.c_iflag &= ~(IXON | IXOFF | IXANY);
    options.c_oflag &= ~OPOST;

    tcsetattr(fd, TCSANOW, &options);

    char buf[BUF_SIZE];
    char lat[16] = "", ns[2] = "", lon[16] = "", ew[2] = "";
    int got_fix = 0;

    printf("Waiting for GPS fix (cold start)...\n");

    while (!got_fix) {
        int n = read(fd, buf, BUF_SIZE - 1);
        if (n > 0) {
            buf[n] = '\0';
            char *line = strtok(buf, "\n");
            while (line != NULL) {
                if (gpgga_has_fix(line)) {
                    got_fix = 1;
                    gpgga_get_latlon(line, lat, ns, lon, ew);
                    printf("\n✅ GPS Fix acquired!\nLatitude: %s %s\nLongitude: %s %s\n", lat, ns, lon, ew);
                    break;
                }
                line = strtok(NULL, "\n");
            }
        }
        if (!got_fix)
            printf("⏳ Waiting for fix...\r");
        sleep(100000); // 0.1s
    }

    // Continue printing coordinates
    while (1) {
        int n = read(fd, buf, BUF_SIZE - 1);
        if (n > 0) {
            buf[n] = '\0';
            char *line = strtok(buf, "\n");
            while (line != NULL) {
                if (gpgga_has_fix(line)) {
                    gpgga_get_latlon(line, lat, ns, lon, ew);
                    printf("Latitude: %s %s | Longitude: %s %s\n", lat, ns, lon, ew);
                }
                line = strtok(NULL, "\n");
            }
        }
        sleep(100000);
    }

    close(fd);
    return 0;
}
