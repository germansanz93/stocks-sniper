import json
import os.path

base_path = os.getcwd()


def get_full_path(dir_name):
    return f'{base_path}/data/{dir_name}'


def assert_directory_existence(dir_name):
    return os.path.exists(get_full_path(dir_name))


def create_directory(dir_name):
    full_path = get_full_path(dir_name)
    os.makedirs(full_path)
    print("Directory", full_path, "created successfully!")
    return get_full_path(dir_name)


def read_valuation_from_file(filename):
    with open(filename) as f:
        return json.load(f)


def save_in_file(filename, to_save):
    with open(filename, 'w') as f:
        json.dump(to_save, f, indent=4)
