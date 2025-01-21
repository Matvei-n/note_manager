from datetime import datetime

def compare_dates(issue_date):
    # Преобразуем строку в объект даты
    try:
        issue_date = datetime.strptime(issue_date, '%Y-%m-%d')
    except ValueError:
        print("Неверный формат даты!")
        return

    # Получаем текущую дату
    current_date = datetime.now()


    if current_date > issue_date:
        return "Дедлайн истёк!"
    else:
        # Вычисляем разницу между текущей датой и дедлайном
        delta = issue_date - current_date
        days_left = delta.days

        return f"До истечения срока осталось {days_left} дней."

# Вводим дату дедлайна
while True:
    issue_date_input = input("Введите дату дедлайна в формате ГГГГ-ММ-ДД: ")


    try:
        compare_dates(issue_date_input)
        break
    except Exception as e:
        print(e)

# Выводим результат сравнения
result = compare_dates(issue_date_input)
print(result)

