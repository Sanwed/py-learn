def check_domain(domain, acceptable_domains):
    for i in acceptable_domains:
        if domain == i:
            return True
    return False


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if ('@' not in sender) or ('@' not in recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    domains = ['com', 'ru', 'net']
    sender_domain = sender.split('.')[-1]
    recipient_domain = recipient.split('.')[-1]
    is_correct_domain = (
            check_domain(sender_domain, domains)
            and check_domain(recipient_domain, domains)
    )
    if not is_correct_domain:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return

    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
