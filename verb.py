def detect_ending():
    cases_present = {
        "1о": ["у", "ю"],
        "2о": ["еш", "єш"],
        "3о": ["е", "є"], 
        "1м": ["емо", "ємо"],
        "2м": ["ете", "єте"],
        "3м": ["уть", "ють"], 
    }

    cases_imperative = {
        "2о": ["й", "и"], 
        "1м": ["мо"],
        "2м": ["те", "ть"]
    }

    cases_future = {
        "1о": ["му"],
         "2о": ["меш"],
        "3о": ["ме"], 
        "1м": ["мемо", "м"], 
        "2м": ["мете"],
        "3м": ["муть"],
    }

    cases_past = {
        "m": ["в"],
        "f": ["ла"], 
        "n": ["ло"],
        "pl": ["ли"],
    }

    while True:
        isPresent = False


        verb = input("Введіть дієслово 1 відміни у теперішньому часі в 3 ос.мн (вони): ").strip().lower()

        for ending in cases_present["3м"]:
            if verb.endswith(ending):
                print(
                    f"Дієслово 1 відміни \"{verb}\" у теперішньому часі в 3 ос.мн (вони), закінчується на \"{ending}\".")
                isPresent = True
                break

        if not isPresent:
            print(f"Введене дієслово \"{verb}\" не є 1-ої відміни. Спробуйте ще раз.")
            continue
        else:
            break

       
    noun = input("Введіть це ж дієслово у будь-якому іншому часі чи способі: ").strip().lower()

    return find_best_ending(noun, cases_present, cases_imperative, cases_future, cases_past, isPresent)




def find_best_ending(verb, cases_present, cases_imperative, cases_future, cases_past, isPresent):
    best_matches = []
    best_ending = ""

    relevant_cases = {
        "Теперішній час": cases_present,
        "Наказовий спосіб": cases_imperative,
        "Майбутній час": cases_future,
        "Минулий час": cases_past,
    }

    for time_or_mood, cases in relevant_cases.items():
        for person_number, endings in cases.items():
            for ending in endings:
                if verb.endswith(ending): 
                    if len(ending) > len(best_ending):
                        best_ending = ending
                        best_matches = [(time_or_mood, person_number)]
                    elif len(ending) == len(best_ending):
                        best_matches.append((time_or_mood, person_number))

    return verb, best_matches, best_ending


def morphoepic_function(verb, case_info, ending):
    case, person = case_info[0]  

    if case == "Майбутній час": 
        if "ти" in verb:
            parts = verb.split("ти", 1)
            root = parts[0] 
            inf_suffix = "ти"
        else:
            root = verb 
            inf_suffix = ""

        word_parts = []

        if person in ["1о", "3о"]:
            word_parts.append(f"{root}-{inf_suffix}-{ending}-0")
            explanation = (
                f"Суфікс інфінітива: '{inf_suffix}', "
                f"словозмінний суфікс: '{ending}', "
                f"закінчення: '0'"
            )
            return f"{word_parts[0]}\n{explanation}", "0"
        elif person in ["2о"]:
            word_parts.append(f"{root}-{inf_suffix}-ме-ш")
            explanation = (
                f"Суфікс інфінітива: '{inf_suffix}', "
                f"словозмінний суфікс: 'ме', "
                f"закінчення: 'ш'"
            )
            return f"{word_parts[0]}\n{explanation}", "ш"
        elif person in ["1м"]:
            if ending == "м":
                word_parts.append(f"{root}-{inf_suffix}-ме-м")
                explanation = (
                    f"Суфікс інфінітива: '{inf_suffix}', "
                    f"словозмінний суфікс: 'ме', "
                    f"закінчення: 'м'"
                )
               
                return f"{word_parts[0]}\n{explanation}", "м"
            elif ending == "мемо":
                word_parts.append(f"{root}-{inf_suffix}-ме-мо")
                explanation = (
                    f"Суфікс інфінітива: '{inf_suffix}', "
                    f"словозмінний суфікс: 'ме', "
                    f"закінчення: 'мо'"
                )
               
                return f"{word_parts[0]}\n{explanation}", "мо"
        elif person in ["3м"]:
            word_parts.append(f"{root}-{inf_suffix}-му-ть")
            explanation = (
                f"Суфікс інфінітива: '{inf_suffix}', "
                f"словозмінний суфікс: 'му', "
                f"закінчення: 'ть'"
            )
            return f"{word_parts[0]}\n{explanation}", "ть"
        elif person in ["2м"]:
            word_parts.append(f"{root}-{inf_suffix}-ме-те")
            explanation = (
                f"Суфікс інфінітива: '{inf_suffix}', "
                f"словозмінний суфікс: 'ме', "
                f"закінчення: 'те'"
            )
            return f"{word_parts[0]}\n{explanation}", "те"

        return f"{word_parts[0]}\n{explanation}", ending

    elif case == "Минулий час":
        if verb.endswith(ending):
            root = verb[:-len(ending)] 
        else:
            root = verb  

        if person == "m":  
            return f"{root}-в-0\nСловозмінний суфікс: 'в', закінчення: '0'", "0"
        elif person == "f": 
            return f"{root}-л-а\nСловозмінний суфікс: 'л', закінчення: 'а'", "а"
        elif person == "n": 
            return f"{root}-л-о\nСловозмінний суфікс: 'л', закінчення: 'о'", "о"
        elif person == "pl":  
            return f"{root}-л-и\nСловозмінний суфікс: 'л', закінчення: 'и'", "и"
    
    elif case == "Наказовий спосіб":
        if person == "2о":
            if verb.endswith("й"):
                root = verb[:-1]
                return f"{root}-й-0\nСуфікс наказовості: 'й', закінчення: '0'", "0"
            elif verb.endswith("и"):
                root = verb[:-1]
                return f"{root}-и, закінчення: 'и'", "и"
        elif person == "1м":
            return f"{verb}-й\nСуфікс наказовості: 'й', закінчення: 'мо'", "мо"
        elif person == "2м":
            if ending == "те":
                return f"{verb[:-2]}-те\nСуфікс наказовості: 'те', закінчення: 'те'", "те"
            elif ending == "ть":
                return f"{verb[:-3]}-іть\nЗакінчення: 'іть'", "іть"
            
    elif case == "Теперішній час":
        if verb.endswith(ending):
            root = verb[:-len(ending)]
        else:
            root = verb
        return f"{root}-{ending}\nЗакінчення: '{ending}'", ending

    return f"{verb}-{ending}", "0"

while True:
    noun, case, ending = detect_ending()
    result, ending = morphoepic_function(noun,case, ending)

    print(result) 
    if len(case) == 1:
        print(
            f"Дієслово \"{noun}\" у {case[0][0]}, {'рід' if case[0][0] == 'Минулий час' else 'особа'}: {case[0][1]}, закінчення: -{'мо' if ending == 'мемо' else ending}.")
    else:
        cases_list = ", ".join([match[1] for match in case])
        cases_name_list = ", ".join([match[0] for match in case]) 

    repeat = input("Бажаєте визначити інші закінчення? (так/ні): ").strip().lower()
    if repeat != "так":
        print("Дякуємо за користування!")
        break