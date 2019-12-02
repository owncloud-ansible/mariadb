---
title: mariadb
type: docs
---

> **WARNING**: This Ansible role is currently in beta state. Use it at your own risk. 

Role to setup MariaDB server.

* [Default Variables](#default-variables)
  * [mariadb_bind_address](#mariadb-bind-address)
  * [mariadb_config_file](#mariadb-config-file)
  * [mariadb_config_include_dir](#mariadb-config-include-dir)
  * [mariadb_config_include_files](#mariadb-config-include-files)
  * [mariadb_databases](#mariadb-databases)
  * [mariadb_datadir](#mariadb-datadir)
  * [mariadb_enabled_on_startup](#mariadb-enabled-on-startup)
  * [mariadb_event_scheduler_state](#mariadb-event-scheduler-state)
  * [mariadb_group_concat_max_len](#mariadb-group-concat-max-len)
  * [mariadb_innodb_buffer_pool_size](#mariadb-innodb-buffer-pool-size)
  * [mariadb_innodb_file_per_table](#mariadb-innodb-file-per-table)
  * [mariadb_innodb_flush_log_at_trx_commit](#mariadb-innodb-flush-log-at-trx-commit)
  * [mariadb_innodb_flush_method](#mariadb-innodb-flush-method)
  * [mariadb_innodb_io_capacity](#mariadb-innodb-io-capacity)
  * [mariadb_innodb_lock_wait_timeout](#mariadb-innodb-lock-wait-timeout)
  * [mariadb_innodb_log_buffer_size](#mariadb-innodb-log-buffer-size)
  * [mariadb_innodb_log_file_size](#mariadb-innodb-log-file-size)
  * [mariadb_innodb_read_io_threads](#mariadb-innodb-read-io-threads)
  * [mariadb_innodb_write_io_threads](#mariadb-innodb-write-io-threads)
  * [mariadb_join_buffer_size](#mariadb-join-buffer-size)
  * [mariadb_key_buffer_size](#mariadb-key-buffer-size)
  * [mariadb_log_error](#mariadb-log-error)
  * [mariadb_log_file_group](#mariadb-log-file-group)
  * [mariadb_lower_case_table_names](#mariadb-lower-case-table-names)
  * [mariadb_max_allowed_packet](#mariadb-max-allowed-packet)
  * [mariadb_max_connections](#mariadb-max-connections)
  * [mariadb_max_heap_table_size](#mariadb-max-heap-table-size)
  * [mariadb_myisam_sort_buffer_size](#mariadb-myisam-sort-buffer-size)
  * [mariadb_mysqldump_max_allowed_packet](#mariadb-mysqldump-max-allowed-packet)
  * [mariadb_overwrite_global_mycnf](#mariadb-overwrite-global-mycnf)
  * [mariadb_packages](#mariadb-packages)
  * [mariadb_packages_extra](#mariadb-packages-extra)
  * [mariadb_pid_file](#mariadb-pid-file)
  * [mariadb_port](#mariadb-port)
  * [mariadb_query_cache_limit](#mariadb-query-cache-limit)
  * [mariadb_query_cache_size](#mariadb-query-cache-size)
  * [mariadb_query_cache_type](#mariadb-query-cache-type)
  * [mariadb_read_buffer_size](#mariadb-read-buffer-size)
  * [mariadb_read_rnd_buffer_size](#mariadb-read-rnd-buffer-size)
  * [mariadb_root_password](#mariadb-root-password)
  * [mariadb_skip_name_resolve](#mariadb-skip-name-resolve)
  * [mariadb_socket](#mariadb-socket)
  * [mariadb_sort_buffer_size](#mariadb-sort-buffer-size)
  * [mariadb_sql_mode](#mariadb-sql-mode)
  * [mariadb_sync_binlog](#mariadb-sync-binlog)
  * [mariadb_table_open_cache](#mariadb-table-open-cache)
  * [mariadb_thread_cache_size](#mariadb-thread-cache-size)
  * [mariadb_tmp_table_size](#mariadb-tmp-table-size)
  * [mariadb_transaction_isolation_level](#mariadb-transaction-isolation-level)
  * [mariadb_users](#mariadb-users)
  * [mariadb_wait_timeout](#mariadb-wait-timeout)
* [Dependencies](#dependencies)

---

## Default Variables

### mariadb_bind_address

#### Default value

```YAML
mariadb_bind_address: 127.0.0.0
```

### mariadb_config_file

#### Example usage

```YAML
mariadb_config_file: /etc/mysql/mariadb.cnf
```

### mariadb_config_include_dir

Include dir for custom MariaDB config files. The default value depends on the operatig system.

#### Example usage

```YAML
mariadb_config_include_dir: /etc/mysql/conf.d
```

### mariadb_config_include_files

#### Default value

```YAML
mariadb_config_include_files: []
```

#### Example usage

```YAML
mariadb_config_include_files:
- src: path/relative/to/playbook/file.cnf
- src: path/relative/to/playbook/anotherfile.cnf
force: yes
```

### mariadb_databases

#### Default value

```YAML
mariadb_databases:
  - name: owncloud
    collation: utf8mb4_bin
    encoding: utf8mb4
```

### mariadb_datadir

MariaDB data directory to use. Default value depends on your operating system.

#### Example usage

```YAML
mariadb_datadir: /var/lib/mysql
```

### mariadb_enabled_on_startup

#### Default value

```YAML
mariadb_enabled_on_startup: true
```

### mariadb_event_scheduler_state

#### Default value

```YAML
mariadb_event_scheduler_state: OFF
```

### mariadb_group_concat_max_len

#### Default value

```YAML
mariadb_group_concat_max_len: '1024'
```

### mariadb_innodb_buffer_pool_size

#### Default value

```YAML
mariadb_innodb_buffer_pool_size: 256M
```

### mariadb_innodb_file_per_table

#### Default value

```YAML
mariadb_innodb_file_per_table: ON
```

### mariadb_innodb_flush_log_at_trx_commit

#### Default value

```YAML
mariadb_innodb_flush_log_at_trx_commit: '1'
```

### mariadb_innodb_flush_method

#### Default value

```YAML
mariadb_innodb_flush_method: O_DIRECT
```

### mariadb_innodb_io_capacity

#### Default value

```YAML
mariadb_innodb_io_capacity: 200
```

### mariadb_innodb_lock_wait_timeout

#### Default value

```YAML
mariadb_innodb_lock_wait_timeout: '50'
```

### mariadb_innodb_log_buffer_size

#### Default value

```YAML
mariadb_innodb_log_buffer_size: 8M
```

### mariadb_innodb_log_file_size

#### Default value

```YAML
mariadb_innodb_log_file_size: 128M
```

### mariadb_innodb_read_io_threads

#### Default value

```YAML
mariadb_innodb_read_io_threads: 4
```

### mariadb_innodb_write_io_threads

#### Default value

```YAML
mariadb_innodb_write_io_threads: '{{ mariadb_innodb_read_io_threads }}'
```

### mariadb_join_buffer_size

#### Default value

```YAML
mariadb_join_buffer_size: '262144'
```

### mariadb_key_buffer_size

#### Default value

```YAML
mariadb_key_buffer_size: 256M
```

### mariadb_log_error

Default value depends on your operating system.

#### Example usage

```YAML
mariadb_log_error: /var/log/mysql/error.log
```

### mariadb_log_file_group

Default value depends on your operating system.

#### Example usage

```YAML
mariadb_log_file_group: adm
```

### mariadb_lower_case_table_names

#### Default value

```YAML
mariadb_lower_case_table_names: '0'
```

### mariadb_max_allowed_packet

#### Default value

```YAML
mariadb_max_allowed_packet: 64M
```

### mariadb_max_connections

#### Default value

```YAML
mariadb_max_connections: '151'
```

### mariadb_max_heap_table_size

#### Default value

```YAML
mariadb_max_heap_table_size: 16M
```

### mariadb_myisam_sort_buffer_size

#### Default value

```YAML
mariadb_myisam_sort_buffer_size: 64M
```

### mariadb_mysqldump_max_allowed_packet

#### Default value

```YAML
mariadb_mysqldump_max_allowed_packet: 64M
```

### mariadb_overwrite_global_mycnf

Whether my.cnf should be updated on every run.

#### Default value

```YAML
mariadb_overwrite_global_mycnf: true
```

### mariadb_packages

Define a custom list of packages to install. Default value depends on your operating system.

#### Example usage

```YAML
mariadb_packages:
  - mariadb
  - mariadb-server
  - MySQL-python
```

### mariadb_packages_extra

List of extra packages to install e.g. a set of custom dependencies.

#### Default value

```YAML
mariadb_packages_extra: []
```

### mariadb_pid_file

Path to MariaDB PID file. Default value depends on your operating system.

#### Example usage

```YAML
mariadb_pid_file: /var/run/mysqld/mysqld.pid
```

### mariadb_port

#### Default value

```YAML
mariadb_port: '3306'
```

### mariadb_query_cache_limit

#### Default value

```YAML
mariadb_query_cache_limit: 1M
```

### mariadb_query_cache_size

#### Default value

```YAML
mariadb_query_cache_size: 16M
```

### mariadb_query_cache_type

#### Default value

```YAML
mariadb_query_cache_type: '0'
```

### mariadb_read_buffer_size

#### Default value

```YAML
mariadb_read_buffer_size: 1M
```

### mariadb_read_rnd_buffer_size

#### Default value

```YAML
mariadb_read_rnd_buffer_size: 4M
```

### mariadb_root_password

Password for the default MariaDB root user. For security reasons you should change it to some secure in production use!

#### Default value

```YAML
mariadb_root_password: root
```

### mariadb_skip_name_resolve

#### Default value

```YAML
mariadb_skip_name_resolve: false
```

### mariadb_socket

Path to MariaDB unix socket. Default value depends on your operating system.

#### Example usage

```YAML
mariadb_socket: /var/run/mysqld/mysqld.sock
```

### mariadb_sort_buffer_size

#### Default value

```YAML
mariadb_sort_buffer_size: 1M
```

### mariadb_sql_mode

MariaDB supports several different modes. You can pass a list of options to to suit your needs.

#### Default value

```YAML
mariadb_sql_mode: []
```

### mariadb_sync_binlog

#### Default value

```YAML
mariadb_sync_binlog: 1
```

### mariadb_table_open_cache

#### Default value

```YAML
mariadb_table_open_cache: '256'
```

### mariadb_thread_cache_size

#### Default value

```YAML
mariadb_thread_cache_size: '8'
```

### mariadb_tmp_table_size

#### Default value

```YAML
mariadb_tmp_table_size: 16M
```

### mariadb_transaction_isolation_level

Set transaction isolation level. Possible values: `READ-UNCOMMITTED|READ-COMMITTED|REPEATABLE-READ|SERIALIZABLE`

#### Default value

```YAML
mariadb_transaction_isolation_level: READ-COMMITTED
```

### mariadb_users

#### Default value

```YAML
mariadb_users:
  - name: owncloud
    host: localhost
    password: owncloud
    priv: owncloud.*:ALL
```

### mariadb_wait_timeout

#### Default value

```YAML
mariadb_wait_timeout: '28800'
```

## Dependencies

None.
