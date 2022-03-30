from pprint import pprint

def my_cook_buk():
    with open('cook.txt',encoding='utf-8') as file:
        menu = {}
        for line in file:
            dish_name = line[:-1]
            counter = file.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingridient = file.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file.readline()

    return(menu)

def get_shop_list_by_dishes(dishes, persons=int):
    menu = my_cook_buk()
    shop_list = {}
    for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shop_list.get(item['ingredient_name']):
                    extra_item = (int(shop_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shop_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shop_list.update(items_list)
    pprint(shop_list)
    

get_shop_list_by_dishes(['Омлет'], 3)