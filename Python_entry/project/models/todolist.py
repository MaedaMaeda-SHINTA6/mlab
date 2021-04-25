"""
model(todolist)
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from flask import request, redirect, url_for, render_template, session
from project import app
from project.models.task import Task

# データベースの指定
engine = sqlalchemy.create_engine('sqlite:///sampledb.db', echo=True)


#categoryと対応した日本語情報を返す
def categoryinit():
    categoryList = {'job':'仕事関係','hobby':'趣味関係','housework':'家事関係','friendship':'交友関係'}
    return categoryList

#todolistに情報を追加する
def todolistAdd(category,name,date,note):
    #listを生成
    todolist = []
    session = sessionmaker(bind=engine)()
    task = Task()
    task.name = name
    task.category = category
    task.plan = date
    task.etc = note
    task.finFlag = 0
    session.add(instance=task)
    session.commit()
    todolist = todoSearchAll()
    return todolist

def todoSearchAll():
    #listを生成
    todolist = []
    session = sessionmaker(bind=engine)()
    returnTodolist=session.query(Task)
    for reTasks in returnTodolist:
        todolist.append({'count':reTasks.taskid,'category':reTasks.category,'name':reTasks.name,'date':reTasks.plan,
        'note':reTasks.etc,'flag':reTasks.finFlag, 'report':reTasks.report}) 
    session.commit()
    return todolist

#todolistからIDで検索する
def todoSearch(id):
    todolist = []
    session = sessionmaker(bind=engine)()
    returnTodolist=session.query(Task).filter(Task.taskid == id)
    for reTasks in returnTodolist:
        todolist.append({'count':reTasks.taskid,'category':reTasks.category,'name':reTasks.name,'date':reTasks.plan,
        'note':reTasks.etc,'flag':reTasks.finFlag, 'report':reTasks.report}) 
    session.commit()
    dict_todolist = {}
    dict_todolist = todolist[0]
    return dict_todolist

#todolistからtodoを完了する
def todoFinish(id,report):
    todolist = []
    session = sessionmaker(bind=engine)()
    returnTodolist = session.query(Task).filter(Task.taskid == id).first()
    returnTodolist.finFlag = 1
    returnTodolist.report = report
    session.commit()
    dict_todolist = todoSearch(id)
    print(dict_todolist)
    return dict_todolist