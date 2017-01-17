from django.http import HttpResponse
from channels import Group
from channels.handler import AsgiHandler
# from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http


@channel_session_user_from_http
def ws_add(message):
    message.reply_channel.send({'accept': True})  # accept connection

    room = message.content['path'].strip("/")
    message.channel_session['room'] = room
    Group('chat-{}'.format(room)).add(message.reply_channel)


@channel_session_user
def ws_message(message):
    room = message.channel_session['room']
    Group('chat-{}'.format(room)).send({
        'text': '[user] {} ({}글자)'.format(message.content['text'], len(message.content['text'])),
    })

    # echo
    # message.reply_channel.send({
    #     'text': '[user] {text}'.format(**message.content),
    # })


@channel_session_user
def ws_disconnect(message):
    print('ws_disconnect : {}'.format(message.reply_channel))
    Group('chat').discard(message.reply_channel)

