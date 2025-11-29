import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def save_results():
    answers = {
        "Жанр": genre_var.get(),
        "Время в неделю": time_var.get(),
        "Режим игры": mode_var.get(),
        "Сюжет важен": plot_var.get(),
        "Графика": graphics_var.get()
    }
    if not all(answers.values()):
        messagebox.showwarning("Ошибка", "Пожалуйста, ответьте на все вопросы.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_text = f"Анкета заполнена: {timestamp}\n"
    for question, answer in answers.items():
        result_text += f"{question}: {answer}\n"
    result_text += "-" * 40 + "\n\n"
    try:
        with open("game_preferences.txt", "a", encoding="utf-8") as f:
            f.write(result_text)
        messagebox.showinfo("Успех", "Ваши предпочтения успешно сохранены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")
root = tk.Tk()
root.title("🎮 Анкета: Какой вы игрок?")
root.geometry("500x400")
root.resizable(False, False)
genre_var = tk.StringVar()
time_var = tk.StringVar()
mode_var = tk.StringVar()
plot_var = tk.StringVar()
graphics_var = tk.StringVar()
tk.Label(root, text="1. Какой жанр игр вам ближе?", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 5))
genres = ["RPG", "Шутер", "Стратегия", "Песочница", "Головоломка", "Симулятор"]
ttk.Combobox(root, textvariable=genre_var, values=genres, state="readonly", width=30).pack(anchor="w", padx=40)
tk.Label(root, text="2. Сколько времени вы играете в неделю?", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 5))
time_options = ["< 5 часов", "5–10 часов", "10–20 часов", "> 20 часов"]
ttk.Combobox(root, textvariable=time_var, values=time_options, state="readonly", width=30).pack(anchor="w", padx=40)
tk.Label(root, text="3. Предпочитаете одиночную или многопользовательскую игру?", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 5))
ttk.Radiobutton(root, text="Одиночная", variable=mode_var, value="Одиночная").pack(anchor="w", padx=40)
ttk.Radiobutton(root, text="Многопользовательская", variable=mode_var, value="Многопользовательская").pack(anchor="w", padx=40)
tk.Label(root, text="4. Важна ли вам сюжетная линия?", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 5))
ttk.Radiobutton(root, text="Да", variable=plot_var, value="Да").pack(anchor="w", padx=40)
ttk.Radiobutton(root, text="Нет", variable=plot_var, value="Нет").pack(anchor="w", padx=40)
tk.Label(root, text="5. Какой стиль графики вы предпочитаете?", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 5))
graphics = ["Реалистичная", "Пиксель-арт", "Мультяшная", "Минимализм", "Киберпанк"]
ttk.Combobox(root, textvariable=graphics_var, values=graphics, state="readonly", width=30).pack(anchor="w", padx=40)
tk.Button(root, text="Сохранить результаты", command=save_results, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)
root.mainloop()
