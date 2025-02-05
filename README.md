

```bash
# Noob-Wasi: Backup File Finder

Noob-Wasi is an advanced open-source tool designed for cybersecurity professionals to find exposed backup files, configuration files, and sensitive information across a wide range of web servers, cloud platforms, and content management systems (CMS). It supports scanning for over 200 backup file extensions.

---

## Features

- **Backup File Detection:** Detects exposed backup files from cloud platforms (AWS, Azure), web servers (Apache, Nginx), CMS (WordPress, Joomla), and more.
- **Comprehensive Extension List:** Scans a wide variety of backup file extensions such as .bak, .zip, .sql, .tar.gz, and more.
- **Fast Scanning:** Optimized to scan multiple URLs quickly and efficiently.
- **Customizable Output:** Option to output results to a file. Supports colorful, easy-to-read terminal output.
- **Simple CLI:** Designed with simplicity in mind, allowing users to scan websites using a few simple commands.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/MuhammadWaseem29/backup-finder.git
cd backup-finder```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Scan a Single URL

```bash
python noob-wasi.py -u http://example.com
```

### Scan Multiple URLs from a File

```bash
python noob-wasi.py -f urls.txt
```

### Scan a URL and Save Results to a File

```bash
python noob-wasi.py -u http://example.com -o output.txt
```

### Enable Colorful Output (Default)

Colorful output is enabled by default, but you can explicitly enable it with:

```bash
python noob-wasi.py -u http://example.com -c
```

### Enable Verbose Output

```bash
python noob-wasi.py -u http://example.com -v
```

---

## Supported Extensions

Noob-Wasi detects backup files from various platforms, including:

- **Cloud Platforms:** AWS, Azure, Google Cloud, DigitalOcean
- **Web Servers:** Apache, Nginx, IIS
- **CMS:** WordPress, Joomla, Drupal
- **Backup File Types:** .bak, .zip, .tar.gz, .sql, .env, .dmp, .swp, and more.

It currently supports over 200 extensions.

---

## Example Output

When running Noob-Wasi, you'll get a clear and colorful output indicating the presence of backup files:

```plaintext
Scanning URL: http://example.com
Backup file found: http://example.com/.env (Status Code: 200) [Green]
Backup file not found: http://example.com/.bak (Status Code: 404) [Red]
```

---

## Contributing

We welcome contributions to Noob-Wasi! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add feature XYZ'
   ```

4. Push to your forked repository:

   ```bash
   git push origin feature-name
   ```

5. Create a pull request to the main repository.

Make sure to write clear commit messages and provide proper documentation for new features.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Disclaimer

Noob-Wasi is intended for educational purposes and authorized security testing only. Unauthorized usage or scanning of websites without permission is illegal and unethical. Always ensure you have explicit authorization before scanning systems.

The creator, Muhammad Waseem, is not responsible for any misuse, damage, or legal consequences that result from the use of this tool.

---
