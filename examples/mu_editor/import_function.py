from check_ip_function import check_ip


def return_correct_ip(ip_addresses):
    correct = []
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
    return correct

if __name__ == "__main__":
    ip_list = ['10.11.1.1/24', '8.8.8.8/32', 'a.a.a.a']
    correct_ip = return_correct_ip(ip_list)
    print(correct_ip)
