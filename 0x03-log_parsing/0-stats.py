import re


def extract_input(line):
    log_fmt = r'\s*(?P<ip>\S+)\s\
    *\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]\s*\
    "(?P<request>[^"]*)"\s*(?P<status_code>\S+)\s*(?P<file_size>\d+)'
    info = {'status_code': 0, 'file_size': 0}
    match = re.fullmatch(log_fmt, line)
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info


def print_statistics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


def run():
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0}
    line_count = 0
    try:
        while True:
            line = input()
            line_info = extract_input(line)
            status_code = line_info.get('status_code', '0')
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
                total_size += line_info['file_size']
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_codes)


if __name__ == '__main__':
    run()
