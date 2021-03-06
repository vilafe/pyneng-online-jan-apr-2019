import sw_int_templates as sw_temp
from sw_data import sw1_fast_int


def generate_access_cfg(sw_dict):
    result = []
    for intf, vlan in sw_dict['access'].items():
        result.append('interface FastEthernet' + intf)
        for command in sw_temp.access_template:
            if command.endswith('access vlan'):
                result.append(' {} {}'.format(command, vlan))
            else:
                result.append(' {}'.format(command))
    return result

##version 1
if __name__ == "__main__":
    print('\n'.join(generate_access_cfg(sw1_fast_int)))
    print(sw_temp.read_file_content('test_script.py'))


##version 2
def main():
    print('\n'.join(generate_access_cfg(sw1_fast_int)))
    print(sw_temp.read_file_content('test_script.py'))

if __name__ == "__main__":
    main()

