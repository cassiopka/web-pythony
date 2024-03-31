from flask import Flask, render_template,request, make_response, jsonify
import re

app = Flask(__name__)

application = app

@app.route('/')
def index():
    msg = 'Hello world'
    return render_template('index.html',msg=msg)

@app.route('/argv')
def argv():
    return render_template('argv.html')

@app.route('/calc')
def calc():
    result = ''
    num1 =  request.args.get('num1') 
    oper = request.args.get('operation') 
    num2 = request.args.get('num2')
    if oper == "+": 
        result = int(num1)+ int(num2)
    elif oper == "-":
        result = int(num1) - int(num2)
    elif oper == "*":
        result = int(num1) * int(num2)
    elif oper == "/":
        result = int(num1)/int(num2)

    return render_template('calc.html', result=result)

@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/cookie')
def cookie():
    resp = make_response(render_template('cookie.html'))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user','NoName')
    return resp

@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html' )

@app.route('/phone_check', methods=['POST'])
def phone_check():
    phone_number = request.form.get('phone_number')
    
    if not phone_number:
        return jsonify({'error': 'Поле с номером телефона не заполнено.'}), 400
    
    phone_number = phone_number.replace('+7', '8')
    
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    if len(phone_number) < 10 or len(phone_number) > 12:
        return jsonify({'error': 'Недопустимый ввод. Неверное количество цифр.'}), 400
    if not re.match(r'^(\+?\d{1,2})?[\s\(\.-]?(\d{3})[\s\)\.-]?(\d{3})[\s\.-]?(\d{2})[\s\.-]?(\d{2})$', phone_number):
        return jsonify({'error': 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'}), 400
    
    if phone_number[0] not in ('8', '+'):
        phone_number = '8' + phone_number
    
    formatted_phone_number = '8-{}-{}-{}-{}'.format(
        phone_number[1:4], phone_number[4:7], phone_number[7:9], phone_number[9:]
    )
    
    return jsonify({'formatted_phone_number': formatted_phone_number}), 200
