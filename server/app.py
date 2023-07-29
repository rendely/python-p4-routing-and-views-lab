#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_param(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count_param(parameter):
    count_array = [f"{n}" for n in range(0, parameter)]
    return "\n".join(count_array)+"\n"

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        ans = num1+num2 
    elif operation == '-':
        ans = num1-num2 
    elif operation == '*':
        ans = num1*num2     
    elif operation == 'div':
        ans = num1 / num2    
    elif operation == '%':
        ans = num1 % num2     
        
    return str(ans)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
