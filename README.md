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

