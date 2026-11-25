time_hour = 8
mood = 'sleepy'

if time_hour >= 0 and time_hour <= 24:
    print('Suggesting a drink option...')
    if mood == 'sleepy' and time_hour < 10:
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
        print('lemonade')
    else:
        print('water')
