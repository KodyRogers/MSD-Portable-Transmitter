#############################################################################
# Makefile for Raspberry Pi LED + 7-segment projects - NO 'all' target
#############################################################################

CSOURCE = test.c sevenseg.c gps.c
CBINS = $(patsubst %.c,%,$(CSOURCE))

CC = gcc
CFLAGS = -Wall -Wextra -O2 -g -std=c99
WIRING = -lwiringPi
I2C_LIBS = -li2c

.SILENT:

.PHONY: LED_test SEVEN_test clean help

# Build + run LED test (builds ONLY when needed)
LED_test: test
	@echo "Running LED test..."
	sudo ./test

# Build + run 7-segment test (builds ONLY when needed)  
SEVEN_test: sevenseg
	@echo "Running SevenSeg test..."
	sudo ./sevenseg

GPS_test: gps
	@echo "Running gps test..."
	sudo ./gps

# Individual build rules (with REAL TABS ↓)
test: test.c
	@echo "Building LED test..."
	$(CC) $(CFLAGS) $< -o $@ $(WIRING)

gps: gps.c
	@echo "Building GPS test..."
	$(CC) $(CFLAGS) $< -o $@ $(WIRING)

sevenseg: sevenseg.c
	@echo "Building 7-segment I2C..."
	$(CC) $(CFLAGS) $< -o $@ $(I2C_LIBS) $(WIRING)

# Clean
clean:
	@echo "Cleaning..."
	rm -f $(CBINS)

# Help (removed 'all' reference)
help:
	@echo "CSOURCE files: $(CSOURCE)"
	@echo "Targets:"
	@echo "  make LED_test   - build + run LED (sudo)"
	@echo "  make SEVEN_test - build + run 7-segment (sudo)"
	@echo "  make test       - build LED only"
	@echo "  make sevenseg   - build 7-segment only"
	@echo "  make clean      - remove executables"
