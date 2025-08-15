[English](DESIGNER_README.md) | [Deutsch](DESIGNER_README.de.md) | [Español](DESIGNER_README.es.md) | [Français](DESIGNER_README.fr.md) | [Русский](DESIGNER_README.ru.md) | [中文](DESIGNER_README.zh.md)

---

# Concepteur de Firmware Kiwiki

Cet outil fournit une interface utilisateur graphique (GUI) pour configurer et compiler facilement le firmware Kiwiki.

## Instructions pour Windows 10/11

Pour utiliser cet outil sous Windows, quelques prérequis doivent être satisfaits.

### 1. Installer les prérequis

#### a) Python 3
L'outil lui-même est un script Python.
1.  Téléchargez l'installateur de Python depuis le site officiel : [python.org](https://www.python.org/downloads/windows/)
2.  Exécutez l'installateur. **Important :** Dans la première boîte de dialogue de l'installateur, cochez la case **"Add Python to PATH"**. C'est crucial pour pouvoir appeler Python facilement depuis la ligne de commande.
3.  Suivez le reste des instructions de l'installateur.

#### b) GNU Arm Embedded Toolchain (`arm-none-eabi-gcc`)
C'est le compilateur qui traduit le code C du firmware en un fichier exécutable pour le microcontrôleur.
1.  Téléchargez la chaîne d'outils depuis le site web d'Arm. Cherchez la dernière "Windows x86_64 hosted cross toolchain" (sous forme de fichier `.zip`) : [Téléchargements de l'Arm GNU Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
2.  Décompressez le fichier `.zip` dans un répertoire de votre choix, par exemple, `C:\Program Files\arm-gnu-toolchain`.
3.  Ajoutez le répertoire `bin` de la chaîne d'outils à votre PATH système. Dans le menu Démarrer de Windows, recherchez "Modifier les variables d'environnement système", cliquez sur "Variables d'environnement...", sélectionnez `Path` dans la section "Variables système", cliquez sur "Modifier...", cliquez sur "Nouveau" et ajoutez le chemin, par exemple, `C:\Program Files\arm-gnu-toolchain\bin`. Confirmez toutes les fenêtres avec "OK".

#### c) Make
`make` est un outil qui contrôle le processus de compilation.
La manière la plus simple d'installer `make` sous Windows est via le gestionnaire de paquets [Chocolatey](https://chocolatey.org/).
1.  Si vous n'avez pas encore Chocolatey, installez-le en suivant les instructions sur le site web (généralement une commande exécutée dans un PowerShell en tant qu'administrateur).
2.  Ouvrez une PowerShell en tant qu'administrateur et exécutez la commande suivante :
    ```sh
    choco install make
    ```
    Alternativement, vous pouvez installer `make` dans le cadre de [Git for Windows](https://git-scm.com/download/win) ou [MSYS2](https://www.msys2.org/).

### 2. Lancer l'outil

Une fois tous les prérequis installés, vous pouvez démarrer le Concepteur de Firmware :

1.  Ouvrez une invite de commandes (`cmd.exe`) ou PowerShell.
2.  Naviguez vers le répertoire de ce projet en utilisant `cd`.
    ```sh
    cd chemin\vers\votre\projet
    ```
3.  Exécutez le script Python :
    ```sh
    python designer.py
    ```

La fenêtre "Concepteur de Firmware Kiwiki" devrait maintenant s'ouvrir. L'outil vérifie au démarrage si `make` et `arm-none-eabi-gcc` peuvent être trouvés et affiche leur statut.
