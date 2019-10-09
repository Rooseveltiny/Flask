
from schedule.pars_schedule import get_schedule
import vk
from flask import Flask, request, json
from settings import *
import json
from WORDS import WORDS, DAYS, USERS_TO_SEND
from Schedule40.schedule import get_schedule as get_arina_schedule


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

    session = vk.Session()
    api = vk.API(session, v=5.0)
    user_id = data['object']['user_id']


    day = get_day(message)

    schedule = get_schedule(day)  

    api.messages.send(access_token=token, user_id=str(
                    user_id), message=schedule)

    return 'ok'

def send_schedule():

    session = vk.Session()
    api = vk.API(session, v=5.0)

    ar_schedule = get_arina_schedule('6г')

    for user_id in USERS_TO_SEND:
        api.messages.send(access_token=token, user_id=str(
                    user_id), message=ar_schedule)


    return 'ok' 
        

if __name__ == "__main__":
    
    send_schedule()