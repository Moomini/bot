#! /usr/bin/env python

import requests
import vk_api
import numpy as np
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

vk_session = vk_api.VkApi(token='53fd4b17d1afd79721d4397c7f53f83e5534396652087ae882c5f67c4eb76ed22513c49de6e7f19614d90')

def rand_id():
    random_user_id=np.int64(randint(10000,1000000000000))
    return random_user_id


longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
    #Слушаем longpoll, если пришло сообщение то:
        message = str(event.text).lower()
        vars = ['привет', 'хай', 'прив']
        if message in vars: #Если написали заданную фразу

            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Как дела?',
                    random_id=rand_id())

            elif event.from_chat:  #Если написали в Беседе
                vk.messages.send(  #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Как дела?',
                    random_id=rand_id())


#if __name__ == '__main__':
    #main()