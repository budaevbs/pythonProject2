import vk_api
import requests
from vk_api import VkApi


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device

def vk_login(login, password, app_id):
    vk_session = VkApi(login, password,
                       auth_handler=auth_handler, app_id=app_id)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    return vk_session.get_api()

app_id = '51691338' # укажите тут your app_id приложения MeetChat
login = "<89834226249>"
password = "<M@ksar2015>"
vk = vk_login(login, password, app_id)