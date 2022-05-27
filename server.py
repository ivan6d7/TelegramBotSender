from flask import Flask, render_template, redirect
import os
import sys
import inspect
import script


app = Flask(__name__)

@app.route('/')
def index0():
  return redirect("/1", code = 302)

@app.route('/1')
def index1():
  return render_template('index1.html')

@app.route('/2')
def index2():
  return render_template('index2.html')

@app.route('/3')
def index3():
  return render_template('index3.html')

@app.route('/my-link1/')
def my_link1():
  print ('I got clicked!')
  script.sendMessage("1st checkpoint", script.bot)
  return('1st is done!')

@app.route('/my-link2/')
def my_link2():
  print ('I got clicked!')
  script.sendMessage("2nd checkpoint", script.bot)
  return('2nd is done!')

@app.route('/my-link3/')
def my_link3():
  print ('I got clicked!')
  script.sendMessage("3rd checkpoint", script.bot)
  return('3rd is done!')

if __name__ == '__main__':
  app.run(debug=True)