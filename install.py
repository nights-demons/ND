import os
print("Обновление pip...")
os.system("pip3 install --upgrade pip")
os.system("clear")
print("              [Installer]\n")
mod = ["requests", "bs4"]
input("Нажмите Enter, для установки нужных библиотек.")
print("Начало установки.")
for i in range(len(mod)):
    print("Установка "+mod[i]+"...")
    os.system("pip3 install "+mod[i])
