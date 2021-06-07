import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_mariadb_running_and_enabled(host):
    mariadb = host.service("mariadb")
    assert mariadb.is_running
    assert mariadb.is_enabled


def test_mariadb_config(host):
    config = host.run("/usr/bin/mysqladmin variables | tr -d ' '").stdout

    assert "|datadir|/var/lib/mysql/|" in config
    assert "|port|3306|" in config
    assert "|socket|/var/run/mysqld/mysqld.sock|" in config
    assert "|pid_file|/var/run/mysqld/mysqld.pid|" in config
    assert "|tx_isolation|READ-COMMITTED|" in config
    assert "|log_error|/var/log/mysql/error.log|" in config
