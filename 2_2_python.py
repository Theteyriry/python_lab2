try:
    # Запрос чисел у пользователя
    n1 = float(input("Введите первое число: "))
    n2 = float(input("Введите второе число: "))
    
    # Проверка деления на ноль
    if n2 == 0:
        raise ZeroDivisionError("Ошибка: деление на ноль невозможно")
    
    # Выполнение деления и вывод результата
    result = num1 / num2
    print(f"Результат деления: {result:.2f}")  # Округление до 2 знаков после запятой

except ValueError:
    print("Ошибка: введено нечисловое значение")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")