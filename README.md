# SD Card Formatter (Linux GTK3 GUI)
![](https://raw.githubusercontent.com/Stradios/SD-Card-Formatter-Linux-GTK3-GUI-/refs/heads/main/sdcard-formatter-installer/icons/sdcard-formatter.png)
This project provides a GTK3 front-end for [Tuxera's official SD Card Formatter](https://www.sdcard.org/downloads/sd-memory-card-formatter-for-linux/).  
> ⚠️ Due to licensing, you **must manually download** the binary `format_sd`.

---

## 🔧 Installation

1. **Download the official formatter**:  
   [Download `SDCardFormatterv1.0.3_Linux_x86_64.tgz`][https://www.sdcard.org/downloads/formatter/eula_linux/SDCardFormatterv1.0.3_Linux_x86_64.tgz](https://www.sdcard.org/downloads/sd-memory-card-formatter-for-linux/)

2. **Extract and copy the binary**:
```bash
tar -xzf ~/Downloads/SDCardFormatterv1.0.3_Linux_x86_64.tgz
sudo cp SDCardFormatterv1.0.3_Linux_x86_64/format_sd /usr/local/bin
sudo chmod +x /usr/local/bin/format_sd
git clone https://github.com/yourname/sdcard-formatter-gui
cd sdcard-formatter-gui
chmod +x install.sh
./install.sh

