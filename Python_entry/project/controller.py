"""
Controller
"""

import os
from flask import request, redirect, url_for, render_template, session
from project import app
from project.models import todolist

@app.route('/') # URL指定。URLにリクエストが来ると関数内が実行される。
def start():
    return render_template('category.html')

@app.route('/index',methods=["GET","POST"]) 
def index():
    categoryid = request.form["category"]
    categorylist = todolist.categoryinit()
    return render_template('index.html',categorylist = categorylist, category = categoryid)

@app.route('/result',methods=["POST"]) 
def result():
    categorylist = todolist.categoryinit()
    resultTodolist = todolist.todolistAdd(request.form["category"],request.form["name"],request.form["date"],request.form["note"])
    return render_template("index.html",categorylist = categorylist,todolist = resultTodolist)

@app.route('/fin/<int:id>',methods=["GET","POST"])
def finish(id):
    if request.method == 'POST':
        resultTodolist = todolist.todoFinish(id,request.form["report"])
        return render_template("category.html",todolist = resultTodolist)
    elif request.method == 'GET':
        resultTodo = todolist.todoSearch(id)
        return render_template("finish.html",todo = resultTodo)
