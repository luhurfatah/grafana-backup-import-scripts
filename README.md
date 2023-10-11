# Grafana Backup and Import Scripts

This repository contains a set of scripts for backing up and importing Grafana dashboards and datasources. These scripts can help you easily manage your Grafana configurations and ensure data consistency.

## Scripts

### Backup Scripts
1. `backup_dashboards.py`: Backs up all Grafana dashboards to individual JSON files.
2. `backup_datasources.py`: Backs up all Grafana datasources to individual JSON files.

### Import Scripts
3. `import_dashboards.sh`: Imports Grafana dashboards from JSON files into your Grafana instance.
4. `import_datasources.sh`: Imports Grafana datasources from JSON files into your Grafana instance.

## Usage

- Use the backup scripts to create local copies of your Grafana dashboards and datasources.
- Configure the import scripts with your Grafana instance details and execute them to import configurations.
- Detailed usage instructions are provided in each script's comments.

## Configuration

Before using the import scripts, make sure to configure them with your Grafana instance's address and API tokens. Refer to the individual script files for configuration options.

## Prerequisites

- Ensure you have `curl` and `jq` installed on your system for these scripts to work.

