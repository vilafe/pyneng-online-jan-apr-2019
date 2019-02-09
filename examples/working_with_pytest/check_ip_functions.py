import ipaddress
import time


def check_ip(ip_address):
    try:
        ipaddress.ip_interface(ip_address)
        return True
    except ValueError as err:
        return False


def return_correct_ip(ip_addresses):
    correct = []
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
    return correct


if __name__ == "__main__":
    result = check_ip('10.1.1.1/24')
    time.sleep(5)
    print('Function result:', result)
