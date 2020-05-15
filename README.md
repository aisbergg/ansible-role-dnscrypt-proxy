# Ansible Role: `aisbergg.dnscrypt-proxy`

This is Ansible role installs and configures the DNSCrypt Proxy, a DNS proxy with support for encrypted DNS protocols.

## Requirements

None.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `dnscrypt_proxy_service_state` | `started` | Set the service state (Possible values: started, restarted, stopped) | 
| `dnscrypt_proxy_service_enabled` | `true` | Enable/Disable the DNSCrypt Proxy service | 
| `dnscrypt_proxy_config` | `{}` | Dictionary (key-value pairs) of DNSCrypt Proxy configuration options. The role provides some sane defaults and is configured to work with quad9 (see: [`vars/main.yml`](./vars/main.yml)).</br></br>A list of all available options can be found in the [example configuration](https://raw.githubusercontent.com/DNSCrypt/dnscrypt-proxy/master/dnscrypt-proxy/example-dnscrypt-proxy.toml). Just make sure to use YAML syntax instead of the TOML. |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  vars:
    dnscrypt_proxy_config:
      sources:
        quad9-resolvers:
          urls:
            - https://www.quad9.net/quad9-resolvers.md
          cache_file: quad9-resolvers.md
          minisign_key: RWQBphd2+f6eiAqBsvDZEBXBGHQBJfeG6G+wJPPKxCZMoEQYpmoysKUN
          prefix: 'quad9-'

      dnscrypt_servers: true
      doh_servers: true
      require_dnssec: false
      require_nolog: true
      require_nofilter: true

      cache: true
      cache_size: 4096
      cache_min_ttl: 2400
      cache_max_ttl: 86400

  roles:
    - aisbergg.dnscrypt-proxy
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
