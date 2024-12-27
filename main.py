import json #подключение модуля

number  = input("Введите квалификацию: ")
number_s = number[:len(number)-3] #ввод номера квалификации и специальности
k = True #счётчик
with open('dump.json', 'r', encoding='utf-8') as file: #открывает файл и записывает его в data
    data = json.load(file) 
    for item in data: #перебор всех элементов файла, поиск соответствующей квалификации, если найдена - счётчик меняется
        if item['model'] == "data.specialty" and item["fields"]["code"] == number_s:
            print("===Найдено===")
            print(f'{number_s} >> Специальность "{item["fields"]["title"]}", {item["fields"]["c_type"]}')
            k = False
        if item['model'] == "data.skill" and item["fields"]["code"] == number:
            print(f'{number} >> Специальность "{item["fields"]["title"]}"')
if k: #вывод если не найдено, проверка по счётчику
    print("===Не найдено===")