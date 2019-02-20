import ipaddress

def check_ip(ip_address, verbose=False):
    try:
        ipaddress.ip_interface(ip_address)
        print('run')
        print('run2')
        return True
    except ValueError as err:
        if verbose: print(err)
        return False
    data = 'test'


if __name__ == "__main__":
    result = check_ip('10.1.1.1/24')
    print('Function result:', result)
    result = check_ip('10.1.1.1000/24')
    print('Function result:', result)

