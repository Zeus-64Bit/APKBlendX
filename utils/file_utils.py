import os
import shutil
import random
import string

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def clear_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def copytree(src, dst):
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source path not found: {src}")
    shutil.copytree(src, dst)

def copyfile(src, dst):
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source file not found: {src}")
    shutil.copy2(src, dst)

def remove(path):
    if os.path.isfile(path):
        os.remove(path)

def exists(path):
    return os.path.exists(path)

def list_files(path, ext=None):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and (f.endswith(ext) if ext else True)]

def clean_workspace():
    if os.path.exists("workspace"):
        shutil.rmtree("workspace")
    os.makedirs("workspace", exist_ok=True)

    if os.path.exists("build"):
        shutil.rmtree("build")
    os.makedirs("build", exist_ok=True)


def generate_random_package():
    prefix = "com"
    middle = ''.join(random.choices(string.ascii_lowercase, k=6))
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"{prefix}.{middle}.{suffix}"
