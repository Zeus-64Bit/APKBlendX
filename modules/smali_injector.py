import os
import shutil

def inject_smali(smali_path, target_src):
    """
    Inject custom smali code from `smali_path` into `target_src/smali/`
    """
    target_smali_dir = os.path.join(target_src, "smali")

    if not os.path.exists(smali_path):
        print(f"[!] Smali injection path not found: {smali_path}")
        return

    for root, dirs, files in os.walk(smali_path):
        for file in files:
            if file.endswith(".smali"):
                rel_dir = os.path.relpath(root, smali_path)
                dst_dir = os.path.join(target_smali_dir, rel_dir)
                os.makedirs(dst_dir, exist_ok=True)
                shutil.copy2(os.path.join(root, file), os.path.join(dst_dir, file))

    print(f"[✓] Injected smali from {smali_path} into {target_smali_dir}")
