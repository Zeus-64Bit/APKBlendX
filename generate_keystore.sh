#!/bin/bash

echo "🔐 APKBlendX Keystore Generator"
echo "-------------------------------"

# Prompt for keystore name
read -p "Enter keystore file name (default: user.keystore): " KEY_NAME
KEY_NAME=${KEY_NAME:-user.keystore}

# Prompt for alias
read -p "Enter alias name (default: apkblendx): " ALIAS
ALIAS=${ALIAS:-apkblendx}

# Prompt for password
read -sp "Enter password for keystore & key (default: password): " PASSWORD
echo
PASSWORD=${PASSWORD:-password}

# Prompt for validity (days)
read -p "Enter validity in days (default: 10000): " VALIDITY
VALIDITY=${VALIDITY:-10000}

# Prompt for Distinguished Name (DN)
read -p "Enter DN (CN, OU, O, L, S, C) (default: CN=APKBlendX, OU=Dev, O=CyberSec, L=Delhi, S=Delhi, C=IN): " DNAME
DNAME=${DNAME:-CN=APKBlendX, OU=Dev, O=CyberSec, L=Delhi, S=Delhi, C=IN}

# Ensure keys directory exists
mkdir -p keys

# Generate keystore
keytool -genkey -v \
  -keystore "keys/$KEY_NAME" \
  -alias "$ALIAS" \
  -keyalg RSA \
  -keysize 2048 \
  -validity "$VALIDITY" \
  -storepass "$PASSWORD" \
  -keypass "$PASSWORD" \
  -dname "$DNAME"

# Success message
if [ $? -eq 0 ]; then
  echo "✅ Keystore generated: keys/$KEY_NAME"
  echo "   Alias: $ALIAS"
  echo "   Password: $PASSWORD"
else
  echo "❌ Failed to generate keystore."
fi
