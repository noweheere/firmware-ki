[English](DESIGNER_README.md) | [Deutsch](DESIGNER_README.de.md) | [Español](DESIGNER_README.es.md) | [Français](DESIGNER_README.fr.md) | [Русский](DESIGNER_README.ru.md) | [中文](DESIGNER_README.zh.md)

---

# Kiwiki Firmware Designer

Dieses Tool bietet eine grafische Benutzeroberfläche (GUI), um die Kiwiki-Firmware einfach zu konfigurieren und zu kompilieren.

## Anleitung für Windows 10/11

Um dieses Tool unter Windows zu verwenden, müssen einige Voraussetzungen erfüllt sein.

### 1. Voraussetzungen installieren

#### a) Python 3
Das Tool selbst ist ein Python-Skript.
1.  Laden Sie den Python-Installer von der offiziellen Webseite herunter: [python.org](https://www.python.org/downloads/windows/)
2.  Führen Sie den Installer aus. **Wichtig:** Setzen Sie im ersten Dialog des Installers den Haken bei **"Add Python to PATH"**. Dies ist entscheidend, damit Sie Python einfach von der Kommandozeile aus aufrufen können.
3.  Folgen Sie den weiteren Anweisungen des Installers.

#### b) GNU Arm Embedded Toolchain (`arm-none-eabi-gcc`)
Dies ist der Compiler, der den C-Code der Firmware in eine lauffähige Datei für den Mikrocontroller übersetzt.
1.  Laden Sie die Toolchain von der Arm-Webseite herunter. Suchen Sie nach der neuesten "Windows x86_64 hosted cross toolchain" (als `.zip`-Datei): [Arm GNU Toolchain Downloads](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
2.  Entpacken Sie die `.zip`-Datei in ein Verzeichnis Ihrer Wahl, z.B. `C:\Program Files\arm-gnu-toolchain`.
3.  Fügen Sie das `bin`-Verzeichnis der Toolchain zu Ihrem System-PATH hinzu:
    *   Suchen Sie im Windows-Startmenü nach "Umgebungsvariablen für dieses Konto bearbeiten".
    *   Wählen Sie in der oberen Liste die Variable `Path` aus und klicken Sie auf "Bearbeiten".
    *   Klicken Sie auf "Neu" und fügen Sie den Pfad zum `bin`-Verzeichnis hinzu, z.B. `C:\Program Files\arm-gnu-toolchain\bin`.
    *   Bestätigen Sie alle Fenster mit "OK".

#### c) Make
`make` ist ein Werkzeug, das den Kompilierungsprozess steuert.
Der einfachste Weg, `make` unter Windows zu installieren, ist über den Paketmanager [Chocolatey](https://chocolatey.org/).
1.  Falls Sie Chocolatey noch nicht haben, installieren Sie es, indem Sie den Anweisungen auf der Webseite folgen (normalerweise ein Befehl, den man in einer PowerShell mit Administratorrechten ausführt).
2.  Öffnen Sie eine PowerShell als Administrator und führen Sie folgenden Befehl aus:
    ```sh
    choco install make
    ```
    Alternativ können Sie `make` auch als Teil von [Git for Windows](https://git-scm.com/download/win) oder [MSYS2](https://www.msys2.org/) installieren.

### 2. Tool starten

Wenn alle Voraussetzungen installiert sind, können Sie den Firmware Designer starten:

1.  Öffnen Sie eine Kommandozeile (`cmd.exe`) oder eine PowerShell.
2.  Navigieren Sie mit `cd` in das Verzeichnis dieses Projekts.
    ```sh
    cd Pfad\zum\Projekt
    ```
3.  Führen Sie das Python-Skript aus:
    ```sh
    python designer.py
    ```

Das Fenster des "Kiwiki Firmware Designer" sollte sich nun öffnen. Das Tool prüft beim Start selbst, ob `make` und `arm-none-eabi-gcc` gefunden werden können und zeigt den Status an.
