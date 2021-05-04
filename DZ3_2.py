from hashlib import sha256

login = input('Введите Логин\n>>>')

with open(file='task_2.txt', encoding='UTF-8', mode='w+') as txt:
    password = input('Введите пароль\n>>>')
    txt.write(sha256(login.encode() + password.encode()).hexdigest())
    txt.seek(0)
    password = input('Повторите пароль\n>>>')
    txt.seek(0)
    if txt.read() == sha256(login.encode() + password.encode()).hexdigest():
        print('Верно!')
    else:
        print('Неверно!')
