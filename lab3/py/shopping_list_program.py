from shopping_list import add_item, remove_item, display_list

# Меню для работы со списком покупок
shopping_list = []
while True:
    print("\nМеню:")
    print("1. Вывести список текущих товаров")
    print("2. Добавить товар в список")
    print("3. Удалить товар из списка")
    print("4. Выход")

    choice = input("Выберите опцию (1–4): ").strip()
    if choice == "1":
        display_list(shopping_list)
    elif choice == "2":
        item = input("Введите название товара: ").strip()
        add_item(shopping_list, item)
    elif choice == "3":
        method = input("Удалить по номеру (1) или названию (2)? ").strip()
        if method == "1":
            try:
                index = int(input("Введите номер товара: ").strip())
                remove_item(shopping_list, index)
            except ValueError:
                print("Неверный ввод. Введите число.")
        elif method == "2":
            name = input("Введите название товара: ").strip()
            remove_item(shopping_list, name)
        else:
            print("Неверный выбор метода удаления.")
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")