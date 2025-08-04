import xml.etree.ElementTree as ET

def add_permission(manifest_path, permission_name):
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    # Check if permission already exists
    for perm in root.findall("uses-permission"):
        if perm.attrib.get('{http://schemas.android.com/apk/res/android}name') == permission_name:
            print(f"[=] Permission already present: {permission_name}")
            return

    ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
    perm = ET.Element("uses-permission")
    perm.set('{http://schemas.android.com/apk/res/android}name', permission_name)
    root.insert(0, perm)

    tree.write(manifest_path, encoding='utf-8', xml_declaration=True)
    print(f"[✓] Added permission: {permission_name}")

def add_service(manifest_path, service_name, exported="false", enabled="true"):
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    application = root.find('application')
    if application is None:
        print("[!] No <application> tag found.")
        return

    for service in application.findall("service"):
        if service.attrib.get('{http://schemas.android.com/apk/res/android}name') == service_name:
            print(f"[=] Service already present: {service_name}")
            return

    ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
    service = ET.Element("service")
    service.set('{http://schemas.android.com/apk/res/android}name', service_name)
    service.set('{http://schemas.android.com/apk/res/android}enabled', enabled)
    service.set('{http://schemas.android.com/apk/res/android}exported', exported)

    application.append(service)
    tree.write(manifest_path, encoding='utf-8', xml_declaration=True)
    print(f"[✓] Added service: {service_name}")
