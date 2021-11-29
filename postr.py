#!/usr/bin/env python3

import json
from serial import Serial
import requests

url = "http://192.168.1.1:8086/write?db=home"
room = "kitchen"

def main():
    port = Serial("/dev/ttyUSB0", 9600)
    line = port.read_until()
    port.close()

    data = json.loads(line)
    temp = data["TEMP"]
    hum = data["HUM"]

    infline = f"""temp,room={room} value={temp}
hum,room={room} value={hum}"""

    requests.post(url, infline)

if __name__ == "__main__":
    main()
