
from .schedule.pars_schedule import get_schedule
import vk
from flask import Flask, request, json
from .settings import *
import json
from .WORDS import WORDS, DAYS
# from .Schedule40.schedule import get_schedule as get_arina_schedule


def take_care_about_call(req: 'request')->'performin bot action':

    data = json.loads(request.data)
    
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':

        return make_a_respond(data)


def make_a_respond(data):


    message = data['object']['body']

    type_of_function = check_type_to_answer(message)

    if type_of_function == 'Савелий':

        session = vk.Session()
        api = vk.API(session, v=5.0)
        user_id = data['object']['user_id']


        day = get_day(message)

        schedule = get_schedule(day)  

        api.messages.send(access_token=token, user_id=str(
                    user_id), message=schedule)

        return 'ok'
        

### checks wich function need to be used
def check_type_to_answer(message):


    for i in WORDS:
        
        if 'Арина'.lower() in message.lower():
            
            return 'Арина'
        
        elif i.lower() in message.lower():

            return 'Савелий'
        
def get_day(message):

    for day in DAYS.keys():

        if day.lower() in message.lower():

            return DAYS[day]

    return 'today'

