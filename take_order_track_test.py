#ВЛАДИСЛАВ КОРОЛЕВ, 9-Я КОГОРТА - ФИНАЛЬНЫЙ ПРОЕКТ. ИНЖЕНЕР ПО ТЕСТИРОВАНИЮ ПЛЮС

import sender_stand_request
import data

#ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ТРЭК-НОМЕРА
def take_track():
    new_order = sender_stand_request.post_new_order(data.order_body) #СОХРАНЯЕМ В ПЕРЕМЕННУЮ ФУНКЦИЮ ДЛЯ СОЗДАНИЯ ЗАКАЗА
    track_number = new_order.json()['track'] #СОХРАНЯЕМ В ПЕРЕМЕННУЮ ЗНАЧЕНИЕ ТРЭК-НОМЕРА
    return track_number #ВОЗВРАЩАЕМ В ФУНКЦИЮ take_track ЗНАЧЕНИЕ ТРЭК-НОМЕРА

#response = take_track() #СОХРВНЯЕМ ФУНКЦИЮ ДЛЯ ПОЛУЧЕНИЯ ТРЭК-НОМЕРА В ПЕРЕМЕННУЮ
#print(response) #ВЫВОДИМ НА ЭРКАН ТРЭК-НОМЕР


#ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ЗАКАЗА ПО ЕГО НОМЕРУ
def truck_order_assert():
    track = take_track()
    return requests.get(configuration.URL_SERVICE + сonfiguration.ORDER_NUMBER_POINT + track)
    assert response.truck_order_assert == 200 #ПРОВЕРЯЕМ СООТВЕТСТВУЕТ ЛИ СТАТУС КОД 200

def test_order():
    truck_order_assert