
# UPM - User Friendly Package Manager for Linux Distributions

UPM (Unified Package Manager) is a user-friendly package manager designed for Debian, Fedora, Ubuntu, and Arch Linux distributions. It simplifies the process of software installation, updates, and maintenance, providing a streamlined user experience.


## Screenshots

UPM GUI

<p align = "center"><img src = "https://github.com/Dtechking/UPM/blob/master/4.png" width="65%"/></p>

Backend

<p align = "center">
    <img src="https://github.com/Dtechking/UPM/blob/master/1.png" width="45%" />
    <img src="https://github.com/Dtechking/UPM/blob/master/2.png" width="45%" />
</p>

Running GUI

<p align = "center"><img src = "https://github.com/Dtechking/UPM/blob/master/6.png" width="65%"/></p>

## Tech / Frameworks Used

**Backend:** Bash

**Frontend:** Python (PyQt)


## Features

- Install packages        :   Easily install packages by specifying the package name.
- Remove packages         :   Remove installed packages from your system.
- Update packages         :   Update installed packages to the latest versions.
- List installed packages :   View a list of all installed packages on your system.
- System upgrade          :   Upgrade your system to the latest version.
- Display system version  :   Get information about the current system version.
- Help and support        :   Access the help message and contact information for support.


## Prerequisites

* Linux distribution: Debian, Fedora, Ubuntu, or Arch Linux
* Bash (default shell)
## Installation

Install my-project with npm

Clone the UPM repository to your local machine:

```shell
    git clone https://github.com/username/upm.git
```

Change to the UPM directory:

```shell
    cd upm
```
Make the upm script executable:

```shell
    chmod +x upm.sh
```

Run UPM:

```shell
    ./upm.sh -help
```
## Usage

To use UPM, open a terminal and navigate to the directory where the upm.sh script is located. Then, you can run the script with various options and arguments to perform different tasks.

```shell
    ./upm.sh [option] [arguments]
```



## GUI Usage

UPM also provides a graphical user interface (GUI) for easier interaction. The GUI allows you to perform package installation, removal, updates, and view installed packages.

To launch the GUI, run the gui.py script:

```shell
    python3 gui.py
```
## Options

-aboutme            : Display information about the current user.

-install [package]  : Install the specified package.

-remove [package]   : Remove the specified package.

-update [package]   : Update the specified package.

-listall            : List all installed packages.

-sysupgrade         : Update the system.

-sysversion         : Display the system version.

-help               : Display the help message.
## Contributors

> Darshan B (2021503505)      - darshanthekingmaker@gmail.com
    
> Prasanna M (2021503535)     - prsnn450@gmail.com
    
> Sridhar P (2021503709)      - sridharpalanisamy171202@gmail.com

> Ajaykumar K (2021503003)    - ajaykumarbw21@gmail.com

