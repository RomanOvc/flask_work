# разложение числа на произведение простых
def razl(number):
    list = []
    while number % 2 == 0:
        number = number / 2
        list.append(2)
    while number % 3 == 0:
        number = number / 3
        list.append(3)
    while number % 5 == 0:
        number = number / 5
        list.append(5)
    while number % 7 == 0:
        number = number / 7
        list.append(7)
    if number % number == 0:
        list.append(int(number))
    if number / number == 1:
        list.append(1)
        return list


# число фибоначи
def fibonacci(num):
    k = []
    m = [0, 1]
    if num < 0:
        m = [0]
    else:
        for i in range(num):
            b = m[i] + m[i + 1]
            m.append(b)
    return m


# обмен возврат
def ob_vz(price, mony):
    itog = float(mony) - float(price)
    return float(round(itog, 3))


# Калькулятор для ипотеки
# monthly_interest_rate - размер месячной процентнйо ставки
# annual_interest_rate - Годовая процентная ставка
# monthly_payment - месячный платёжь
# total_funds - общая сумма средств
# loan term per month - срок займа в месяц
def monthly_payment(annual_interest_rate, total_funds, loan_term_per_month):
    mir = (annual_interest_rate / 100) / 12
    mp = total_funds * (mir / (1 - (1 + mir) ** (-loan_term_per_month)))
    return float(round(mp, 3))


"""Перевод числа из двоичной ситсемы в десятичную и из десятичной в двоичную"""


# в десятичную
def in_dec(two_number):
    list = []
    list1 = []
    if '.' in two_number:
        beforee = two_number.split('.')[:1]
        aftere = two_number.split('.')[1:]
        ii = int(len(beforee)) + 1
        for i in beforee:
            for iii in i:
                x = int(iii) * 2 ** ii
                list.append(x)
                ii -= 1
            answeri = sum(list)
        jj = -(int(len(beforee)))
        for j in aftere:
            for jjj in j:
                y = int(jjj) * 2 ** jj
                list1.append(y)
                jj += 1
            answerj = sum(list1)
        return answeri + answerj
    else:
        ii = int(len(two_number)) - 1
        for i in two_number:
            x = int(i) * 2 ** ii
            list.append(x)
            ii -= 1
        answer = sum(list)
        return answer


# в двоичную
def in_two(ten_number):
    resultb = []
    list1 = []
    if '.' in ten_number:
        before = ten_number.split('.')[:1]
        after = ten_number.split('.')[1:]
        for i in before:
            a = int(i)
            while a > 0:
                b = a % 2
                a = int(a / 2)
                resultb.append(str(b))
            answeri = ''.join(reversed(resultb))
        for j in after:
            w = float(j) / 10 ** len(after)
            i = 0
            while i < 4:
                w *= 2
                c = w % 2
                i += 1
                list1.append(str(int(c)))
            answerj = ''.join(list1)
        answer = answeri + '.' + answerj
        return answer
    else:
        a = int(ten_number)
        while a > 0:
            b = a % 2
            a = int(a / 2)
            resultb.append(str(b))
        answer = ''.join(reversed(resultb))
    return answer

# простой калькулятор
operations = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '-': lambda x, y: x - y,
}


def calc(operation, a, b):
    answer_predict = operations[operation](a, b)
    return answer_predict
