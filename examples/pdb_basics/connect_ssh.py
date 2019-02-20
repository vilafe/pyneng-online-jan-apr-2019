#!/usr/bin/env python
from netmiko import ConnectHandler

device = {
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}

ssh = ConnectHandler(**device)
import IPython; IPython.embed()

output = ssh.send_command("sh ip int br")
for line in output.splitlines():
    print(line)

ssh.disconnect()
