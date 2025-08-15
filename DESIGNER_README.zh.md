[English](DESIGNER_README.md) | [Deutsch](DESIGNER_README.de.md) | [Español](DESIGNER_README.es.md) | [Français](DESIGNER_README.fr.md) | [Русский](DESIGNER_README.ru.md) | [中文](DESIGNER_README.zh.md)

---

# Kiwiki 固件设计器

本工具提供一个图形用户界面（GUI），以便轻松配置和编译 Kiwiki 固件。

## Windows 10/11 使用说明

要在 Windows 上使用本工具，必须满足一些先决条件。

### 1. 安装先决条件

#### a) Python 3
该工具本身是一个 Python 脚本。
1.  从官方网站下载 Python 安装程序：[python.org](https://www.python.org/downloads/windows/)
2.  运行安装程序。**重要提示：** 在安装程序的第一个对话框中，勾选 **"Add Python to PATH"** 复选框。这对于从命令行轻松调用 Python至关重要。
3.  按照安装程序的其余说明进行操作。

#### b) GNU Arm 嵌入式工具链 (`arm-none-eabi-gcc`)
这是将固件的 C 代码转换为微控制器可执行文件的编译器。
1.  从 Arm 网站下载工具链。寻找最新的 "Windows x86_64 hosted cross toolchain"（以 `.zip` 文件形式）：[Arm GNU 工具链下载](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
2.  将 `.zip` 文件解压缩到您选择的目录，例如 `C:\Program Files\arm-gnu-toolchain`。
3.  将工具链的 `bin` 目录添加到您的系统 PATH。在 Windows 开始菜单中，搜索“编辑系统环境变量”，点击“环境变量...”，在“系统变量”部分选择 `Path`，点击“编辑...”，点击“新建”并添加路径，例如 `C:\Program Files\arm-gnu-toolchain\bin`。用“确定”确认所有窗口。

#### c) Make
`make` 是一个控制编译过程的工具。
在 Windows 上安装 `make` 的最简单方法是通过 [Chocolatey](https://chocolatey.org/) 包管理器。
1.  如果您还没有 Chocolatey，请按照网站上的说明进行安装（通常是在管理员 PowerShell 中运行的命令）。
2.  以管理员身份打开 PowerShell 并运行以下命令：
    ```sh
    choco install make
    ```
    或者，您可以将 `make` 作为 [Git for Windows](https://git-scm.com/download/win) 或 [MSYS2](https://www.msys2.org/) 的一部分进行安装。

### 2. 启动工具

安装完所有先决条件后, 您可以启动固件设计器：

1.  打开命令提示符 (`cmd.exe`) 或 PowerShell。
2.  使用 `cd` 导航到本项目的目录。
    ```sh
    cd path\to\project
    ```
3.  运行 Python 脚本：
    ```sh
    python designer.py
    ```

"Kiwiki 固件设计器" 窗口现在应该会打开。该工具在启动时会检查是否能找到 `make` 和 `arm-none-eabi-gcc` 并显示其状态。
