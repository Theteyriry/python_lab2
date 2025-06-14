
# Читаем числа из файла data.txt
with open('data.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Находим результаты
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Записываем результатов в файл result.txt
with open('result.txt', 'w') as file:
    file.write(f"Сумма: {sum_numbers}\n")
    file.write(f"Среднее: {average}\n")  
    file.write(f"Максимум: {maximum}\n")
    file.write(f"Минимум: {minimum}\n")

print("Результат записан в файл result.txt")