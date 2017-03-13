import os


def remove_file(file_path):
    os.remove(file_path)


def is_file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False