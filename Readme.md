# Manual steps

If the ECS (https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) field definition and boards supplied by Elastic are to be used, the following manual steps must be carried out:

Configure an suitable elastic user and enable template / dashboard setup:

```yaml
setup:
  dashboards:
    enabled: true
  template:
    enabled: true
  kibana:
    host: "https://kibana-host:443"
    username: "<user>"
    password: "<password>"
```

then stop the service and run the setup: 

```bash
metricbeat setup -e
```

In order to prevent metricbeat to override templates and boards on every startup (takes several minutes), disable template / dashboard setup again.
