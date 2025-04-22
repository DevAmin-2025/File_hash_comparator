# File Hash Comparator
This Python script computes the SHA-256 hash of two files and compares their hashes to determine whether the files are identical or different. It supports both regular file paths and Windows Subsystem for Linux (WSL)-compatible paths, making it a versatile tool for users working in mixed environments.

## Features
- Converts Windows file paths to WSL-compatible paths when necessary(if using **WSL**).
- Computes the SHA-256 hash of files, ensuring compatibility with large files by reading them in chunks.
- Compares two files and notifies the user if they are identical or different.
- Provides error handling for missing files.
- Outputs messages with color formatting using the `termcolor` library for better visibility.

## How to Use
**Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

Navigate to the project directory and make sure to install the necessary requirements(if any).
```bash
cd File_hash_comparator
pip install -r requirements.txt
```
Run the script `run.py` in command-line-interface.
```bash
python run.py
```
### Example Usage
```bash
Enter path to the first file: /path/to/first/file
Enter path to the second file: /path/to/second/file
Two files are identical.
```
## Limitations
- This script does **not work on Windows** as it relies on converting Windows file paths to WSL-compatible paths using the `wslpath` command.
- To use this script, ensure you are running it on a Unix-based system or in a Linux environment (e.g., WSL on Windows, macOS, or Linux).
