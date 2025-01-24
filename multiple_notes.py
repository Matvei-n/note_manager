notes = []

def create_note():
    """Создание заметки."""
    global notes
    name = input("Введите имя заметки: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (например, 'выполнено'): ")
    creation_date = input("Введите дату создания заметки в формате ДД.ММ.ГГГГ: ")
    deadline = input("Введите дедлайн заметки в формате ДД.ММ.ГГГГ: ")

    # Создание словаря для каждой заметки
    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }

    notes.append(note)
    print("Заметка успешно создана.")

def display_notes():
    """Отображение заметок."""
    for note in notes:
        print(f"{note['Имя']}:")
        print(f"Заголовок: {note['Заголовок']}\nОписание: {note['Описание']}\nСтатус: {note['Статус']}\nДата создания: {note['Дата создания']}\nДедлайн: {note['Дедлайн']}")

while True:
    command = input("Чтобы создать заметку напишите: 'создать заметку' ").lower()

    if command == "стоп":
        break
    elif command == "создать заметку":
        create_note()
    elif command == "показать заметки":
        display_notes()
    else:
        print("Неизвестная команда. Введите 'стоп', чтобы завершить программу.")