

```markdown
# Noob-Wasi: A Powerful Backup File Scanner

**Noob-Wasi** is a powerful tool created by **Muhammad Waseem** to scan URLs or files for common backup files. This script helps cybersecurity professionals, bug bounty hunters, and penetration testers identify backup files and configurations that could be exposed to the internet. 

The tool supports scanning for backup files across various platforms, including cloud services (AWS, Azure), web servers (Nginx, Apache), and content management systems (WordPress).

---

## Features

- Scans a single URL or multiple URLs from a file for exposed backup files.
- Supports a wide range of backup file extensions, including cloud, CMS, and server configurations.
- Colorful and easy-to-read output for success, failure, and access restrictions.
- Option to save output to a file for future analysis.
- Useful for bug bounty hunters and penetration testers.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MuhammadWaseem29/backup-finder.git
    cd backup-finder
    ```

2. Install the required Python libraries (manually via pip):
    ```bash
    pip install requests termcolor
    ```

---

## Usage

### Scan a Single URL

To scan a single URL for backup files:

```bash
python noob-wasi.py -u http://example.com
```

### Scan Multiple URLs from a File

To scan URLs listed in a text file (`urls.txt`), use:

```bash
python noob-wasi.py -f urls.txt
```

### Save Output to a File

To save the results to an output file:

```bash
python noob-wasi.py -u http://example.com -o output.txt
```

### Enable Colorful Output

To enable colorful output (default is enabled):

```bash
python noob-wasi.py -u http://example.com -c
```

### Verbose Output

Enable verbose output for detailed information:

```bash
python noob-wasi.py -u http://example.com -v
```

---

## Supported Extensions

- **Cloud Platforms:** AWS, Azure, GCP, DigitalOcean, etc.
- **CMS Platforms:** WordPress, Joomla, Drupal, etc.
- **Web Servers:** Nginx, Apache, IIS.
- **Backup Files:** `.bak`, `.tar.gz`, `.zip`, `.sql`, `.env`, `.bak1`, `.swp`, `.dmp`, and many more.

The tool supports over **200 different extensions** related to backup files across various platforms.

---

## Example Output

When running the script, the output will be colorful, showing results for each URL or file scanned:

```bash
Scanning URL: http://example.com
Backup file found: http://example.com/.env (Status Code: 200) [green]
Backup file not found: http://example.com/.bak (Status Code: 404) [red]
```

---

## Contributing

Contributions are welcome! Feel free to fork the repository and create pull requests.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make your changes and commit them (`git commit -m 'Add feature XYZ'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This tool is intended for educational purposes and ethical hacking. Do not use it on websites or systems without proper authorization. The creator of this tool is not responsible for any misuse or damage caused by the use of this script.
```

This version of the README excludes the **requirements.txt** section but includes manual installation instructions for the required libraries (`requests` and `termcolor`).
