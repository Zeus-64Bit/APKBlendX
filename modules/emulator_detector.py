import os

def create_emudetect_smali(output_dir, package_name):
    """
    Create Smali stub for EmuDetect.java
    """
    class_path = os.path.join(output_dir, *package_name.split("."), "EmuDetect.smali")
    os.makedirs(os.path.dirname(class_path), exist_ok=True)

    smali_code = f""".class public L{package_name.replace('.', '/')}/EmuDetect;
.super Ljava/lang/Object;

.method public static native isEmulator()Z
.end method

.static constructor <clinit>()V
    .locals 1
    const-string v0, "anti_emulator"
    invoke-static {{v0}}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V
    return-void
.end method
"""
    with open(class_path, "w") as f:
        f.write(smali_code)
    print(f"[+] Injected EmuDetect.smali at: {class_path}")


def inject_emulator_check_to_main(main_activity_path, pkg_name="com/example"):
    """
    Modify onCreate method to include emulator check
    """
    if not os.path.exists(main_activity_path):
        print(f"[!] MainActivity.smali not found: {main_activity_path}")
        return

    with open(main_activity_path, "r") as file:
        lines = file.readlines()

    modified_lines = []
    inserted = False
    for line in lines:
        modified_lines.append(line)
        if ".method public onCreate" in line and not inserted:
            modified_lines.append(
                f"    invoke-static {{}}, L{pkg_name.replace('.', '/')}/EmuDetect;->isEmulator()Z\n"
                "    move-result v0\n"
                "    if-eqz v0, :continue\n"
                "    invoke-virtual {p0}, L" + pkg_name.replace('.', '/') + "/MainActivity;->finish()V\n"
                "    return-void\n"
                "    :continue\n"
            )
            inserted = True

    with open(main_activity_path, "w") as file:
        file.writelines(modified_lines)

    print(f"[+] Emulator detection added to: {main_activity_path}")
