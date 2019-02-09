from check_ip_functions import check_ip


def test_check_ip():
    assert check_ip('10.1.1.1/24') == True, 'При правильном IP, функция должна возвращать True'
    assert check_ip('10.1.1.1/45') == False, 'Если маска неправильная, функция должна возвращать False'
    assert check_ip('500.1.1.1/24') == False, 'Если адрес неправильный, функция должна возвращать False'


