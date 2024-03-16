from numb3rs import validate
import random


def test_validate():
    for _ in range(99099):
        number1 = random.randint(0, 255)
        number2 = random.randint(0, 255)
        number3 = random.randint(0, 255)
        number4 = random.randint(0, 255)
        assert validate(f"{number1}.{number2}.{number3}.{number4}") == True


def test_validate_wrong_input():
    wrong_dot_ips = ['255..255.255.255', '255.255..255.255', '255.255.255.', '.255.255.255.255']
    letter_ips = ['255.255.255.2A5', '255.255.25B.255', '255.25C.255.255', '25D.255.255.255']
    special_char_ips = ['255.255.255.2#5', '255.255.25@.255', '255.25$.255.255', '25%.255.255.255']
    too_many_dot_ips = ['255.255.255.255.255', '255.255.255.255.', '255..255.255.255.255', '...255.255.255.255']
    less_octets_ips = ['255.255.255', '255.255.', '255.', '']
    more_octets_ips = ['255.255.255.255.255', '255.255.255.255.255.255', '255.255.255.255.255.255.255']
    exceed_ips = ['255.255.255.256', '255.255.260.255', '255.270.255.255', '280.255.255.255']
    
    ip_addresses = wrong_dot_ips + letter_ips + special_char_ips + too_many_dot_ips + less_octets_ips + more_octets_ips + exceed_ips
    
    for ip in ip_addresses:
        assert validate(ip) == False
