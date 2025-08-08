from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/random')
def random_number():
    number = random.randint(1, 100)
    return render_template('random.html', number=number)

@app.route('/reverse', methods=['GET', 'POST'])
def reverse():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        result = text[::-1]
    return render_template('reverse.html', result=result)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            op = request.form['operation']
            if op == 'add':
                result = a + b
            elif op == 'subtract':
                result = a - b
            elif op == 'multiply':
                result = a * b
            elif op == 'divide':
                result = a / b
        except Exception as e:
            result = f"Error: {e}"
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
