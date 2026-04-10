# Ansible Role: Prometheus Postgres Exporter

[![CI](https://github.com/lcd1232/ansible-role-prometheus-postgres/actions/workflows/ci.yml/badge.svg)](https://github.com/lcd1232/ansible-role-prometheus-postgres/actions/workflows/ci.yml)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-prometheus_postgres-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/lcd1232/prometheus_postgres/)

Installs and configures the [prometheus-community/postgres_exporter](https://github.com/prometheus-community/postgres_exporter) for exposing PostgreSQL metrics to Prometheus.

## Requirements

PostgreSQL must be installed and running on the target host.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    prometheus_postgres_version: "0.19.1"

The version of postgres_exporter to install.

    prometheus_postgres_dbname: postgres
    prometheus_postgres_data_source_name: >-
      user=postgres dbname={{ prometheus_postgres_dbname }}
      host=/var/run/postgresql/ sslmode=disable

Database connection settings. The data source name is passed as the `DATA_SOURCE_NAME` environment variable.

    prometheus_postgres_addr: "0.0.0.0"
    prometheus_postgres_port: 9187

Address and port for the metrics endpoint.

    prometheus_postgres_system_user: postgres

System user to run the exporter. If set to something other than `postgres`, the user will be created automatically.

    prometheus_postgres_state: started
    prometheus_postgres_enabled: true

Service state and boot enablement.

    prometheus_postgres_restart_handler_state: restarted

State to apply when the restart handler is triggered. Set to `reloaded` if you prefer graceful reloads.

    prometheus_postgres_enabled_collectors: []

Extra collectors to enable beyond upstream defaults. Example: `["postmaster", "stat_statements", "long_running_transactions"]`.

    prometheus_postgres_disabled_collectors: []

Collectors to explicitly disable from upstream defaults. Example: `["wal", "locks"]`.

    prometheus_postgres_options: ""

Extra CLI flags passed directly to postgres_exporter. Example: `"--collector.stat_statements.limit=200 --log.level=debug"`.

    prometheus_postgres_extend_query_path: ""

Path to a custom query YAML file. This uses the deprecated `--extend.query-path` flag. Leave empty to use built-in collectors only.

    prometheus_postgres_query_filenames: []
    prometheus_postgres_query_directory: files/

Legacy settings for assembling query files. Only used when `prometheus_postgres_extend_query_path` is set.

## Dependencies

None.

## Example Playbook

    - hosts: db
      roles:
        - lcd1232.prometheus_postgres

To enable additional collectors:

    - hosts: db
      roles:
        - role: lcd1232.prometheus_postgres
          prometheus_postgres_enabled_collectors:
            - stat_statements
            - postmaster

## License

BSD

## Author Information

Created by [lcd1232](https://github.com/lcd1232).
