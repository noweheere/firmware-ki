[English](DESIGNER_README.md) | [Deutsch](DESIGNER_README.de.md) | [Español](DESIGNER_README.es.md) | [Français](DESIGNER_README.fr.md) | [Русский](DESIGNER_README.ru.md) | [中文](DESIGNER_README.zh.md)

---

# Diseñador de Firmware Kiwiki

Esta herramienta proporciona una interfaz gráfica de usuario (GUI) para configurar y compilar fácilmente el firmware de Kiwiki.

## Instrucciones para Windows 10/11

Para usar esta herramienta en Windows, se deben cumplir algunos requisitos previos.

### 1. Instalar Prerrequisitos

#### a) Python 3
La herramienta en sí es un script de Python.
1.  Descargue el instalador de Python desde el sitio web oficial: [python.org](https://www.python.org/downloads/windows/)
2.  Ejecute el instalador. **Importante:** En el primer diálogo del instalador, marque la casilla **"Add Python to PATH"**. Esto es crucial para poder llamar a Python fácilmente desde la línea de comandos.
3.  Siga el resto de las instrucciones del instalador.

#### b) GNU Arm Embedded Toolchain (`arm-none-eabi-gcc`)
Este es el compilador que traduce el código C del firmware a un archivo ejecutable para el microcontrolador.
1.  Descargue la cadena de herramientas del sitio web de Arm. Busque la última "Windows x86_64 hosted cross toolchain" (como archivo `.zip`): [Descargas de Arm GNU Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
2.  Descomprima el archivo `.zip` en un directorio de su elección, por ejemplo, `C:\Program Files\arm-gnu-toolchain`.
3.  Agregue el directorio `bin` de la cadena de herramientas a su PATH del sistema. En el menú de inicio de Windows, busque "Editar las variables de entorno del sistema", haga clic en "Variables de entorno...", seleccione `Path` en la sección "Variables del sistema", haga clic en "Editar...", haga clic en "Nuevo" y agregue la ruta, por ejemplo, `C:\Program Files\arm-gnu-toolchain\bin`. Confirme todas las ventanas con "OK".

#### c) Make
`make` es una herramienta que controla el proceso de compilación.
La forma más fácil de instalar `make` en Windows es a través del gestor de paquetes [Chocolatey](https://chocolatey.org/).
1.  Si aún no tiene Chocolatey, instálelo siguiendo las instrucciones del sitio web (generalmente un comando que se ejecuta en una PowerShell de administrador).
2.  Abra una PowerShell como Administrador y ejecute el siguiente comando:
    ```sh
    choco install make
    ```
    Alternativamente, puede instalar `make` como parte de [Git for Windows](https://git-scm.com/download/win) o [MSYS2](https://www.msys2.org/).

### 2. Iniciar la Herramienta

Una vez que todos los prerrequisitos estén instalados, puede iniciar el Diseñador de Firmware:

1.  Abra un Símbolo del sistema (`cmd.exe`) o PowerShell.
2.  Navegue al directorio de este proyecto usando `cd`.
    ```sh
    cd ruta\a\su\proyecto
    ```
3.  Ejecute el script de Python:
    ```sh
    python designer.py
    ```

La ventana "Diseñador de Firmware Kiwiki" debería abrirse. La herramienta comprueba al inicio si se pueden encontrar `make` y `arm-none-eabi-gcc` y muestra su estado.
