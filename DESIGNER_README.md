[English](DESIGNER_README.md) | [Deutsch](DESIGNER_README.de.md) | [Español](DESIGNER_README.es.md) | [Français](DESIGNER_README.fr.md) | [Русский](DESIGNER_README.ru.md) | [中文](DESIGNER_README.zh.md)

---

# Kiwiki Firmware Designer

This tool provides a graphical user interface (GUI) to easily configure and compile the Kiwiki firmware.

## Instructions for Windows 10/11

To use this tool on Windows, a few prerequisites must be met.

### 1. Install Prerequisites

#### a) Python 3
The tool itself is a Python script.
1.  Download the Python installer from the official website: [python.org](https://www.python.org/downloads/windows/)
2.  Run the installer. **Important:** In the first dialog of the installer, check the box for **"Add Python to PATH"**. This is crucial so you can easily call Python from the command line.
3.  Follow the rest of the installer's instructions.

#### b) GNU Arm Embedded Toolchain (`arm-none-eabi-gcc`)
This is the compiler that translates the firmware's C code into an executable file for the microcontroller.
1.  Download the toolchain from the Arm website. Look for the latest "Windows x86_64 hosted cross toolchain" (as a `.zip` file): [Arm GNU Toolchain Downloads](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
2.  Unzip the `.zip` file to a directory of your choice, e.g., `C:\Program Files\arm-gnu-toolchain`.
3.  Add the toolchain's `bin` directory to your system PATH. In the Windows Start Menu, search for "Edit the system environment variables", click "Environment Variables...", select `Path` from the "System variables" section, click "Edit...", click "New" and add the path, e.g., `C:\Program Files\arm-gnu-toolchain\bin`. Confirm all windows with "OK".

#### c) Make
`make` is a tool that controls the compilation process.
The easiest way to install `make` on Windows is via the [Chocolatey](https://chocolatey.org/) package manager.
1.  If you don't already have Chocolatey, install it by following the instructions on the website (usually a command run in an administrative PowerShell).
2.  Open a PowerShell as Administrator and run the following command:
    ```sh
    choco install make
    ```
    Alternatively, you can install `make` as part of [Git for Windows](https://git-scm.com/download/win) or [MSYS2](https://www.msys2.org/).

### 2. Launch the Tool

Once all prerequisites are installed, you can start the Firmware Designer:

1.  Open a Command Prompt (`cmd.exe`) or PowerShell.
2.  Navigate to this project's directory using `cd`.
    ```sh
    cd path\to\project
    ```
3.  Run the Python script:
    ```sh
    python designer.py
    ```

The "Kiwiki Firmware Designer" window should now open. The tool checks on startup whether `make` and `arm-none-eabi-gcc` can be found and displays their status.
