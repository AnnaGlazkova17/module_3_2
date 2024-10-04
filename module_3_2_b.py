def send_email(message, recipient, sender='university.help@gmail.com'):
    ok = False # задаю флаг
    if sender != recipient: # проверка что почты не совпадают
        recipient_1 = list(recipient) # преобразую строку адрес в список
        if '@' in recipient_1: # проверяю есть ли в списке @
                if recipient[-4::1] == '.com' or recipient[-3::1] == '.ru' or recipient[-4::1] == '.net': # проверяем окончание
                    ok = True # меняем значение флага, нужно для 12, 21 и 23 строк
                else:
                    print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}") # сообщение есть неверное окончание
        elif ok == False: # для вывода сообщения если не нашли @ и ok не сменился на True
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        if sender != 'university.help@gmail.com' and ok == True: # аналогично для почты отправителя, если она нестандартная
            sender_1 = list(sender) # преобразую строку адрес в список
            if '@' in sender_1: # проверяю есть ли в списке @
                    if sender[-4::1] == '.com' or sender[-3::1] == '.ru' or sender[-4::1] == '.net':
                        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
                        ok = False # смена знаяения флага, чтобы не сработала 21 строка
                    else:
                        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                        ok = False # смена знаяения флага, чтобы не сработала 21 строка
            elif ok == True:
                    print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        elif sender == 'university.help@gmail.com' and ok == True:
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else: # вывод в случае, когда почты одинаковые
        print('Нельзя отправить письмо самому себе!')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')