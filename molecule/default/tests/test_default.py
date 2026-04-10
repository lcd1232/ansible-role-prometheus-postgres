import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_running(host):
    svc = host.service('prometheus-postgres-exporter')
    assert svc.is_running
    assert svc.is_enabled


def test_metrics_endpoint(host):
    cmd = "python3 -c \"import urllib.request; print(urllib.request.urlopen('http://localhost:19187/metrics').read().decode())\""
    out = host.check_output(cmd)
    assert 'pg_database_size_bytes' in out


def test_database_metric(host):
    cmd = "python3 -c \"import urllib.request; print(urllib.request.urlopen('http://localhost:19187/metrics').read().decode())\""
    out = host.check_output(cmd)
    assert 'datname="alice"' in out
