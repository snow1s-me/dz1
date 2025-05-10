import random

s = random.randint(1, 10)
p = 3

while p > 0:
    ch = int(input("Вгадайте число від 1 до 10: "))
    if ch == s:
        print("Ви вгадали число!")
        break
    elif ch> s:
        print("Менше")
    else:
        print("Більше")
    p -= 1

if p == 0 and ch != s:
    print("Ви програли!")
