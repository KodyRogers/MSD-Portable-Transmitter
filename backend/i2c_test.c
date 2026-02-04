#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

int main(void) {
    int fd;
    const char *device = "/dev/i2c-1";
    int addr = 0x70;   // HT16K33 default address

    fd = open(device, O_RDWR);
    if (fd < 0) {
        perror("Failed to open I2C bus");
        return 1;
    }

    if (ioctl(fd, I2C_SLAVE, addr) < 0) {
        perror("Failed to select I2C device");
        close(fd);
        return 1;
    }

    // Try a simple write (turn oscillator ON for HT16K33)
    unsigned char cmd = 0x21;
    if (write(fd, &cmd, 1) != 1) {
        perror("I2C write failed");
        close(fd);
        return 1;
    }

    printf("I2C write succeeded — device ACKed\n");

    close(fd);
    return 0;
}

