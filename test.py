# -*- coding: utf-8 -*-


import sys
from process_question import Question
# 创建问题处理对象，这样模型就可以常驻内存
que=Question()
# Restorepip freeze > requirements.txt
def enablePrint():
    sys.stdout = sys.__stdout__
enablePrint()


result=que.question_process("李连杰生日是哪天？")
print(result)
