import json
from datetime import datetime

def generate_user_json():
    users = []
    print("Введите данные для 5 пользователей (или больше):")
    for i in range(5):
        print(f"\nПользователь {i + 1}:")
        login = input("Логин: ").strip()
        last_login_str = input("Время последнего входа (YYYY-MM-DD HH:MM:SS): ").strip()
        duration = int(input("Длительность пребывания на сайте (в минутах): "))
        try:
            last_login = datetime.strptime(last_login_str, "%Y-%m-%d %H:%M:%S").isoformat() + "Z"
        except ValueError:
            print("Неверный формат даты. Используйте YYYY-MM-DD HH:MM:SS. Устанавливаем текущее время.")
            last_login = datetime.now().isoformat() + "Z"
        user = {
            "login": login,
            "last_login": last_login,
            "session_duration_minutes": duration
        }
        users.append(user)
    json_str = json.dumps(users, indent=2, ensure_ascii=False)
    return json_str

def parse_and_display_json(json_str):
    try:
        users = json.loads(json_str)
        print("\n" + "="*60)
        print("Информация о пользователях:")
        print("="*60)
        for user in users:
            login = user.get("login", "Неизвестно")
            last_login = user.get("last_login", "Неизвестно")
            duration = user.get("session_duration_minutes", 0)
            if last_login.endswith("Z"):
                dt = datetime.fromisoformat(last_login[:-1])
                formatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")
            else:
                formatted_date = last_login
            print(f"Логин: {login}")
            print(f"  Последний вход: {formatted_date}")
            print(f"  Длительность сессии: {duration} мин")
            print("-" * 40)
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON.")

def main():
    print("Программа управления данными пользователей сайта")
    print("-" * 50)
    while True:
        print("\nВыберите действие:")
        print("1. Сгенерировать JSON-строку с данными пользователей")
        print("2. Разобрать и вывести JSON-строку")
        print("3. Выйти")
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice == '1':
            json_data = generate_user_json()
            print("\nСгенерированная JSON-строка:")
            print(json_data)
            with open("users.json", "w", encoding="utf-8") as f:
                f.write(json_data)
            print("\nДанные сохранены в файл 'users.json'")
        elif choice == '2':
            print("\nВыберите способ ввода JSON:")
            print("a) Ввести вручную")
            print("b) Загрузить из файла 'users.json'")
            option = input("Ваш выбор (a/b): ").strip().lower()
            if option == 'a':
                print("Введите JSON-строку (в одну строку или скопируйте из файла):")
                json_input = input()
                parse_and_display_json(json_input)
            elif option == 'b':
                try:
                    with open("users.json", "r", encoding="utf-8") as f:
                        json_input = f.read()
                    parse_and_display_json(json_input)
                except FileNotFoundError:
                    print("Файл 'users.json' не найден. Сначала сгенерируйте данные (пункт 1).")
            else:
                print("Неверный выбор.")
        elif choice == '3':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()