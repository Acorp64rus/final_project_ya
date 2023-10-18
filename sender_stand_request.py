import configuration
import data
import requests

#ФУНКЦИЯ ДЛЯ СОЗДАНИЯ НОВОГО ЗАКАЗА
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_POINT,
                         json=body)

#response = post_new_order(data.order_body)
#print(response.json())