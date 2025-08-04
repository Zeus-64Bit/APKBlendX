import random

# Hardcoded list of legit-looking package names
SAFE_PACKAGES = [
    "com.google.services",
    "com.android.update",
    "com.adobe.viewer",
    "com.microsoft.sync",
    "com.dropbox.mobile",
    "com.whatsapp.clone",
    "com.system.configurator",
    "com.media.backup",
    "com.android.callservice",
    "com.instagram.updater"
]

def get_random_package_name():
    return random.choice(SAFE_PACKAGES)

def is_suspicious(name):
    blacklisted_keywords = ["metasploit", "payload", "rat", "virus", "hack"]
    return any(bad in name.lower() for bad in blacklisted_keywords)
