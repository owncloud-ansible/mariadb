# mariadb

[![Build Status](https://drone.owncloud.com/api/badges/owncloud-ansible/mariadb/status.svg)](https://drone.owncloud.com/owncloud-ansible/mariadb)


Ansible role to setup MariaDB server

## Table of content

* [Default Variables](#default-variables)
  * [mariadb_root_password](#mariadb_root_password)
  * [mariadb_enabled_on_startup](#mariadb_enabled_on_startup)
  * [overwrite_global_mycnf](#overwrite_global_mycnf)
  * [mariadb_transaction_isolation_level](#mariadb_transaction_isolation_level)
  * [mariadb_packages_extra](#mariadb_packages_extra)
  * [mariadb_port](#mariadb_port)
  * [mariadb_bind_address](#mariadb_bind_address)
  * [mariadb_skip_name_resolve](#mariadb_skip_name_resolve)
  * [mariadb_sql_mode](#mariadb_sql_mode)
  * [mariadb_key_buffer_size](#mariadb_key_buffer_size)
  * [mariadb_max_allowed_packet](#mariadb_max_allowed_packet)
  * [mariadb_table_open_cache](#mariadb_table_open_cache)
  * [mariadb_sort_buffer_size](#mariadb_sort_buffer_size)
  * [mariadb_read_buffer_size](#mariadb_read_buffer_size)
  * [mariadb_read_rnd_buffer_size](#mariadb_read_rnd_buffer_size)
  * [mariadb_myisam_sort_buffer_size](#mariadb_myisam_sort_buffer_size)
  * [mariadb_thread_cache_size](#mariadb_thread_cache_size)
  * [mariadb_query_cache_type](#mariadb_query_cache_type)
  * [mariadb_query_cache_size](#mariadb_query_cache_size)
  * [mariadb_query_cache_limit](#mariadb_query_cache_limit)
  * [mariadb_max_connections](#mariadb_max_connections)
  * [mariadb_tmp_table_size](#mariadb_tmp_table_size)
  * [mariadb_max_heap_table_size](#mariadb_max_heap_table_size)
  * [mariadb_group_concat_max_len](#mariadb_group_concat_max_len)
  * [mariadb_join_buffer_size](#mariadb_join_buffer_size)
  * [mariadb_lower_case_table_names](#mariadb_lower_case_table_names)
  * [mariadb_wait_timeout](#mariadb_wait_timeout)
  * [mariadb_event_scheduler_state](#mariadb_event_scheduler_state)
  * [mariadb_innodb_file_per_table](#mariadb_innodb_file_per_table)
  * [mariadb_innodb_buffer_pool_size](#mariadb_innodb_buffer_pool_size)
  * [mariadb_innodb_log_file_size](#mariadb_innodb_log_file_size)
  * [mariadb_innodb_log_buffer_size](#mariadb_innodb_log_buffer_size)
  * [mariadb_innodb_flush_method](#mariadb_innodb_flush_method)
  * [mariadb_innodb_flush_log_at_trx_commit](#mariadb_innodb_flush_log_at_trx_commit)
  * [mariadb_innodb_lock_wait_timeout](#mariadb_innodb_lock_wait_timeout)
  * [mariadb_innodb_read_io_threads](#mariadb_innodb_read_io_threads)
  * [mariadb_innodb_write_io_threads](#mariadb_innodb_write_io_threads)
  * [mariadb_innodb_io_capacity](#mariadb_innodb_io_capacity)
  * [mariadb_sync_binlog](#mariadb_sync_binlog)
  * [mariadb_mysqldump_max_allowed_packet](#mariadb_mysqldump_max_allowed_packet)
  * [mariadb_config_include_files](#mariadb_config_include_files)
  * [mariadb_databases](#mariadb_databases)
  * [mariadb_users](#mariadb_users)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### mariadb_root_password

#### Default value

```YAML
mariadb_root_password: root
```

### mariadb_enabled_on_startup

#### Default value

```YAML
mariadb_enabled_on_startup: true
```

### overwrite_global_mycnf

#### Default value

```YAML
overwrite_global_mycnf: true
```

### mariadb_transaction_isolation_level

#### Default value

```YAML
mariadb_transaction_isolation_level: READ-COMMITTED
```

### mariadb_packages_extra

#### Default value

```YAML
mariadb_packages_extra: []
```

### mariadb_port

#### Default value

```YAML
mariadb_port: '3306'
```

### mariadb_bind_address

#### Default value

```YAML
mariadb_bind_address: 127.0.0.0
```

### mariadb_skip_name_resolve

#### Default value

```YAML
mariadb_skip_name_resolve: false
```

### mariadb_sql_mode

#### Default value

```YAML
mariadb_sql_mode: ''
```

### mariadb_key_buffer_size

#### Default value

```YAML
mariadb_key_buffer_size: 256M
```

### mariadb_max_allowed_packet

#### Default value

```YAML
mariadb_max_allowed_packet: 64M
```

### mariadb_table_open_cache

#### Default value

```YAML
mariadb_table_open_cache: '256'
```

### mariadb_sort_buffer_size

#### Default value

```YAML
mariadb_sort_buffer_size: 1M
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

### mariadb_myisam_sort_buffer_size

#### Default value

```YAML
mariadb_myisam_sort_buffer_size: 64M
```

### mariadb_thread_cache_size

#### Default value

```YAML
mariadb_thread_cache_size: '8'
```

### mariadb_query_cache_type

#### Default value

```YAML
mariadb_query_cache_type: '0'
```

### mariadb_query_cache_size

#### Default value

```YAML
mariadb_query_cache_size: 16M
```

### mariadb_query_cache_limit

#### Default value

```YAML
mariadb_query_cache_limit: 1M
```

### mariadb_max_connections

#### Default value

```YAML
mariadb_max_connections: '151'
```

### mariadb_tmp_table_size

#### Default value

```YAML
mariadb_tmp_table_size: 16M
```

### mariadb_max_heap_table_size

#### Default value

```YAML
mariadb_max_heap_table_size: 16M
```

### mariadb_group_concat_max_len

#### Default value

```YAML
mariadb_group_concat_max_len: '1024'
```

### mariadb_join_buffer_size

#### Default value

```YAML
mariadb_join_buffer_size: '262144'
```

### mariadb_lower_case_table_names

#### Default value

```YAML
mariadb_lower_case_table_names: '0'
```

### mariadb_wait_timeout

#### Default value

```YAML
mariadb_wait_timeout: '28800'
```

### mariadb_event_scheduler_state

#### Default value

```YAML
mariadb_event_scheduler_state: OFF
```

### mariadb_innodb_file_per_table

#### Default value

```YAML
mariadb_innodb_file_per_table: '1'
```

### mariadb_innodb_buffer_pool_size

#### Default value

```YAML
mariadb_innodb_buffer_pool_size: 256M
```

### mariadb_innodb_log_file_size

#### Default value

```YAML
mariadb_innodb_log_file_size: 128M
```

### mariadb_innodb_log_buffer_size

#### Default value

```YAML
mariadb_innodb_log_buffer_size: 8M
```

### mariadb_innodb_flush_method

#### Default value

```YAML
mariadb_innodb_flush_method: O_DIRECT
```

### mariadb_innodb_flush_log_at_trx_commit

#### Default value

```YAML
mariadb_innodb_flush_log_at_trx_commit: '1'
```

### mariadb_innodb_lock_wait_timeout

#### Default value

```YAML
mariadb_innodb_lock_wait_timeout: '50'
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

### mariadb_innodb_io_capacity

#### Default value

```YAML
mariadb_innodb_io_capacity: 200
```

### mariadb_sync_binlog

#### Default value

```YAML
mariadb_sync_binlog: 1
```

### mariadb_mysqldump_max_allowed_packet

#### Default value

```YAML
mariadb_mysqldump_max_allowed_packet: 64M
```

### mariadb_config_include_files

#### Default value

```YAML
mariadb_config_include_files: []
```

### mariadb_databases

#### Default value

```YAML
mariadb_databases:
  - name: owncloud
    collation: utf8_general_ci
    encoding: utf8
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

## Dependencies

None.

## License

Apache-2.0

## Author

Robert Kaussow
