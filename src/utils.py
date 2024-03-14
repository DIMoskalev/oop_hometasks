import json


def read_from_file_json(file_path):
    """
    Функция считывает данные из файла file_path и возвращает список с товарами
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def creating_class_objects(list_of_objects):
    object_list = []
    object_list.append(list_of_objects[0]['name'])
    object_list.append(list_of_objects[0]['description'])
    object_list.append(list_of_objects[0]['products'])
    # for object in list_of_objects:
    #     object_list.append(object['name'][0])
    #     object_list.append(object['description'][0])
    #     object_list.append(object['products'][0])

    return object_list


# print(read_from_file_json(OPERATIONS_PATH))
# print(creating_class_objects(read_from_file_json(OPERATIONS_PATH)))
