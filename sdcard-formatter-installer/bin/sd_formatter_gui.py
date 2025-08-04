#!/usr/bin/env python3

import gi
import subprocess
import os
import re

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SDFormatter(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="SD Card Formatter")
        self.set_border_width(10)
        self.set_default_size(420, 270)

        # Optional: set window icon
        icon_path = os.path.expanduser("~/.local/share/icons/sdcard-formatter.png")
        if os.path.exists(icon_path):
            self.set_icon_from_file(icon_path)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # Device dropdown and refresh button
        grid.attach(Gtk.Label(label="Select Device:"), 0, 0, 1, 1)
        self.device_dropdown = Gtk.ComboBoxText()
        grid.attach(self.device_dropdown, 1, 0, 1, 1)

        self.refresh_button = Gtk.Button(label="🔄 Refresh")
        self.refresh_button.connect("clicked", self.on_refresh_clicked)
        grid.attach(self.refresh_button, 2, 0, 1, 1)

        # Volume Label
        grid.attach(Gtk.Label(label="Volume Label:"), 0, 1, 1, 1)
        self.label_entry = Gtk.Entry()
        self.label_entry.set_max_length(11)
        grid.attach(self.label_entry, 1, 1, 2, 1)

        # Format type
        grid.attach(Gtk.Label(label="Format Type:"), 0, 2, 1, 1)
        self.format_type = Gtk.ComboBoxText()
        self.format_type.append_text("Quick (Default)")
        self.format_type.append_text("Discard")
        self.format_type.append_text("Overwrite")
        self.format_type.set_active(0)
        grid.attach(self.format_type, 1, 2, 2, 1)

        # Format Button
        self.format_button = Gtk.Button(label="Format")
        self.format_button.connect("clicked", self.on_format_clicked)
        grid.attach(self.format_button, 1, 3, 1, 1)

        # Output label
        self.output_label = Gtk.Label(label="")
        self.output_label.set_line_wrap(True)
        grid.attach(self.output_label, 0, 4, 3, 1)

        # Populate devices initially
        self.populate_devices()

    def populate_devices(self):
        self.device_dropdown.remove_all()
        try:
            output = subprocess.check_output(
                ["lsblk", "-P", "-o", "NAME,SIZE,TYPE,RM,TRAN,MODEL"],
                text=True
            )
            print("DEBUG: lsblk -P output:\n", output)

            for line in output.strip().split('\n'):
                info = dict(re.findall(r'(\w+)="([^"]*)"', line))
                print("DEBUG LINE PARSED:", info)

                if info.get("TYPE") == "disk" and info.get("RM") == "1":
                    name = info["NAME"]
                    size = info["SIZE"]
                    model = info.get("MODEL", "") or "Removable"
                    device_path = f"/dev/{name}"
                    label = f"{device_path} – {size} – {model}"
                    print("DEBUG ADDING:", label)
                    self.device_dropdown.append_text(label)

            if self.device_dropdown.get_active() == -1:
                self.device_dropdown.set_active(0)

        except Exception as e:
            self.output_label.set_text(f"Device detection error: {e}")
            print("DEBUG ERROR:", e)

    def on_refresh_clicked(self, widget):
        self.populate_devices()
        self.output_label.set_text("🔄 Device list refreshed.")

    def on_format_clicked(self, widget):
        selected_text = self.device_dropdown.get_active_text()
        label = self.label_entry.get_text().strip()
        mode = self.format_type.get_active_text()

        if not selected_text:
            self.output_label.set_text("❌ No device selected.")
            return

        # Extract /dev/sdX from dropdown label
        device = selected_text.split("–")[0].strip()
        if not os.path.exists(device):
            self.output_label.set_text("❌ Device path does not exist.")
            return

        # Determine script path regardless of launch directory
        script_dir = os.path.dirname(os.path.realpath(__file__))
        format_sd_path = os.path.join(script_dir, "format_sd")
        if not os.path.exists(format_sd_path):
            self.output_label.set_text("❌ Error:\nCannot find 'format_sd' in script directory.")
            return

        cmd = ["pkexec", format_sd_path, "-l", label or "Untitled"]
        if mode == "Discard":
            cmd.append("--discard")
        elif mode == "Overwrite":
            cmd.append("--overwrite")
        cmd.append(device)

        try:
            self.output_label.set_text("⚙️ Formatting in progress...")
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode == 0:
                stdout_lines = result.stdout.strip().splitlines()
                if stdout_lines:
                    last_line = stdout_lines[-1]
                    self.output_label.set_text("✅ Success:\n" + last_line)
                else:
                    self.output_label.set_text("✅ Success: Device formatted (no output).")
            else:
                self.output_label.set_text("❌ Error:\n" + result.stderr.strip())

        except Exception as e:
            self.output_label.set_text(f"⚠️ Exception: {e}")
            print("DEBUG ERROR:", e)


if __name__ == "__main__":
    win = SDFormatter()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

