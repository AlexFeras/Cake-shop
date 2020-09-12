import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from Base import*
from functional import*
import json

token_vk='49836e413787c60d0c5ca795c76f489d972bcc322a3e76a0f373e252aa73a88f37299290bb77b5c1b851b'
group_id=192385645
vk = vk_api.VkApi(token=token_vk)
vk._auth_token()
vk.get_api()

if __name__ == '__main__':
    longpoll = VkBotLongPoll(vk, group_id)
    def get_button(label='but', color='red', payload=''):
        return {
            "action": {
                "type": 'text',
                'payload': payload,#идентификатор кнопки
                'label': label#то что написано на кнопке
            },
            "color": color
        }

    keyboard = str(json.dumps({
        "one_time":False,
            "buttons": [
                [get_button(label="Печенье", color='secondary')],[get_button(label="Булочка", color='secondary'),get_button(label="Тортик", color='secondary')]
            ]
    }, ensure_ascii=False)) #Обязательная строчка

    keyboard_baker = str(json.dumps({
        "one_time": False,
        "buttons": [
            [get_button(label="Печенье", color='secondary')],
            [get_button(label="Булочка", color='secondary'), get_button(label="Тортик", color='secondary')],[get_button(label="Пополнить_ресурсы", color='secondary')]
        ]
    }, ensure_ascii=False))
    while True:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.message['text'].lower() == "начать":
                    a_name = vk.method('users.get', {'user_ids': event.object.message['peer_id']})
                    a_name = a_name[0]['first_name']
                    vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                'message': 'Привет  ' + str(
                                                    a_name) + ' Выберите то,что хотите купить',
                                                'random_id': 0, 'keyboard': keyboard})
                if event.object.message['text'].lower() == "печенье":
                    vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                'message': 'Какое количество вы хотите купить?(в кг)',
                                                'random_id': 0})
                if event.object.message['text'].isdigit():# получает цифры
                    if a.query(Item).filter(Item.quantity >= int(event.object.message['text'])).first():#сюда передаёт количество
                        k=a.query(Item).filter(Item.name == "Печенька1").first()
                        k.quantity -= int(event.object.message['text'])#как получить введённое значение?
                        a.commit()
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'спасибо за покупку',
                                                    'random_id': 0})

                if event.object.message['text'].lower() == "пекарь":
                    a_name = vk.method('users.get', {'user_ids': event.object.message['peer_id']})
                    a_name = a_name[0]['first_name']
                    vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                'message': 'Привет  ' + str(
                                                    a_name) + ' Выберите то,что хотите приготовить',
                                                'random_id': 0,
                                                'keyboard': keyboard_baker})
                if event.object.message['text'].lower() == "пополнить_ресурсы":
                    vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                'message': 'Введите количество продуктов',
                                                'random_id': 0})
                if event.object.message['text'].isdigit():
                    zz = a.query(Atem).filter(Atem.id == 5).first()
                    zz.quantity += int(event.object.message['text'])
                    a.commit

                if event.object.message['text'].lower() == "печеньки":
                    vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                'message': 'Какое количество вы хотите испечья?',
                                                'random_id': 0})
                    if event.object.message['text'].isdigit():
                        k=a.query(Item).filter(Item.name=="Печенька")
                        k.quantity+=int(event.object.message['text'])
                        a.commit()
                        Simplebiscuits(event.object.message['text'].isdigit(),"Печенька")
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Продукт готов',
                                                    'random_id': 0})
                if event.object.message['text'].lower() == "булочки":
                    vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                'message': 'Какое количество вы хотите испечь?',
                                                'random_id': 0})
                    if event.object.message['text'].isdigit():
                        k = a.query(Item).filter(Item.name == "Булочка")
                        k.quantity += int(event.object.message['text'])
                        a.commit()
                        SimpleCake()
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Продукт готов',
                                                    'random_id': 0})




