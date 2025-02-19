def get_sum(a, b): return a + b
def get_difference(a, b): return a - b
def get_product(a, b): return a * b
def get_quotient(a, b): return "На нуль ділити не можна!" if b == 0 else a / b
def get_remainder(a, b): return a % b
def get_exponentiation(a, b): return a ** b

def perform_operation(a, b, operation):
    operations = {
        '+': get_sum,
        '-': get_difference,
        '*': get_product,
        '/': get_quotient,
        '%': get_remainder,
        '^': get_exponentiation
    }
    
    if operation in operations:
        return operations[operation](a, b)
    else:
        return "Невірна операція!"

def main():
    try:
        num1 = float(input('Введіть перше число: '))
        operation = input('Введіть дію +, -, *, /, %, ^: ')
        num2 = float(input('Введіть друге число або до якого степеня потрібно піднести перше число: '))

        result = perform_operation(num1, num2, operation)
        print(f'Результат: {result}')
    
    except ValueError:
        print("Будь ласка, введіть коректне число.")

if __name__ == "__main__":
    main()
