import tkinter as tk
from tkinter import ttk
import threading
import subprocess

class FirmwareDesigner(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kiwi.ki Firmware Designer")
        self.geometry("800x600")

        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.vars = {}

        # --- System Check Frame ---
        dependency_frame = ttk.LabelFrame(main_frame, text="1. System-Check", padding="10")
        dependency_frame.pack(fill=tk.X, pady=5)
        self.dependency_status_label = ttk.Label(dependency_frame, text="Prüfe Abhängigkeiten...", wraplength=750, justify=tk.LEFT)
        self.dependency_status_label.pack(fill=tk.X)
        self.dependencies_ok = self.check_dependencies()

        # --- Configuration Frame ---
        config_frame = ttk.LabelFrame(main_frame, text="2. Konfiguration", padding="10")
        config_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        notebook = ttk.Notebook(config_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)

        simple_tab = ttk.Frame(notebook)
        expert_tab = ttk.Frame(notebook)
        notebook.add(simple_tab, text="Einfache Ansicht")
        notebook.add(expert_tab, text="Experten-Ansicht")

        self.create_simple_widgets(simple_tab)
        self.create_expert_widgets(expert_tab)

        # --- Build Frame ---
        build_frame = ttk.LabelFrame(main_frame, text="3. Kompilieren", padding="10")
        build_frame.pack(fill=tk.X, pady=5)

        self.build_button = ttk.Button(build_frame, text="Firmware Kompilieren", command=self.start_build_thread)
        self.build_button.pack(pady=5)
        if not self.dependencies_ok:
            self.build_button.config(state=tk.DISABLED)

        # --- Output Log ---
        log_frame = ttk.LabelFrame(main_frame, text="Log-Ausgabe", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = tk.Text(log_frame, height=10, wrap=tk.WORD, bg="black", fg="white")
        self.log_text.pack(fill=tk.BOTH, expand=True)


    def _create_param_widget(self, parent, param_name, default_value, is_bool=False):
        """Helper to create a label and an entry/checkbutton for a parameter."""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=2, padx=5)

        label = ttk.Label(frame, text=f"{param_name}:", width=30)
        label.pack(side=tk.LEFT, padx=5)

        if is_bool:
            var = tk.BooleanVar(value=bool(int(default_value)))
            widget = ttk.Checkbutton(frame, variable=var)
        else:
            var = tk.StringVar(value=str(default_value))
            widget = ttk.Entry(frame, textvariable=var, width=20)

        widget.pack(side=tk.LEFT, padx=5)
        self.vars[param_name] = var
        return frame

    def create_simple_widgets(self, parent_tab):
        """Creates and places widgets for the simple configuration view."""
        frame = ttk.Frame(parent_tab)
        frame.pack(fill=tk.X, pady=10)
        self._create_param_widget(frame, "KIWI_CHANNEL", 81)
        self._create_param_widget(frame, "SEND_DOUBLE_TAP_CHALLENGES", 1, is_bool=True)
        self._create_param_widget(frame, "SEND_NORMAL_CHALLENGES", 0, is_bool=True)
        self._create_param_widget(frame, "POLL_INTERVAL_STANDARD", 950)
        self._create_param_widget(frame, "MOTIONLESS_TIME", 5000)
        self._create_param_widget(frame, "DOUBLE_TAP_TIME", 5000)

    def create_expert_widgets(self, parent_tab):
        """Creates and places widgets for the expert configuration view."""

        # --- Listen Timings Group ---
        listen_group = ttk.LabelFrame(parent_tab, text="Listen Timings (µs)", padding="10")
        listen_group.pack(fill=tk.X, pady=5, padx=5)
        self._create_param_widget(listen_group, "LISTEN_TIME_BEACON", 1500)
        self._create_param_widget(listen_group, "LISTEN_TIME_RANDOM", 10000)
        self._create_param_widget(listen_group, "LISTEN_TIME_MANUFACTURING", 1000)

        # --- Packet Send Logic Group ---
        packet_group = ttk.LabelFrame(parent_tab, text="Packet Send Logic", padding="10")
        packet_group.pack(fill=tk.X, pady=5, padx=5)
        self._create_param_widget(packet_group, "WAIT_BEFORE_RANDOM", 50)
        self._create_param_widget(packet_group, "SEND_COUNT_RANDOM", 1)
        self._create_param_widget(packet_group, "SEND_COUNT_CHALLENGE", 1)
        self._create_param_widget(packet_group, "SEND_SPACING_CHALLENGE", 50)
        self._create_param_widget(packet_group, "PACKET_STAT_THRESH", 4)
        self._create_param_widget(packet_group, "PACKET_STAT_MAX", 5)

        # --- Door Proximity Timings Group ---
        door_prox_group = ttk.LabelFrame(parent_tab, text="Door Proximity Timings (ms)", padding="10")
        door_prox_group.pack(fill=tk.X, pady=5, padx=5)
        self._create_param_widget(door_prox_group, "MAYBE_IFOD_THRESHOLD", 1500)
        self._create_param_widget(door_prox_group, "LONGTIME_IFOD_THRESHOLD", 13000)
        self._create_param_widget(door_prox_group, "DOOR_SEEN_SW_MAX", 20000)
        self._create_param_widget(door_prox_group, "POLL_INTERVAL_SHORT", 650)
        self._create_param_widget(door_prox_group, "POLL_INTERVAL_SHORTEST", 150)
        self._create_param_widget(door_prox_group, "POLL_INTERVAL_LONG", 1950)

        # --- Accelerometer Thresholds Group ---
        accel_group = ttk.LabelFrame(parent_tab, text="Accelerometer Thresholds", padding="10")
        accel_group.pack(fill=tk.X, pady=5, padx=5)
        self._create_param_widget(accel_group, "ACC_THRESHOLD_LOWPWR_G", "0x04")
        self._create_param_widget(accel_group, "ACC_THRESHOLD_LOWPWR_DUR", "0x20")
        self._create_param_widget(accel_group, "ACC_THRESHOLD_MOVEMENT", 8)
        self._create_param_widget(accel_group, "ACC_THRESHOLD_DURATION", 0)

        # --- Accelerometer Double Tap Group ---
        dtap_group = ttk.LabelFrame(parent_tab, text="Accelerometer Double Tap Tuning", padding="10")
        dtap_group.pack(fill=tk.X, pady=5, padx=5)
        self._create_param_widget(dtap_group, "ACC_DOUBLE_TAP_THRESHOLD", "0x6E")
        self._create_param_widget(dtap_group, "ACC_DOUBLE_TAP_LIMIT", "0x20")
        self._create_param_widget(dtap_group, "ACC_DOUBLE_TAP_LATENCY", "0x10")
        self._create_param_widget(dtap_group, "ACC_DOUBLE_TAP_WINDOW", "0x30")

    def check_dependencies(self):
        """Checks for required command-line tools and updates the GUI."""
        import shutil
        import platform

        dependencies = ['make', 'arm-none-eabi-gcc']
        missing_deps = [dep for dep in dependencies if shutil.which(dep) is None]

        if not missing_deps:
            self.dependency_status_label.config(text="✅ Alle Abhängigkeiten sind installiert.", foreground="green")
            return True
        else:
            system = platform.system()
            message = f"❌ Fehlende Abhängigkeiten: {', '.join(missing_deps)}\n\n"
            if system == "Linux":
                message += "INSTALLATION (Debian/Ubuntu):\n`sudo apt-get update && sudo apt-get install build-essential gcc-arm-none-eabi`"
            elif system == "Windows":
                message += "INSTALLATION:\n"
                message += "1. ARM GCC: Installieren Sie 'GNU Arm Embedded Toolchain' (https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads).\n"
                message += "2. Make: Installieren Sie es z.B. via Chocolatey (`choco install make`).\n"
                message += "Stellen Sie sicher, dass beide im System-PATH sind."
            else: # macOS
                message += "INSTALLATION (macOS mit Homebrew):\n`brew install arm-none-eabi-gcc make`"

            self.dependency_status_label.config(text=message, foreground="red")
            return False

    def log(self, message):
        """Appends a message to the log window in a thread-safe way."""
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.update_idletasks()

    def start_build_thread(self):
        """Starts the build process in a new thread to keep the GUI responsive."""
        self.build_button.config(state=tk.DISABLED)
        self.log_text.delete(1.0, tk.END)
        self.log("Starte Kompilierung...\n")

        thread = threading.Thread(target=self.build_firmware)
        thread.daemon = True
        thread.start()

    def build_firmware(self):
        """Constructs and runs the make command."""
        try:
            cflags = []
            for name, var in self.vars.items():
                value = var.get()
                if isinstance(var, tk.BooleanVar):
                    # For boolean, the value is 1 if True, 0 if False
                    cflags.append(f"-D{name}={int(value)}")
                else:
                    # Basic sanitization for other values to prevent injection
                    safe_value = "".join(c for c in str(value) if c.isalnum() or c in ('_','-','.','x'))
                    cflags.append(f"-D{name}={safe_value}")

            cflags_str = " ".join(cflags)
            command = ['make', 'clean', 'all', f'CFLAGS_EXTRA={cflags_str}']

            self.log(f"Executing command: {' '.join(command)}\n\n")

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
            )

            for line in iter(process.stdout.readline, ''):
                self.log(line)

            process.wait()

            if process.returncode == 0:
                self.log("\n\n✅ Kompilierung erfolgreich!\n")

                # Add the flashing instructions
                flash_instructions = (
                    "\n--------------------------------------------------\n"
                    "Anleitung zum Flashen der Firmware:\n\n"
                    "1. Verbinden Sie Ihr Kiwiki-Gerät über den J-Link Debugger.\n"
                    "2. Öffnen Sie ein Terminal / eine Kommandozeile.\n"
                    "3. Führen Sie den folgenden Befehl aus, um die Firmware zu flashen:\n\n"
                    "   `JLinkExe -device nrf51822 -if swd -speed 1000 -AutoConnect 1 "
                    "-loadbin build/alice.bin 0`\n\n"
                    f"Die kompilierte Datei ist: `build/alice.bin`\n"
                    "--------------------------------------------------\n"
                )
                self.log(flash_instructions)
            else:
                self.log(f"\n\n❌ Fehler bei der Kompilierung! (Exit-Code: {process.returncode})\n")

        except Exception as e:
            self.log(f"\n\n❌ Ein unerwarteter Fehler ist aufgetreten: {e}\n")
        finally:
            # Schedule the button re-enabling to run in the main thread
            self.after(100, lambda: self.build_button.config(state=tk.NORMAL))


if __name__ == "__main__":
    app = FirmwareDesigner()
    app.mainloop()
