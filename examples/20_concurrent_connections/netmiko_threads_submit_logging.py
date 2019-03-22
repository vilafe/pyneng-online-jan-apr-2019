from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pprint import pprint
import time
from itertools import repeat
import threading
import logging


import yaml
from netmiko import ConnectHandler


# отключаем логи paramiko:
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO
)


start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


def connect_ssh(device_dict, command):
    #logging.info(f'Thread: {threading.current_thread()} running... Device: {device_dict["ip"]}')
    logging.info(start_msg.format(datetime.now().time(), device_dict['ip']))
    if device_dict['ip'] == '192.168.100.1':
        time.sleep(10)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(received_msg.format(datetime.now().time(), device_dict['ip']))
    return {device_dict['ip']: result}


def threads_conn(function, devices, limit=2, command=''):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [
            executor.submit(function, device, command) for device in devices
        ]
        for f in as_completed(future_ssh):
            all_results.append(f.result())
    return all_results


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.load(f, Loader=yaml.FullLoader)
    all_done = threads_conn(
        connect_ssh, devices['routers'], command='sh clock')
    pprint(all_done)
