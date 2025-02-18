# KMK Keyboard Firmware for Amstrad 464 Plus

This repository contains the KMK firmware for a custom Amstrad 464 Plus keyboard, running on CircuitPython and built using the [KMK framework](https://github.com/KMKfw/kmk_firmware).

## Features

- Dual-layer keymap: default and alternate layers.
- Custom macros for non-standard keys.
- Customised row and column pinout.
- Column-to-row diode orientation.

## Requirements

- A microcontroller running CircuitPython.
- KMK framework and dependencies.
- Hardware wiring as per the defined pinout.
- Keyboard region settings should be United Kingdom.

## Usage

1. Clone this repository.
2. Install CircuitPython and ensure KMK dependencies are available on your device.
3. Modify the GPIO pins to match wiring of your microcontroller.
4. Flash the firmware onto your microcontroller.
5. Use your Amstrad 464 Plus as a USB keyboard.

## Custom Layers

- **Default layer**: Standard keymap.
- **Alternate layer**: Activated via the `SHIFT` key.

## Licence

This project is licensed under the MIT Licence.
