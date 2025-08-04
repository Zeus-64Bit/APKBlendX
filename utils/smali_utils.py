import os

def find_main_activity(smali_dir):
    for root, _, files in os.walk(smali_dir):
        for file in files:
            if file == "MainActivity.smali":
                return os.path.join(root, file)
    return None

def smali_path_to_class(smali_path):
    relative = smali_path.split("smali/")[-1]
    return relative.replace(".smali", "").replace("/", ".")

def class_to_smali_path(cls, smali_root="smali"):
    return os.path.join(smali_root, cls.replace(".", "/") + ".smali")
