import os
import re

def rebrand_package(source_path, new_package):
    """
    Replace all occurrences of the old package name with a new one in smali and manifest files.
    """
    old_package = None
    manifest_path = os.path.join(source_path, "AndroidManifest.xml")

    # Get old package from manifest
    with open(manifest_path, "r") as f:
        content = f.read()
        match = re.search(r'package="([^"]+)"', content)
        if match:
            old_package = match.group(1)
        else:
            raise ValueError("Could not find old package name in manifest.")

    # Update manifest
    updated_manifest = content.replace(old_package, new_package)
    with open(manifest_path, "w") as f:
        f.write(updated_manifest)

    # Update smali files
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(".smali"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    smali_content = f.read()
                updated_content = smali_content.replace(old_package.replace(".", "/"), new_package.replace(".", "/"))
                with open(file_path, "w") as f:
                    f.write(updated_content)

    print(f"[✓] Rebranded package from {old_package} to {new_package}")
