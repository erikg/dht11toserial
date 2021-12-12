#!/usr/bin/env python3

import json
from serial import Serial
import config

def main():
    port = Serial(config.serial, config.baud)
    line = port.read_until()
    port.close()
    print(line)

if __name__ == "__main__":
    main()
