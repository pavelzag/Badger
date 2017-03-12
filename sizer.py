import os


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        value = convert_bytes(file_info.st_size)
        if 'MB' in value:
            return float(value.split(' ', 1)[0])
        elif 'KB' in value:
            return float(value.split(' ', 1)[0]) * 0.001
