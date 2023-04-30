a = int(input('[ შეიყვანეთ პრიველი რიცხვი ] '))
b = int(input('[ შეიყვანეთ მეორე რიცხვი ] '))
while b > 0:
    c = a % b
    a = b
    b = c
print(a)
    
