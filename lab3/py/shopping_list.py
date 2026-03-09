# Модуль для работы со списком покупок

def add_item(shopping_list, item):
    # Добавление товара в список покупок
    if item in shopping_list:
        print("Этот товар уже есть в списке.")
    else:
        shopping_list.append(item)
        print(f"Товар '{item}' добавлен в список.")

def remove_item(shopping_list, identifier):
    # Удаление товара из списка покупок
    if isinstance(identifier, int):
        if 1 <= identifier <= len(shopping_list):
            removed = shopping_list.pop(identifier - 1)
            print(f"Товар '{removed}' удален из списка.")
        else:
            print("Неверный номер. Попробуйте снова.")
    elif isinstance(identifier, str):
        if identifier in shopping_list:
            shopping_list.remove(identifier)
            print(f"Товар '{identifier}' удален из списка.")
        else:
            print("Товар не найден в списке.")

def display_list(shopping_list):
    # Отображение списка покупок
    if not shopping_list:
        print("Список покупок пуст.")
    else:
        print("Текущий список покупок:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")