# -*- coding: utf-8 -*-
import requests
import json


def Chat():
    print("Robot: 您好，有什么需要帮助的吗？[输入0退出]")
    while True:
        text=input("Me: ")
        if text=='0':
            print("Robot: 再见～")
            break
        url="http://127.0.0.1:5000/search?q="+text
        response = requests.get(url)
        result = json.loads(response.content)['answer']
        print("Robot:",result)

if __name__ == '__main__':
    Chat()
