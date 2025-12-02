from http.client import responses

import configuration
import requests
import data

#Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


#Получение данных о заказе по трек номеру
def get_data_order_with_track(track_number):
    url_get_order = f"{configuration.URL_SERVICE}{configuration.GET_ORDER}{track_number}"
    return requests.get(url_get_order)