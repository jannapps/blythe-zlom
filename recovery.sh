#!/bin/bash

# run this script if the HID keyboard has keys perpetually held down

echo -en \\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00 >> /dev/hidg0
