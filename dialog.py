import time
from snake import snake

def dialog_10():

    print('\n- У нас множество видов и сортов, чаи все хорошие, завезенные из Малайзии. У нас есть и \n'
          'множество сортов на любой размер кошелька.\n')

    time.sleep(3)
    print('Сидя на неудобной подушке, я рассуждал, сколько людей сидели на этом же месте и пили эту отраву. \n'
          'Серьёзно, ведь это было похоже на заваренный чай в холодной воде, который потом чуть подогрели в \n'
          'микроволновке. Мне не рассказали ни про сорта, ни про цены, поэтому я сидел в напряжении, боясь, \n'
          'что я могу оставить здесь все заработанные деньги на стройке. \n'
          'Полностью согревшись, я решил, что надо сваливать, подошел к администратору и спросил сколько я им должен. \n')
    time.sleep(3)
    print( '- Вы пили цветочный чай Tienchi , который собирали в Китае. К оплате 1750 рублей. \n')
    time.sleep(3)
    print('- А он разве не из Малайзии? - Выпучив глаза и посмотрев на малюсенькую чашку, \n'
          'что стояла около подушки. \n')
    time.sleep(3)
    print('- Производится в Малайзии, собирается в Китае, пакетируется в России. \n')

    time.sleep(3)
    print('Тут ты понял, что выход здесь один - бежать.\n')

# def dialog_1():
    # b = input('Находясь в своих мыслях я даже и не заметил, как наткнулся на красивую \n'
    #           'девушку, которая стояла на улице, зазывая всех подряд на чайную церемонию. \n'
    #           '- Молодой человек, скажите, пожалуйста, вы любите чай. Хотите попробовать нашего традиционного? \n'
    #           '1. На улице слишком холодно, чтобы отказываться от чая, он не должен стоить очень дорого. \n'
    #           '2. Я пью только водку, особенно в такую погоду! \n\nОТВЕТ: ')
    #
    # if '1' in b:
    #     dialog_10()
    #     snake()
    # if '2' in b:
    #     print('Зная про этих ребят на Невском, которые заманивают \n'
    #           'к себе под предлогом чая, а потом вымогают деньги, ты быстро побежал!')
    #     snake()
    #
    # print('После интенсивной пробежки, передо мной возникло небольшое двухэтажное здание, \n'
    #       'которое светилось со всех сторон, а над входом находилась вывеска «brothers».\n')





# def dialog_2():
#
#     time.sleep(3)
#     print('Это лучше, чем быть пойманным полицией, и пойти отрабатывать 120 часов, оставшись \n'
#           'в этом городе на энное количество суток. \n'
#           'Перед входом стоял ухоженный мужчина крепкого телосложения. \n')
#
#     time.sleep(3)
#     print('- Куда вам? – грозно сказал он. \n '
#           '- Туда! – чуть ли не ткнул пальцем я в его грудь, что закрывала проход внутрь \n')




def dialog_3():

    # print('После интенсивной пробежки, передо мной возникло небольшое двухэтажное здание, \n'
    #       'которое светилось со всех сторон, а над входом находилась вывеска «brothers».\n')

    time.sleep(3)
    print('Это лучше, чем быть пойманным полицией, и пойти отрабатывать 120 часов, оставшись \n'
          'в этом городе на энное количество суток. \n'
          'Перед входом стоял ухоженный мужчина крепкого телосложения. \n')

    time.sleep(3)
    print('- Куда вам? – грозно сказал он \n'
          '\n- Туда! – чуть ли не ткнул пальцем я в его грудь, что закрывала проход внутрь \n')

    time.sleep(3)
    print('- Пароль! \n')
    b = input('ОТВЕТ: ')

    while b != 'пароль':
        print('\nНЕПРАВИЛЬНЫЙ ПАРОЛЬ\n')
        b = input("ОТВЕТ: ")

    time.sleep(2)
    print('\n- Проходите \n')

    time.sleep(3)
    print('Зайдя внутрь я увидел только представителей \n'
          'мужского пола и тогда пазл соединился воедино. \n')

    time.sleep(3)
    print('- Добрый вечер! Я на собеседование. \n')

    time.sleep(3)
    print('- Добрый! Меня зовут Андрей, как я могу к вам обращаться? \n'
          ' Мы разве с вами договаривались на эту дату? \n')

    e = input("ОТВЕТ: ")

    time.sleep(3)
    print('\n- Ну,' + e + ', раз вы у нас уже на опыте, можете идти переодеваться, \n'
          'комната персонала там, костюм тоже. – Андрей ткнул пальцем за мою спину. \n')

    time.sleep(3)
    print('- Во что переодеваться? – спросил я, глупо поморгав. \n')

    time.sleep(3)
    print('- У вас сегодня здесь выступление, гонорар 30 000 за вечернюю программу, \n'
          'мы ведь с вами все обсудили – нахмурившись сказал администратор. \n')

    time.sleep(3)
    print('Округлив глаза, я понял, что мне надо делать и что я смогу уехать домой, \n'
          'не плацкартом, голодая два дня, а на сапсане за три часа. \n')
    d = input('1. Согласиться. \n'
          '2. Отказаться. \n\n'
              'ОТВЕТ: ')
    if '1' in d:
        print('\nПоздравляю! Вы прошли игру, и ваш персонаж добрался до дома за шесть часов, сытый и невредимый. \n')

    if '2' in d:
        print('\nПоздравляю! Вы прошли игру, и ваш персонаж добрался до дома за два дня, \n'
              'где его встретили друзья с едой, чтобы он не упал в обморок. \n')


def rules():
    print('_______________________________________________________________________________________________\n'
          'ПРАВИЛА ИГРЫ\n'
          '-----------------------------------------------------------------------------------------------'
        '\nГлавное правило - дойти до конца и помочь главному герою добраться домой,\n'
          '1. Внимательно следите за ходом игры, чтобы не пропустить ничего важного,\n'
'2. Делайте выбор с умом, потому что каждое ваше решение, может изменить ход игры,'
'\n3. Если вам не понравится исход игры, вы всегда можете перепройти и изменить конец истории,'
'\n4. Отвечайте на вопросы вводом цифры, которой соответствует ваш ответ,'
'\n5. Чтобы начать игру BALL нажмите Enter, управляйте стрелками,'
'\n6. Чтобы начать игру SNAKE начните управление стрелками.')

def answer_1():
    a = input('\n\n- Хей, парень не хочешь заработать многа денег?\n'
              ' У меня есть мой брат, он хочет многа работников, \n'
              'чтобы платить им многа деняг.\n \n'

              '1. Разве у меня есть выбор?\n'
              '2. Я не доверяю этому пареньку...\n\nОТВЕТ: ')
    if '2' in a:
          print('\nПосле того, как я час простоял в холодном Питере в кроссовках \n'
                'и легкой ветровке, в моем кармане так и не набралось даже на шаверму. \n'
                'Я решил, что находиться здесь бессмысленно и надо бы найти другое решение \n'
                'этой проблемы. Невский проспект, конечно, прекрасен, много интересных людей, \n'
                'которые идут по своим делам, прекрасная архитектура, живая музыка…\n')
    elif '1' in a:
          score,paddle,ball = ball()
          balance = score.score