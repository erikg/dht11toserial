#!/usr/bin/env python3

import json
from serial import Serial
import requests

import config

def main():
    port = Serial(config.serial, config.baud)
    line = port.read_until()
    port.close()

    data = json.loads(line)
    temp = data["TEMP"]
    hum = data["HUM"]

    infline = f"""temp,room={config.room} value={temp}
hum,room={config.room} value={hum}"""
    headers = {"Authorization": f"Token {config.token}"}

    res = requests.post(config.url, infline, headers=headers)

if __name__ == "__main__":
    main()
