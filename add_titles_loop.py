def get_title():
    title = input("Введите заголовок  (или введите 'стоп', чтоб завершить): ")
    return title

#Основная программа
titles = []
while True:
    title = get_title()
    if title == "стоп":
        break
    elif title != '':  # Функция для запроса заголовка заметки
        titles.append(title)

print("Вы ввели следуещие заголовки:")
for title in titles:
    print("- ", title)

