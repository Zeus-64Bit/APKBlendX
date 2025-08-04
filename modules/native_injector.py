import os
import shutil

SUPPORTED_ABIS = ['armeabi-v7a', 'arm64-v8a', 'x86']

def inject_native_lib(lib_path, target_apk_dir):
    """
    Inject native libraries (.so) into the smali APK build directory
    """
    for abi in SUPPORTED_ABIS:
        source = os.path.join(lib_path, abi, 'libanti_emulator.so')
        if os.path.exists(source):
            dest_dir = os.path.join(target_apk_dir, 'lib', abi)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy(source, dest_dir)
            print(f"[+] Injected lib for {abi}: {source} → {dest_dir}")
        else:
            print(f"[!] Skipped {abi}: {source} not found")
