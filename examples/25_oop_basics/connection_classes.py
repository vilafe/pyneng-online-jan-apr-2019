from netmiko import ConnectHandler


class CiscoIosSSH:
    def __init__(self, user, password, enable, ip_address):
        self.username = user
        self.host = ip_address
        self.ssh = ConnectHandler(username=user, password=password,
                                  secret=enable, ip=ip_address,
                                  device_type='cisco_ios')
        self.ssh.enable()

    def get_config(self):
        if self.ssh.is_alive():
            config = self.ssh.send_command('sh run')
            return config
        else:
            raise ValueError('Сессия закрыта')


if __name__ == "__main__":
    r1 = CiscoIosSSH('cisco', 'cisco', 'cisco', '192.168.100.1')
    print(r1.get_config())
