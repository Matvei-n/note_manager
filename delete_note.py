notes = [
    {
        "name": "Иван",
        "title": "Записка 1",
        "text": "Это первая заметка."
    },
    {
        "name": "Мария",
        "title": "Записка 2",
        "text": "Это вторая заметка."
    },
    {
        "name": "Сергей",
        "title": "Записка 3",
        "text": "Это третья заметка."
    }
]

def delete_note(notes, criterion):
    if criterion == "name":
        return [note for note in notes if note["name"] != criterion]
    elif criterion == "title":
        return [note for note in notes if note["title"] != criterion]
    else:
        print("Некорректный критерий для удаления.")
        return notes

while True:
    criterion = input("Введите критерий для удаления (имя пользователя или заголовок): ")
    if not criterion:
        break
    result = delete_note(notes, criterion)
    if result == notes:
        print("Заметок для удаления не найдено.")
    else:
        notes = result
        print(notes)
