# Ansible Role: `aisbergg.dnscrypt-proxy`

This is Ansible role installs and configures the DNSCrypt Proxy, a DNS proxy with support for encrypted DNS protocols.

## Requirements

None.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `dnscrypt_proxy_service_state` | `started` | Set the service state (Possible values: started, restarted, stopped) | 
| `dnscrypt_proxy_service_enabled` | `true` | Enable/Disable the DNSCrypt Proxy service | 
| `dnscrypt_proxy_config` | `{}` | Dictionary of DNSCrypt Proxy configuration variables (key-value pairs). See role provides some defaults to work with quad9 (see: [`vars/main.yml`](./vars/main.yml) ). These defaults can be overriden like shown in the [Example Playbook](#example-playbook) section below.<br><br>DNSCrypt Proxy provides an [example configuration](https://raw.githubusercontent.com/DNSCrypt/dnscrypt-proxy/master/dnscrypt-proxy/example-dnscrypt-proxy.toml), which lists all available variables and can be used as a reference. Just make sure to use YAML syntax for the role instead of the TOML syntax shown in the example configuration. |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  vars:
    dnscrypt_proxy_config:
      server_names:
        - "quad9-dnscrypt-ip6-filter-pri"
        - "quad9-dnscrypt-ip6-filter-alt"
        - "quad9-dnscrypt-ip4-filter-pri"
        - "quad9-dnscrypt-ip4-filter-alt"
      fallback_resolvers:
        - "9.9.9.9:53"
        - "8.8.8.8:53"
      netprobe_address: "9.9.9.9:53"

      ignore_system_dns: true
      ipv4_servers: true
      ipv6_servers: true
      dnscrypt_servers: true
      doh_servers: false

      tls_cipher_suite:
        - 52392
        - 49199

      sources:
        quad9-resolvers:
          urls:
            - https://www.quad9.net/quad9-resolvers.md
          cache_file: quad9-resolvers.md
          minisign_key: RWQBphd2+f6eiAqBsvDZEBXBGHQBJfeG6G+wJPPKxCZMoEQYpmoysKUN
          prefix: 'quad9-'

  roles:
    - aisbergg.dnscrypt-proxy
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
