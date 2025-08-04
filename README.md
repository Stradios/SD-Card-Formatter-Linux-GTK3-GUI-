# SD Card Formatter (Linux GTK3 GUI)

<p align="center">
  <img src="https://raw.githubusercontent.com/Stradios/SD-Card-Formatter-Linux-GTK3-GUI-/refs/heads/main/Screenshot%20From%202025-08-04%2022-37-59.png" alt="Screenshot">
</p>

---

This project provides a GTK3 front-end for [Tuxera's official SD Card Formatter](https://www.sdcard.org/downloads/sd-memory-card-formatter-for-linux/).  
> ⚠️ Due to licensing restrictions, you **must manually download** the binary `format_sd`.

---

## 🔧 Installation

### 1. Download the official formatter

Download `SDCardFormatterv1.0.3_Linux_x86_64.tgz` from the official site:  
👉 [SD Memory Card Formatter for Linux (Official)](https://www.sdcard.org/downloads/sd-memory-card-formatter-for-linux/)

### 2. Extract and copy the binary

```bash
tar -xzf ~/Downloads/SDCardFormatterv1.0.3_Linux_x86_64.tgz
sudo cp SDCardFormatterv1.0.3_Linux_x86_64/format_sd /usr/local/bin/
sudo chmod +x /usr/local/bin/format_sd
```

### 3. Install the GUI

```bash
git clone https://github.com/Stradios/SD-Card-Formatter-Linux-GTK3-GUI-.git
cd SD-Card-Formatter-Linux-GTK3-GUI-/sdcard-formatter-installer
chmod +x install.sh
./install.sh
```

---


## 🖼 Features

- Simple GTK3 interface
- Lists only removable drives
- Choose Quick, Discard, or Overwrite format types
- Confirmation before formatting
- Shows output messages
- Detects and unmounts drives before formatting
- Desktop icon with taskbar support

---

## 📝 License

This GUI is open-source (MIT license).  
The **`format_sd` binary is proprietary** and must be downloaded from the official SD Association website.

---

## 🧊 Author

Developed by [Stradios](https://github.com/Stradios)
