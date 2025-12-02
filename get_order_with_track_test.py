import data
import sendor_stand_request



#Авто тест для проверки того, что заказ создается и по полученному трек номеру можно получить данные о заказе
def test_order_created_and_data_is_being_output():
    order = sendor_stand_request.create_order(data.order_body)

    #Получение трек номера созданного заказа
    track_number = order.json()["track"]
    print(f" Номер вашего заказа: {track_number}")
    #Получение данных заказа по треку
    response = sendor_stand_request.get_data_order_with_track(track_number)
    assert response.status_code == 200, f"Запрос не прошел, ошибка: {response.status_code}"
    order_data = response.json()
    print(f"Данные вашего заказа: {order_data}")