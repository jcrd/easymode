import os
import socket
import sys
from pathlib import PurePath

import yaml
from flask import Flask, render_template

app = Flask(__name__)


def get_hostname():
    name = os.getenv("EASYMODE_HOSTNAME")
    if name:
        return name
    return socket.getfqdn()


def get_ip():
    ip = os.getenv("EASYMODE_IP")
    if ip:
        return ip
    return socket.gethostbyname(get_hostname())


def get_address(url=None):
    ip = get_ip()
    if url:
        ip = "{}:{}".format(ip, url)
    return "http://" + ip


def load_config():
    path = os.getenv("EASYMODE_CONFIG", ".easymode-config")

    config = []
    for f in os.listdir(path):
        if not f.endswith(".yml"):
            continue
        with open(PurePath(path, f), "r") as file:
            try:
                config.append(yaml.safe_load(file))
            except yaml.YAMLError as e:
                print(e, file=sys.stderr)
                sys.exit(2)

    config_keys = ["name", "url", "icon"]

    try:
        for i, s in enumerate(config, start=1):
            for k in config_keys:
                s[k]
            s["url"] = get_address(s["url"])
    except KeyError as e:
        print("[error] service {} is missing key: {}".format(i, e), file=sys.stderr)
        sys.exit(2)

    return config


config = load_config()


@app.route("/")
def index():
    return render_template("index.html", title=get_hostname(), config=config)
