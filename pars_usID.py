import json

# Предположим, что у вас есть файл с именем "data.json" и он содержит данные в формате JSON

# Открываем файл для чтения
with open("output.json", "r") as file:
    # Читаем содержимое файла
    json_data = file.read()

# Преобразуем содержимое JSON-файла в словарь
# Преобразуем JSON-строку в список словарей
data_list = json.loads(json_data)
list_id = []
# Теперь переменная data_list содержит список словарей
for item in data_list:
    for node in item["data"]["view"]["people"]["nodes"]:
        list_id.append(node["id"])
print(list_id)