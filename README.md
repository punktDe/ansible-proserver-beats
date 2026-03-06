<!-- BEGIN_ANSIBLE_DOCS -->
<!--
Do not edit README.md directly!

This file is generated automatically by aar-doc and will be overwritten.

Please edit meta/argument_specs.yml instead.
-->
# ansible-proserver-beats

beats role for Proserver

## Supported Operating Systems

- Debian 12, 13
- Ubuntu 24.04, 22.04
- FreeBSD [Proserver](https://infrastructure.punkt.de/de/produkte/proserver.html)

## Role Arguments



#### Options for `beats`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `remove_legacy_repository` | Whether to remove the legacy elastic repository. | bool | no | True |
| `version` | The major version of beats to install. | int | no | 8 |
| `repository` | Repository configuration for installing beats. | dict of 'repository' options | no |  |

#### Options for `beats.repository`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `apt` |  | dict | no |  |

#### Options for `metricbeat`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `enabled` | Whether to enable and install Metricbeat. | bool | no | False |
| `prefix` | Path prefixes for Metricbeat. | dict | no |  |
| `config` | Metricbeat specific configuration. | dict | no |  |

#### Options for `filebeat`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `enabled` | Whether to enable and install Filebeat. | bool | no | False |
| `prefix` | Path prefixes for Filebeat. | dict | no |  |
| `config` | Filebeat specific configuration. | dict | no |  |

## Dependencies
None.

## Installation
Add this role to the requirements.yml of your playbook as follows:
```yaml
roles:
  - name: ansible-proserver-beats
    src: https://github.com/punktDe/ansible-proserver-beats
```

Afterwards, install the role by running `ansible-galaxy install -r requirements.yml`

## Example Playbook

```yaml
- hosts: all
  roles:
    - name: beats
```

<!-- END_ANSIBLE_DOCS -->
