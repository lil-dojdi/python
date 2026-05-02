import os
from gtts import gTTS, lang
from gtts.lang import tts_langs


# 1. ВЫБОР СПОСОБА ВВОДА


print("Выберите способ ввода текста:")
print("1 — Ввести с клавиатуры")
print("2 — Загрузить из файла")

choice = input("Ваш выбор (1/2): ")

text = ""


# 2. ПОЛУЧЕНИЕ ТЕКСТА


try:
    if choice == "1":
        text = input("Введите текст: ")

    elif choice == "2":
        file_path = input("Введите путь к .txt файлу: ")

        if not os.path.exists(file_path):
            raise FileNotFoundError("Файл не найден!")

        if os.path.getsize(file_path) == 0:
            raise ValueError("Файл пустой!")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        raise ValueError("Неверный выбор!")

    # проверка текста
    if not text.strip():
        raise ValueError("Текст пустой!")

except Exception as e:
    print("Ошибка при вводе:", e)
    exit()


# 3. ВЫБОР ЯЗЫКА


languages = tts_langs()

print("\nДоступные языки (пример):")
for code, name in list(languages.items())[:10]:
    print(f"{code} — {name}")

lang_choice = input("\nВведите код языка (например: ru, en): ")

if lang_choice not in languages:
    print("Ошибка: язык не поддерживается!")
    exit()


# 4. СОЗДАНИЕ АУДИО


try:
    tts = gTTS(text=text, lang=lang_choice, slow=False)

    output_file = "lab8/output.mp3"
    tts.save(output_file)

    # проверка файла
    if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
        raise Exception("Ошибка создания аудиофайла!")

    print("\n✅ Аудиофайл успешно создан:", output_file)

except Exception as e:
    print("Ошибка при создании аудио:", e)