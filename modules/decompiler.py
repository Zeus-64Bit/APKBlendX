import os
import subprocess
import shutil

def decompile_apk(apk_path, output_dir):
    """Decompile an APK using apktool."""
    if os.path.exists(output_dir):
        print(f"[!] Removing existing directory: {output_dir}")
        shutil.rmtree(output_dir)

    print(f"[+] Decompiling {apk_path}...")
    try:
        subprocess.run(["apktool", "d", "-f", apk_path, "-o", output_dir], check=True)
        print(f"[✓] Decompiled to: {output_dir}")
        return True
    except subprocess.CalledProcessError:
        print(f"[✗] Failed to decompile {apk_path}")
        return False
