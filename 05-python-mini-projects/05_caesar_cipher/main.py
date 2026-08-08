# Автор: Ира Улмаскулова (ulmaskulovaira-collab)
# Проект: Шифр Цезаря
# Описание: Шифрует и расшифровывает текст со сдвигом букв алфавита на N позиций.

print("=== Шифр Цезаря ===")
print("Автор: Ира Улмаскулова")
print("Сдвиг букв алфавита на N позиций\n")


def caesar(text: str, shift: int, mode: str = "encrypt") -> str:
    """
    Шифрует или расшифровывает текст с помощью шифра Цезаря.

    text  — исходный текст
    shift — на сколько позиций сдвигать буквы
    mode  — "encrypt" (зашифровать) или "decrypt" (расшифровать)
    """
    result = []

    for char in text:
        if char.isalpha():  # Работаем только с буквами
            # Определяем, с какой буквы начинается алфавит (A или a)
            base = ord("A") if char.isupper() else ord("a")

            # При шифровании сдвигаем вперёд, при расшифровке — назад
            offset = shift if mode == "encrypt" else -shift

            # Вычисляем новую букву с учётом цикличности алфавита (mod 26)
            new_char = chr((ord(char) - base + offset) % 26 + base)
            result.append(new_char)
        else:
            # Цифры, пробелы и знаки препинания оставляем без изменений
            result.append(char)

    return "".join(result)


# --- Основная программа ---

text = input("Введи текст: ")

# Запрашиваем величину сдвига
try:
    shift = int(input("Введи сдвиг (например 3 или 7): "))
except ValueError:
    shift = 4
    print("Некорректный ввод. Установлен сдвиг = 4")

# Выбираем режим работы
mode_input = input("Режим (e = зашифровать / d = расшифровать): ").strip().lower()
mode = "decrypt" if mode_input in ("d", "decrypt", "расшифровать") else "encrypt"

# Получаем и выводим результат
result = caesar(text, shift, mode)
print(f"\n▶ Результат: {result}")
