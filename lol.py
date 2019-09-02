import json
import re

from flask import Flask, request, jsonify, make_response
from flask import render_template

# creates a Flask application, named app
import lib_for_lol

app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html')


# this program razlozhenie
@app.route('/first', methods=['GET', 'POST'])
def first():
    if request.method == 'POST':
        mes = int(request.form['num'])
        lol = lib_for_lol.razl(mes)
        return render_template('first.html', lol=lol)
    else:
        return render_template('first.html')


# this programm number fibonacci
@app.route('/fibonacci', methods={'GET', 'POST'})
def fibonac():
    if request.method == 'POST':
        number = int(request.form['number'])
        answer = lib_for_lol.fibonacci(number)
        return render_template('fibonacci.html', answer=answer)
    else:
        return render_template('fibonacci.html')


# обмен-возврат
@app.route('/obmen_vozvrat', methods=['GET', 'POST'])
def obm_voz():
    if request.method == 'POST':
        price, mony = float(request.form['price']), float(request.form['mony'])
        answer = lib_for_lol.ob_vz(price, mony)
        return render_template('obmen_vozvrat.html', answer=answer)
    else:
        return render_template('obmen_vozvrat.html')


@app.route('/mortgage', methods=['GET', 'POST'])
def mortgage():
    if request.method == 'POST':
        annual_interest_rate, total_funds, loan_term_per_month = int(request.form['annual_interest_rate']), float(
            request.form['total_funds']), int(request.form['loan_term_per_month'])
        answer = lib_for_lol.monthly_payment(annual_interest_rate, total_funds, loan_term_per_month)
        return render_template('mortgage.html', answer=answer)
    else:
        return render_template('mortgage.html')


# не знаю почему это работает
@app.route('/ajax_test_calc')
def index1():
    return render_template('ajax_test_calc.html')


@app.route('/ajax_test_calc', methods=['POST'])
def ajax_test_calc():
    email = request.form['email']
    name = request.form['name']
    if name and email:
        newName = name
        return jsonify({'name': newName})
    return jsonify({'error': 'Missing Data!'})


@app.route('/test_request')
def test_request():
    return render_template('test_request.html')


@app.route('/test_request/create', methods=['POST'])
def create_empty():
    req = request.get_json()
    lol = make_response(jsonify(req))
    return render_template('test_request.html', {'lol': lol})


# перевод из двоичной системы в десятичную или наоборот
@app.route("/new_page", methods=['GET', 'POST'])
def new_page():
    return render_template("new_page.html")


@app.route("/new_page/create-entry", methods=['POST'])
def create_entry():
    req = request.get_json()
    number = req['number']
    selected_option = req['selected_option']
    answer = 0
    if selected_option == 0:
        answer = str(lib_for_lol.in_dec(number))
    elif selected_option == 1:
        answer = str(lib_for_lol.in_two(number))
    answer = {"answer": answer}
    response = app.response_class(
        response=json.dumps(answer),
        status=200,
        mimetype='application/json'
    )
    return response


# calculator
@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    return render_template("calculator.html")


@app.route("/calculator/calculator-entry", methods=["POST"])
def calculator_answer():
    req = request.get_json()
    resp = req["response"]
    pek = re.findall(r"[0-9]*[.,]?[0-9]+|\S", resp)
    j = 1
    aa = pek[0]
    while True:
        if pek[j] != '=':
            aa = lib_for_lol.calc(pek[j], float(aa), float(pek[j + 1]))
            j += 2
        else:
            answer = str(aa)
            answer = {"answer": answer}
            response = app.response_class(
                response=json.dumps(answer),
                status=200,
                mimetype='application/json'
            )
            return response


# this is method see json file
# @app.route('/test_json/open_json')
# def test_json_file():
#     return render_template('test.json')


# run the application


if __name__ == "__main__":
    app.run(debug=True)
