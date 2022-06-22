# easymode

easymode is a super easy to use home server landing page.

It is designed to be configured by automation systems such as [Ansible][ansible].

[ansible]: https://www.ansible.com/

## Screenshot

[<img src="https://github.com/jcrd/easymode/blob/assets/screenshot.png" width="300"/>][scrn]

[scrn]: https://github.com/jcrd/easymode/blob/assets/screenshot.png

## Usage

easymode is *easiest* to use via docker or podman.

Pull its image from: `docker.io/supplantr/easymode`.

It expects:

- the environment variable `EASYMODE_HOSTNAME` to be the server's hostname
- the environment variable `EASYMODE_IP` to be the server's IP address
- configuration files to be found in `/config`

### Configuration

easymode looks for YAML (`.yml`) configuration files in the path pointed to by
`EASYMODE_CONFIG`, which is set to `/config` in the above image.

Config files must contain these top-level keys:

- `name`: name of the service
- `url`: service URL starting with port (will be appended to the server's IP address)
- `icon`: name of icon from [material design icons][mdi]

[mdi]: https://materialdesignicons.com/

Example `plex.yml`:

```yml
name: plex
url: 32400/web
icon: live_tv
```

### Example

Create a container with an Ansible task:

```yml
- name: Create container
  command: >
    podman create --name=easymode
    -p 80:80
    -e EASYMODE_HOSTNAME={{ ansible_hostname }}
    -e EASYMODE_IP={{ hostip }}
    -v {{ easymodeconfig }}:/config:z
    docker.io/supplantr/easymode
```

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)).
