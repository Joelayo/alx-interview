#!/usr/bin/python3
import sys
import signal
import random
from time import sleep
import datetime

# Function to handle keyboard interrupt
def signal_handler(sig, frame):
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler) # Register signal handler

# Initialize variables
total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

for i in range(10000):
    sleep(random.random())
    line = "{}.{}.{}.{} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )
    sys.stdout.write(line)
    sys.stdout.flush()
    line_count += 1

    # Split line by space
    parts = line.split(" ")

    # Check if line is in correct format
    if len(parts) != 9:
        continue

    # Get status code and file size
    status_code = parts[8]
    file_size = parts[9]

    # Check if status code is valid
    if status_code.isnumeric() and int(status_code) in status_codes:
        status_codes[status_code] += 1
    else:
        continue

    # Check if file size is valid
    if file_size.isnumeric():
        total_size += int(file_size)
    else:
        continue

    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print("File size: {}".format(total_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key] > 0:
                print("{}: {}".format(key, status_codes[key]))
