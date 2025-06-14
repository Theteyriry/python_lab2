import re

# Читаем текст из файла text.txt
try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Находим email-адреса
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    with open('emails.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(emails))
    
    # Находим номера телефонов в формате +7-XXX-XXX-XX-XX
    phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)
    with open('phones.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(phones))
    
    # Находим слова, начинающиеся с заглавной буквы
    capital_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', text)
    with open('capital_words.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(capital_words))
    
    print("Результаты успешно сохранены в файлы:")
    print("- emails.txt")
    print("- phones.txt")
    print("- capital_words.txt")

except FileNotFoundError:
    print("Ошибка: файл text.txt не найден в текущей директории")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")