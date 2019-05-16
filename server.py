# -*- coding: utf-8 -*-
import json
from flask import Flask,request
import sys
from process_question import Question


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

app = Flask(__name__,static_url_path="")
app.after_request(after_request)

# 创建问题处理对象，这样模型就可以常驻内存
que=Question()
# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
enablePrint()


@app.route('/')
def index():
    return app.send_static_file('index.html')

# http://127.0.0.1:5000/search?q=你好
@app.route('/search')
def search():
    text = request.args.get('q')
    answer=que.question_process(text)
    res = json.dumps({"answer":answer})
    return res


if __name__ == '__main__':
    #部署到服务器时host要改成'0.0.0.0'
    app.run(debug=True, host='127.0.0.1', port=5000)
