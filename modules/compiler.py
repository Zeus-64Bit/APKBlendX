import os
import subprocess

def compile_apk(source_dir, output_apk_path):
    """
    Recompiles the modified APK from the decompiled source using apktool.

    :param source_dir: Path to the decompiled and modified APK source (usually workspace/merged)
    :param output_apk_path: Path where the recompiled APK will be saved
    :return: Path to the compiled APK
    """
    print("[*] Recompiling APK using apktool...")

    try:
        subprocess.run([
            "apktool", "b", source_dir, "-o", output_apk_path
        ], check=True)
        print(f"[✓] APK successfully recompiled to: {output_apk_path}")
        return output_apk_path

    except subprocess.CalledProcessError as e:
        print(f"[✗] Failed to recompile APK: {e}")
        raise
