name = input('Привет, как тебя зовут?: ')
answer = input('Любишь играть в майнкрафт?: ')

if answer == 'да' or answer == 'конечно':
    two_answer = input('Спросим у папы, можно ли поиграть?: ')
    if two_answer == 'да':
        papa_answer = input('Папа, можно поиграть?: ')
        if papa_answer == 'нет':
            print('Извини, ' + name + ', папа не разрешает!')
        else:
            print('Ура! Стоп! Но ведь 7 дней еще не прошло... Запрет на игры еще действует. Извини, но нельзя!')
    else:
        print('Ну, тогда давай просто поиграй в динозавры!')
else:
    print('Что? Я тебе не верю, ' + name + '!!!! Ты - обманщик!!!')
