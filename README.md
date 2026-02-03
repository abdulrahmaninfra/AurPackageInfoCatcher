# AUR Package Checker 📦

A lightweight Python utility designed to fetch real-time information and safety metrics for packages on the **Arch User Repository (AUR)**. By interfacing with the official AUR RPC API, this tool helps users quickly vet packages before installation.

## 🚀 Features
* **Real-time Data:** Fetches package name, version, description, and official website.
* **Snapshot Links:** Generates a direct download link for the package source (tarball).
* **The "Sus" Detector:** A built-in logic system that evaluates package safety based on community trust metrics.
* **Clean UI:** Automatic screen clearing and formatted terminal output for better readability.

---

## 🛡️ Security Assessment Logic
Since anyone can upload to the AUR, this tool classifies packages into three safety tiers based on **Votes** and **Popularity**:

| Status | Criteria | Risk Level |
| :--- | :--- | :--- |
| **Safe** | > 50 Votes & > 1.0 Popularity | Low - Community Staples |
| **Likely Safe** | >= 10 Votes | Moderate - Established |
| **Getting Sus** | < 10 Votes | High - **Inspect PKGBUILD carefully!** |



---

## 🛠️ Installation

### 1. Requirements
Ensure you have Python installed and the `requests` library:
```bash
pip install requests

2. Setup

Clone this repository or copy the main.py file:
Bash

git clone [https://github.com/yourusername/aur-checker.git](https://github.com/yourusername/aur-checker.git)
cd aur-checker

🖥️ Usage

Run the script:
Bash

python main.py

Example Output:
Plaintext

Enter the AUR package name
    >>> visual-studio-code-bin

Name: visual-studio-code-bin
Version: 1.86.0-1
Description: Visual Studio Code (Open Source) binary version
Website: [https://code.visualstudio.com/](https://code.visualstudio.com/)
Snapshot: [https://aur.archlinux.org/cgit/aur.git/snapshot/visual-studio-code-bin.tar.gz](https://aur.archlinux.org/cgit/aur.git/snapshot/visual-studio-code-bin.tar.gz)
Votes: 2450
Popularity: 89.4
Status: Safe

⚙️ How It Works

The script follows a simple request-response cycle to ensure you get the most up-to-date data directly from the Arch Linux infrastructure.

    User Input: Takes the package name.

    API Call: Sends a request to https://aur.archlinux.org/rpc/.

    Parsing: Extracts JSON data and calculates the safety status.

    Display: Prints a clean summary to the terminal.

⚠️ Disclaimer

The "Status" provided by this tool is a community-based heuristic. Always remember the golden rule of the AUR: Always manually inspect the PKGBUILD and associated files before running makepkg.
