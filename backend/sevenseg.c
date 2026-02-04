#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

#define HT16K33_ADDR 0x70

void write_display(int fd, uint8_t *buffer) {
    uint8_t data[17];
    data[0] = 0x00; // start at RAM address 0

    for (int i = 0; i < 16; i++)
        data[i + 1] = buffer[i];

    write(fd, data, 17);
}

void clear_display(int fd) {
    uint8_t blank[16] = {0};
    write_display(fd, blank);
}

int main() {
    int fd = open("/dev/i2c-1", O_RDWR);
    if (fd < 0) {
        perror("Failed to open I2C bus");
        return 1;
    }

    if (ioctl(fd, I2C_SLAVE, HT16K33_ADDR) < 0) {
        perror("Failed to set I2C address");
        return 1;
    }

    // --- Initialize HT16K33 ---
    uint8_t cmd;

    cmd = 0x21;  // Turn on oscillator
    write(fd, &cmd, 1);

    cmd = 0x81;  // Display on, no blink
    write(fd, &cmd, 1);

    cmd = 0xEF;  // Brightness = 15
    write(fd, &cmd, 1);

    uint8_t display[16] = {0};

    printf("=== HT16K33 TEST START ===\n");

    // -------------------------------
    // Test 1: Light each digit
    // -------------------------------
    printf("Test 1: Lighting each digit...\n");

    for (int digit = 0; digit < 4; digit++) {
        clear_display(fd);

        int addr = digit * 2;   // 0,2,4,6
        display[addr] = 0x7F;   // all segments ON

        printf("Digit %d ON\n", digit);
        write_display(fd, display);

        sleep(1);
    }

    // -------------------------------
    // Test 2: All digits ON
    // -------------------------------
    printf("Test 2: All digits ON...\n");

    clear_display(fd);
    display[0] = 0x7F;
    display[2] = 0x7F;
    display[4] = 0x7F;
    display[6] = 0x7F;
    write_display(fd, display);
    sleep(2);

    // -------------------------------
    // Test 3: Brightness sweep
    // -------------------------------
    printf("Test 3: Brightness sweep...\n");

    for (int b = 0; b < 16; b++) {
        cmd = 0xE0 | b;
        write(fd, &cmd, 1);
        sleep(200000);
    }

    // -------------------------------
    // Test 4: Display OFF / ON
    // -------------------------------
    printf("Test 4: Display OFF...\n");
    cmd = 0x80;  // display off
    write(fd, &cmd, 1);
    sleep(1);

    printf("Display ON...\n");
    cmd = 0x81;  // display on
    write(fd, &cmd, 1);
    sleep(1);

    // -------------------------------
    // End
    // -------------------------------
    printf("=== TEST COMPLETE ===\n");

    clear_display(fd);
    close(fd);
    return 0;
}
