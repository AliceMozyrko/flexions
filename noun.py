def detect_ending():
    cases = {
        "називний": ["а", "я"],
        "родовий": ["и", "і", "ї"],
        "давальний": ["і", "ї"],
        "знахідний": ["у", "ю"],
        "орудний": ["ою", "ею", "єю"],
        "місцевий": ["і", "ї"],
        "кличний": ["о", "е", "є"]
    }

    cases_plural = {
        "називний": ["и", "і"],
        "родовий": ["ь", "б", "в", "г", "ґ", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц",
                    "ч", "ш", "щ"],
        "давальний": ["ам"],
        "знахідний": ["и", "і"],
        "орудний": ["ами"],
        "місцевий": ["ах"],
        "кличний": ["и", "і"]
    }

    # Перевірка називного відмінка
    while True:
        isPlural = False
        noun = input("Введіть іменник 1 відміни у називному відмінку: ").strip().lower()

        for ending in cases["називний"]:
            if noun.endswith(ending):
                print(f"Іменник \"{noun}\" у називному відмінку ОДНИНИ закінчується на \"{ending}\".")
                break
        else:


            #  check if isPlural
            for ending in cases_plural["називний"]:
                if noun.endswith(ending):
                    print(f"Іменник \"{noun}\" у називному відмінку МНОЖИНИ закінчується на \"{ending}\".")
                    isPlural = True
                    break
            if not isPlural:
                print("Введений іменник не 1 відміни або не у називному відмінку. Спробуйте ще раз.")
                continue
        break

    # Перевірка у будь-якому іншому відмінку
    noun = input("Введіть цей же іменник у будь-якому іншому відмінку: ").strip().lower()

    #   isPlural block
    if isPlural:
        return find_best_ending(noun, cases_plural)

    # Перевірка закінчень для орудного відмінка
    if noun.endswith(("ею", "ою", "єю")):
        for ending in cases["орудний"]:
            if noun.endswith(ending):
                return noun, "орудний", ending, isPlural  # Повертаємо фактичне закінчення

    # Перевірка для знахідного відмінка
    elif noun.endswith("ю"):
        return noun, "знахідний", "ю", isPlural

    # Перевірка для випадків з "і" або "ї"
    elif noun.endswith(("і", "ї")):
        return noun, "можливі: родовий, давальний, місцевий", noun[-1], isPlural

    # Інші перевірки для решти відмінків
    else:
        for case, endings in cases.items():
            for ending in endings:
                if noun.endswith(ending):
                    return noun, case, ending, isPlural



    # Якщо закінчення не знайдено
    return noun, "невідомий відмінок", None, isPlural


def find_best_ending(noun, cases_plural):
    best_match = None
    best_ending = ""

    # Перебираємо всі відмінки та їхні закінчення
    for case, endings in cases_plural.items():
        for ending in endings:
            # Якщо слово закінчується на поточне закінчення

            if noun.endswith(ending):
                # Перевіряємо, чи це закінчення довше за попереднє знайдене
                if len(ending) > len(best_ending):
                    best_ending = ending
                    best_match = case
    if best_ending in ["и", "і"]:
        best_match = "можливі: називний, знахідний, кличний"
    if best_match == 'родовий':
        best_ending = "-0"
    # Повертаємо слово, відмінок і найбільше закінчення

    return noun, best_match, best_ending, True

# Основний цикл програми
while True:
    # Викликаємо функцію
    noun, case, ending, isPlural = detect_ending()

    # Виводимо результат
    if case != "невідомий відмінок":
        if case == "можливі: родовий, давальний, місцевий":
            print(f"Іменник \"{noun}\" може бути у родовому, давальному або місцевому відмінку, закінчення:-{ending}.")
        if case == "можливі: називний, знахідний, кличний":
            print(f"Іменник \"{noun}\" у може бути у називному, знахідному, кличному відмінку МНОЖИНИ!!! закінчення: -{ending}.")

        else:
            print(f"Іменник \"{noun}\" {'МНОЖИНИ' if isPlural else 'однини'} у відмінку \"{case}\" закінчення: -{ending}.")

        # Запитуємо, чи хоче користувач визначити інше слово
        repeat = input("Бажаєте визначити інші закінчення? (так/ні): ").strip().lower()
        if repeat != "так":
            print("Дякуємо за користування!")
            break
    else:
        print(f"Не вдалося визначити відмінок для іменника \"{noun}\". Спробуйте ще раз.")