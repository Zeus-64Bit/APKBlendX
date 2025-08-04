import subprocess

def sign_apk(apk_path, output_apk, keystore_path, alias, keystore_pass):
    """
    Sign an APK using apksigner.
    """
    cmd = [
        "apksigner", "sign",
        "--ks", keystore_path,
        "--ks-key-alias", alias,
        "--ks-pass", f"pass:{keystore_pass}",
        "--out", output_apk,
        apk_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("[!] APK signing failed:")
        print(result.stderr)
        raise RuntimeError("APK signing failed.")
    
    print("[✓] APK signed successfully.")
