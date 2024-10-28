from flask import Flask
import random

app = Flask(__name__)

num = 5
def toolow():
    return '<h1 style = "text-align: center">number is too low</h1>'\
    '<div style="width: 50%; margin: 0 auto; text-align: center;"><img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHZ1OG50cXlmaGpoM2VwMHJybXU4MW9mdHk5ZHFjZHFldHUzY2xmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ia62g1fUnD1egRBsU0/giphy.gif" width = "300" height = "200"></div>'

@app.route('/')
def greet():
    return '<h1 style = "text-align: center">please guess a no. between 0 to 9</h1>'\
    '<div style="width: 50%; margin: 0 auto; text-align: center;"><img src = "./static/1.gif" width = "300" height = "200"></div>'

@app.route('/<int:number>')
def check(number):
    if number <5:
        return '<h1 style = "text-align: center">number is too low</h1>'\
        '<div style="width: 50%; margin: 0 auto; text-align: center;"><img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHZ1OG50cXlmaGpoM2VwMHJybXU4MW9mdHk5ZHFjZHFldHUzY2xmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ia62g1fUnD1egRBsU0/giphy.gif" width = "300" height = "200"></div>'
    elif number>5:
        return '<h1 style = "text-align: center">number is too high</h1>'\
        '<div style="width: 50%; margin: 0 auto; text-align: center;"><img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHZ1OG50cXlmaGpoM2VwMHJybXU4MW9mdHk5ZHFjZHFldHUzY2xmNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ia62g1fUnD1egRBsU0/giphy.gif" width = "300" height = "200"></div>'
    else:
        return '<h1 style = "text-align: center">you got it right</h1>'

if __name__ == '__main__':
    app.run(debug=True)
