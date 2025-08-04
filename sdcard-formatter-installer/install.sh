#!/bin/bash
set -e

INSTALL_DIR="/usr/local/bin"
FORMAT_SD="$INSTALL_DIR/format_sd"

echo "📥 This script will install the SD Card Formatter GUI only."
echo "⚠️  Due to licensing, 'format_sd' must be downloaded manually."
echo

# Check if format_sd exists
if [[ ! -f "$FORMAT_SD" ]]; then
  echo "❌ 'format_sd' not found in $INSTALL_DIR"
  echo "🔗 Please download it from the official website:"
  echo "   https://www.sdcard.org/downloads/formatter/eula_linux/SDCardFormatterv1.0.3_Linux_x86_64.tgz"
  echo
  echo "After downloading, run the following commands:"
  echo "   tar -xzf SDCardFormatterv1.0.3_Linux_x86_64.tgz"
  echo "   sudo cp SDCardFormatterv1.0.3_Linux_x86_64/format_sd $INSTALL_DIR"
  echo "   sudo chmod +x $INSTALL_DIR/format_sd"
  echo
  echo "Then re-run this installer:"
  echo "   ./install.sh"
  exit 1
fi

# Install GUI script
sudo install -Dm755 bin/sd_formatter_gui.py "$INSTALL_DIR/sd_formatter_gui.py"

# Install icon
mkdir -p ~/.local/share/icons
cp icons/sdcard-formatter.png ~/.local/share/icons/sdcard-formatter.png

# Install desktop shortcut
mkdir -p ~/.local/share/applications
cp sdcard-formatter.desktop ~/.local/share/applications/sdcard-formatter.desktop

# Update desktop DB (optional)
update-desktop-database ~/.local/share/applications || true

echo
echo "✅ SD Card Formatter GUI installed!"
echo "📌 Launch it from your application menu."

