import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"


#

def get_climate_tip():
    import random
    # Создаем список советов
    tips = [
        "Переходите на светодиодное освещение - это экономит до 85% энергии",
        "Используйте общественный транспорт или велосипед вместо личного автомобиля",
        "Установите солнечные панели на крыше вашего дома",
        "Сократите потребление мяса - животноводство является одним из главных источников выбросов",
        "Покупайте продукты с минимальной упаковкой",
        "Переходите на возобновляемые источники энергии",
        "Сажайте деревья - одно дерево поглощает около 20 кг CO2 в год",
        "Используйте энергосберегающие приборы",
        "Отключайте электроприборы от сети, когда они не используются",
        "Выбирайте продукты местного производства",
        "Используйте многоразовые сумки вместо одноразовых",
        "Экономьте воду - производство и очистка воды требуют много энергии",
        "Перерабатывайте отходы правильно",
        "Используйте энергоэффективные окна",
        "Установите программу для умного управления отоплением",
        "Выбирайте товары с минимальным углеродным следом",
        "Поддерживайте компании, которые заботятся об экологии",
        "Используйте экологичную косметику и бытовую химию",
        "Участвуйте в местных экологических инициативах",
        "Выбирайте одежду из экологичных материалов",
        "Используйте энергосберегающие режимы на компьютере и телефоне",
        "Поддерживайте возобновляемые источники энергии",
        "Сократите использование одноразовых пластиковых изделий",
        "Используйте экологичные средства передвижения",
        "Поддерживайте экологическое образование и просвещение"
    ]
    
    # Выбираем случайный совет
    return random.choice(tips)















    