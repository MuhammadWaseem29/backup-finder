#!/usr/bin/env python3
import os
import sys
import requests
from termcolor import colored
import argparse
from urllib.parse import urljoin

# Banner
def banner():
    os.system('clear')
    print(colored("""
  _   _                 _      __      __           
 | \ | |               | |     \ \    / /           
 |  \| | ___   ___   __| | ___ \ \  / /_ _ _ __ ___ 
 | . ` |/ _ \ / _ \ / _` |/ _ \ \ \/ / _` | '_ ` _ \\
 | |\  | (_) | (_) | (_| |  __/ \  / (_| | | | | | |
 |_| \_|\___/ \___/ \__,_|\___|  \/ \__,_|_| |_| |_|
    Created by Muhammad Waseem
    """, 'cyan'))

# List of backup file extensions
backup_extensions = [
    '.bak', '.backup', '.bkp', '.old', '.orig', '.swp', '.swm', '.temp', '.~', 
    '.tar', '.gz', '.tgz', '.tar.gz', '.zip', '.tar.bz2', '.tar.xz', '.bak1',
    '.bak2', '.bak3', '.swo', '.swn', '.dmp', '.ps1', '.config', '.htpasswd', '.htaccess', '.env', 
    '.bak5', '.db', '.bak1', '.bak2', '.bak3', '.bak4', '.bak5', '.bkp', '.bck', '.backup', '.bkp1', 
    '.bkp2', '.bkp3', '.temp', '.swp', '.swm', '.swp1', '.swp2', '.~swp', '.old', '.orig', '.swo', 
    '.swn', '.ps1', '.config', '.env', '.tar', '.tar.gz', '.tgz', '.zip', '.tar.bz2', '.tar.xz', 
    '.gz', '.rar', '.tar.lz', '.tar.xz', '.dump', '.sql', '.sql.gz', '.bak2', '.tar.bz2', '.bak3',
    '.bak4', '.dat', '.swp', '.log', '.taz', '.bak5', '.bin', '.db', '.msi', '.pkg', '.dmp', 
    '.bakfile', '.bak2021', '.oldversion', '.log1', '.cpbackup', '.vhd', '.bakup', '.vhdx', 
    '.snapshot', '.macosx', '.backup1', '.backup2', '.xbackup', '.dbbak', '.datbak', '.dmpbak', 
    '.tarlog', '.smbbak', '.logs', '.baklog', '.tdb', '.configbak', '.ntbackup', '.txtbak', '.exe.bak', 
    '.xmlbak', '.yamlbak', '.txt.bak', '.pkg.bak', '.dbr', '.tarbackup', '.zip1', '.zip2', '.tarbak', 
    '.tar.gz1', '.tar.gz2', '.tar.gzip', '.bakp', '.slk', '.sql-backup', '.sql_backup', '.cp-backup', 
    '.phplog', '.phpbak', '.backup-old', '.urlbak', '.confbak', '.bak-archive', '.bak-zip', '.bin-backup', 
    '.htaccess-backup', '.htpasswd-backup', '.wp-backup', '.php-backup', '.apppackage', '.tar1', '.gz1', 
    '.bz2', '.gzip', '.zip3', '.tgz1', '.bak.tar', '.pkl', '.pdb', '.dll.bak', '.apk', '.bak-archive', 
    '.cfile', '.m4v', '.mp4bak', '.bakimage', '.dbf', '.bakweb', '.configbak', '.mediadump', '.filesbackup', 
    '.tmp', '.mkv.bak', '.nfs', '.partitionbak', '.clone', '.symlinkbak', '.keybak', '.zbak', '.sqlbak', 
    '.xhtmlbak', '.dbbackup', '.archives', '.archives-backup', '.json-backup', '.logbak', '.backupdata', 
    '.autosave', '.documentbackup', '.tiffbak', '.cmdbak', '.db-backup', '.plist', '.diskimage', '.resbak',
    '.vmdk', '.nfsbak', '.rollback', '.recovery', '.backupfiles', '.conf1', '.conf2', '.configold', 
    '.dllbackup', '.gitbak', '.svnbackup', '.remotebackup', '.lazback', '.logfiles', '.bz2bak', 
    '.datbackup', '.md5back', '.ftpbackup', '.rawbackup', '.tmpbak', '.configrestore', '.zipbak', 
    '.directories', '.configrestore1', '.swp-backup', '.membackup', '.merge-backup', '.binrestore',
    '.tarrestore', '.rawrestore', '.dumper', '.htaccessrestore', '.backupfolder', '.backupdata1',
    '.restorebackup', '.ziprestore', '.databasebackup', '.php-config-backup'
]

# 100 unique extensions related to Cloud Platforms, Servers, CMS etc.
cloud_server_extensions = [
    '.aws', '.azurebackup', '.nginx', '.wordpress', '.wpconfig', '.gitlab', '.dockerfile', '.kubernetes', 
    '.vpcbackup', '.ebs', '.cloudtrail', '.s3', '.rds', '.ec2', '.cloudformation', '.lambda', '.cloudfront', 
    '.route53', '.cloudwatch', '.api', '.cmsbackup', '.vpc', '.virtualbox', '.docker', '.wpbackup', '.wp-config', 
    '.nginxbackup', '.my.cnf', '.appdata', '.vhosts', '.config.json', '.env.docker', '.settings.php', 
    '.mysql-dump', '.k8s', '.helm', '.terraform', '.redis-backup', '.couchdb-backup', '.sphinx-backup', 
    '.openstack', '.sqlserverbak', '.apache2', '.nginxconfig', '.wordpress-database', '.admin-backup', '.dbdump', 
    '.k8sdump', '.gitconfig', '.gitignore', '.docker-compose', '.mongodump', '.mongodb-dump', '.nfs-backup', 
    '.sql-backup', '.pgbackup', '.laravel', '.laravel-backup', '.dockerfile-backup', '.grafana-backup', 
    '.prometheus-backup', '.nginx-logs', '.apache-logs', '.user-config', '.site-backup', '.auth-config', 
    '.azure-dump', '.az-backup', '.gcloud-backup', '.kubectl-config', '.rancher-backup', '.wordpress-uploads', 
    '.wordpress-theme-backup', '.cdn-backup', '.lighthouse-backup', '.nginx-conf-backup', '.php.ini-backup', 
    '.varnish-backup', '.postgres-dump', '.postgres-backup', '.redis-dump', '.s3-backup', '.mongodb-backup', 
    '.docker-dump', '.jenkins-backup', '.ci-backup', '.apache2-backup', '.ecr-backup', '.vagrant-backup', 
    '.saml-backup', '.json-backup', '.docker-image-backup', '.haproxy-backup', '.ci-cd-config', '.azure-config', 
    '.cloudstack-backup', '.restic-backup', '.backup-report', '.pivotal-backup', '.cloud-config', '.gh-backup', 
    '.bitbucket-backup', '.github-backup', '.docker-compose-backup', '.wpdb-backup', '.terraform-backup', 
    '.provision-backup', '.hcl-backup', '.slack-backup', '.prisma-backup', '.consul-backup'
]

backup_extensions.extend(cloud_server_extensions)

# Function to scan a single URL for backup files
def scan_url_for_backups(url):
    try:
        for ext in backup_extensions:
            backup_url = url + ext
            response = requests.get(backup_url)
            status_code = response.status_code
            if status_code == 200:
                print(colored(f"Backup file found: {backup_url} (Status Code: {status_code})", 'green'))
            elif status_code == 403:
                print(colored(f"Access forbidden for: {backup_url} (Status Code: {status_code})", 'yellow'))
            elif status_code == 404:
                print(colored(f"Backup file not found: {backup_url} (Status Code: {status_code})", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Error with URL {url}: {e}", 'red'))

# Function to scan URLs from a file
def scan_file_for_backups(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            urls = f.readlines()
            for url in urls:
                url = url.strip()
                print(colored(f"Scanning URL: {url}", 'blue'))
                scan_url_for_backups(url)
    else:
        print(colored(f"File {file} not found!", 'red'))

# Save output to a file
def save_output(output, file_name):
    with open(file_name, 'a') as f:
        f.write(output + "\n")
    print(colored(f"Output saved to {file_name}", 'green'))

# Main function to parse arguments and execute the tool
def main():
    banner()

    parser = argparse.ArgumentParser(description="Noob-Wasi: A powerful backup file scanner tool")
    parser.add_argument('-u', '--url', type=str, help="Scan a single URL for backup files")
    parser.add_argument('-f', '--file', type=str, help="Scan URLs from a file for backup files")
    parser.add_argument('-o', '--output', type=str, help="Save output to a file")
    parser.add_argument('-c', '--color', action='store_true', help="Enable colorful output")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    args = parser.parse_args()

    if args.url:
        print(colored(f"Scanning single URL: {args.url} for backup files", 'blue'))
        scan_url_for_backups(args.url)
        if args.output:
            save_output(f"Scanned URL: {args.url} for backup files", args.output)

    elif args.file:
        print(colored(f"Scanning URLs from file: {args.file} for backup files", 'blue'))
        scan_file_for_backups(args.file)
        if args.output:
            save_output(f"Scanned URLs from file: {args.file} for backup files", args.output)

    else:
        print(colored("No URL or file provided. Use -u for URL or -f for file.", 'red'))
        sys.exit(1)

    if args.verbose:
        print(colored("Verbose mode enabled. Displaying additional information.", 'yellow'))

if __name__ == '__main__':
    main()
