# Ansible Role: `aisbergg.dnscrypt-proxy`

This is Ansible role installs and configures the DNSCrypt Proxy, a DNS proxy with support for encrypted DNS protocols.

## Requirements

None.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `dnscrypt_proxy_service_state` | `started` | Set the service state (Possible values: started, restarted, stopped) | 
| `dnscrypt_proxy_service_enabled` | `true` | Enable/Disable the DNSCrypt Proxy service | 
| `dnscrypt_proxy_config` | `{}` | Dictionary of DNSCrypt Proxy configuration variables (key-value pairs). DNSCrypt Proxy provides an [example configuration](https://raw.githubusercontent.com/DNSCrypt/dnscrypt-proxy/master/dnscrypt-proxy/example-dnscrypt-proxy.toml), which lists all available variables. Use the example configuration as a reference, but make sure, you specify the values as YAML in this role instead of TOML (see example usage below). |

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
      ignore_system_dns: true
      netprobe_address: "9.9.9.9:53"

  roles:
    - aisbergg.dnscrypt-proxy
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
