a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = input("Введіть дію (+, -, *, /): ")

if c == '+':
    print(f"Результат: {a + b}")
elif c == '-':
    print(f"Результат: {a - b}")
elif c == '*':
    print(f"Результат: {a * b}")
elif c == '/':
    print(f"Результат: {a / b}")
