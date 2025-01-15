notes = []

def add_note():
    name = input("Введите имя: ")
    content = input("Введите содержание заметки: ")
    status = input("Введите статус (например, 'черновик', 'готово'): ")
    creation_date = input("Введите дату создания в формате ДД.ММ.ГГГГ: ")
    modification_date = input("Введите дату изменения в формате ДД.ММ.ГГГГ: ")


    headers = []
    while True:
        header = input(f"Введите заголовок ('продолжить' or 'завершить'): ")
        if header == 'завершить':
            break
        else:
            headers.append(header)

    note = [
        name,
        content,
        status,
        creation_date,
        modification_date,
        headers
    ]

    notes.append(note)
    print("Заметка добавлена!")
    return notes

def display_notes():
    for note in notes:
        print(f"{note[0]}")
        print(f"Содержание: {note[1]}")
        print(f"Статус: {note[2]}")
        print(f"Дата создания: {note[3]}")
        print(f"Дата изменения: {note[4]}")

        for header in note[5]:
            print(f"\t{header}")

notes = add_note()
display_notes()

