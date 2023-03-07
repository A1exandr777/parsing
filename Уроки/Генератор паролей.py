import random

password = []
simvols = []
print("Это генератор паролей")
print("Введите количетсво символов из которых должен состоять пароль:")
dlina = int(input())

for i in range(65, 90):
    simvols.append(chr(i))
for i in range(97, 122):
    simvols.append(chr(i))
for i in range(48, 57):
    simvols.append(chr(i))
simvols.append(chr(33))
simvols.append(chr(35))
simvols.append(chr(64))
simvols.append(chr(63))
simvols.append(chr(38))
for i in range(dlina):
    password.append(simvols[random.randint(0, len(list(simvols)))])

print("Ваш пароль готов!")
print("".join(password))