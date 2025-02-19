import random

symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=')

def random_lower_letter(): return chr(random.randint(ord('a'), ord('z')))
def random_upper_letter(): return chr(random.randint(ord('A'), ord('Z')))
def random_number(): return str(random.randint(0, 9))
def random_symbol(): return random.choice(symbols)

def generate_password(length):
    methods = [random_lower_letter, random_upper_letter, random_number, random_symbol]
    return ''.join(random.choice(methods)() for _ in range(length))

while True:
    password_length = input('Введіть довжину пароля (6-32), або "STOP" для завершення: ')
    if password_length.lower() == 'stop': break
    if password_length.isdigit() and 6 <= int(password_length) <= 32:
        print(f'Згенерований пароль: {generate_password(int(password_length))}')
    else:
        print('Введіть коректну довжину пароля від 6 до 32.')
