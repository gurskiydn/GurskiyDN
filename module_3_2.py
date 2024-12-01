def send_email(message, recipient,*, sender="university.help@gmail.com"):
    def prov_email(email): #функция на корректный емайл
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if not prov_email(sender) or not prov_email(recipient): #Если один из адресов не корректен, то выводится сообщение
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient: #проверка на свой адрес
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com": #проверка на отправителя
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email("привет", "dmnic73@ya.ru")
send_email("вроде все верно", "sashaLudimov@assa.leg")
send_email("университет", "university.help@gmail.com")
