import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_mariadb_running_and_enabled(host):
    mariadb = host.service("rh-mariadb103-mariadb")
    assert mariadb.is_running
    assert mariadb.is_enabled


def test_mariadb_syspaths(host):
    mysql_client = host.file("/usr/bin/mysql")
    mysql_version = host.run("/usr/bin/mysql --version").stdout

    assert mysql_client.exists
    assert "/opt/rh/rh-mariadb103/root/usr/bin/mysql" in mysql_version
    assert "Distrib 10.3" in mysql_version


def test_mariadb_config(host):
    config = host.run("/opt/rh/rh-mariadb103/root/bin/mysqladmin variables | tr -d ' '").stdout

    assert "|datadir|/var/opt/rh/rh-mariadb103/lib/mysql/|" in config
    assert "|port|3306|" in config
    assert "|socket|/var/lib/mysql/mysql.sock|" in config
    assert "|pid_file|/var/run/rh-mariadb103-mariadb/mariadb.pid|" in config
    assert "|tx_isolation|READ-COMMITTED|" in config
    assert "|log_error|/var/opt/rh/rh-mariadb103/log/mariadb/mariadb.log|" in config
