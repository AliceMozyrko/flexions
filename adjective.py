def detect_ending():
    cases_sing_m = {
        "називний": ["ий", "ій"],
        "родовий": ["ого"],
        "давальний": ["ому"],
        "знахідний": ["ий", "ій", "ого"],
        "орудний": ["им", "ім"],
        "місцевий": ["ому", "ім"],
        "кличний": ["ий", "ій"]
    }

    cases_sing_f = {
        "називний": ["а", "я"],
        "родовий": ["ої"],
        "давальний": ["ій"],
        "знахідний": ["у", "ю"],
        "орудний": ["ою"],
        "місцевий": ["ій"],
        "кличний": ["а", "я"]
    }

    cases_sing_n = {
        "називний": ["е", "є"],
        "родовий": ["ого"],
        "давальний": ["ому"],
        "знахідний": ["е", "є", "ого"],
        "орудний": ["им", "ім"],
        "місцевий": ["ому", "ім"],
        "кличний": ["е", "є"]
    }

    cases_plural = {
        "називний": ["і"],
        "родовий": ["их", "іх"],
        "давальний": ["им", "ім"],
        "знахідний": ["их", "іх", "і"],
        "орудний": ["ими", "іми"],
        "місцевий": ["их", "іх"],
        "кличний": ["і"]
    }

    while True:
        isMale = False
        isFemale = False
        isNeuthral = False
        isPlural = False
        noun = input("Введіть прикметник у називному відмінку: ").strip().lower()

        for ending in cases_sing_m["називний"]:
            if noun.endswith(ending):
                print(f"Прикметник \"{noun}\" у називному відмінку чоловічого роду, закінчується на \"{ending}\".")
                isMale = True
                break
        for ending in cases_sing_f["називний"]:
            if noun.endswith(ending):
                print(f"Прикметник \"{noun}\" у називному відмінку жіночого роду, закінчується на \"{ending}\".")
                isFemale = True
                break
        for ending in cases_sing_n["називний"]:
            if noun.endswith(ending):
                print(f"Прикметник \"{noun}\" у називному відмінку середнього роду, закінчується на \"{ending}\".")
                isNeuthral = True
                break
        for ending in cases_plural["називний"]:
            if noun.endswith(ending):
                print(f"Прикметник \"{noun}\" у називному відмінку МНОЖИНИ закінчується на \"{ending}\".")
                isPlural = True
                break
        if not isPlural and not isMale and not isFemale and not isNeuthral:
            print("Введений прикметник не чоловічого, жіночого, середнього родів, або не множини. Спробуйте ще раз.")
            continue
        break

    noun = input("Введіть цей же прикметник у будь-якому іншому відмінку: ").strip().lower()

    return  find_best_ending(noun, cases_sing_m, cases_sing_f, cases_sing_n, cases_plural, isMale, isFemale, isNeuthral, isPlural)



def find_best_ending(noun, cases_sing_m, cases_sing_f, cases_sing_n, cases_plural, isMale, isFemale, isNeuthral,
                     isPlural):
    best_matches = []  
    best_ending = ""

    if isMale:
        relevant_cases = {"чоловічого роду": cases_sing_m}
    elif isFemale:
        relevant_cases = {"жіночого роду": cases_sing_f}
    elif isNeuthral:
        relevant_cases = {"середнього роду": cases_sing_n}
    elif isPlural:
        relevant_cases = {"множини": cases_plural}
    else:
        return noun, "Невідомий рід або множина", None, False

    for gender, cases in relevant_cases.items():
        for case, endings in cases.items():
            for ending in endings:
                if noun.endswith(ending):
                    if len(ending) > len(best_ending):
                        best_ending = ending
                        best_matches = [(gender, case)]
                    elif len(ending) == len(best_ending):
                        best_matches.append((gender, case))

    return noun, best_matches, best_ending

while True:
    noun, case, ending = detect_ending()

    if len(case) == 1:
        print(
            f"Прикметник \"{noun}\" у {case[0][0]} {'роді' if case[0][0] != 'множині' else ''}, відмінок: {case[0][1]}, закінчення: -{ending}.")
    else:
        cases_list = ", ".join([match[1] for match in case])
        print(
            f"Прикметник \"{noun}\" у {case[0][0]} {'роді' if case[0][0] != 'множині' else ''}, відмінки: {cases_list}, закінчення: -{ending}.")

    repeat = input("Бажаєте визначити інші закінчення? (так/ні): ").strip().lower()
    if repeat != "так":
        print("Дякуємо за користування!")
        break