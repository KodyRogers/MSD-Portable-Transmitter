#include "header.h"

#define LED_PIN     0   // WiringPi 0 -> GPIO17 (output)
#define SWITCH_PIN  2   // WiringPi 2 -> GPIO27 (input, also for mode switch)

// Auto blink LED continuously
void LED_test(void) {
    while (1) {
        digitalWrite(LED_PIN, HIGH);
        delay(500);
        digitalWrite(LED_PIN, LOW);
        delay(500);
    }
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("WiringPi initialization failed!\n");
        return 1;
    }

    pinMode(LED_PIN, OUTPUT);
    pinMode(SWITCH_PIN, OUTPUT);
    pullUpDnControl(SWITCH_PIN, PUD_UP);

    printf("Choose mode:\n");
    printf("1. 't' for LED_test (auto blink)\n");
    printf("2. 's' for switch_control (manual toggle)\n");
    printf("Press key then Enter: ");
    
    char mode;
    scanf(" %c", &mode);  // Space skips whitespace
    
    if (mode == 't' || mode == 'T') {
        printf("LED_test mode - blinking forever. Ctrl+C to exit.\n");
        LED_test();
    } else if (mode == 's' || mode == 'S') {
        printf("Switch mode - press switch on GPIO27 to toggle LED. Ctrl+C to exit.\n");
        while (1) {
            //switch_control();
            delay(50);
        }
    } else {
        printf("Invalid choice. Defaulting to switch mode.\n");
        exit(99);
    }

    return 0;
}
