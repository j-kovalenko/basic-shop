from flask import Flask, render_template, request, session, make_response, redirect

import data.tshirts
from data import db_session
from data.hoodies import Hoodie
from data.tshirts import Tshirt
# from data.accessories import import Acc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/shop.db")


@app.route('/')
@app.route('/index')
def index():
    page_name = "Домашняя страница"
    # session.pop('cart', None)
    # session.pop('total', None)
    return render_template('index.html', name=page_name)


@app.route('/cart')
def cart():
    page_name = "Корзина"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    cart = session.get('cart', [])
    user_cart = []
    for it in cart:
        if it[1] == 'hoodies':
            item = db_sess.query(Hoodie).filter(Hoodie.name_id == it[0]).first()
        elif it[1] == 'tshirts':
            item = db_sess.query(Tshirt).filter(Tshirt.name_id == it[0]).first()
        user_cart.append(item)
    total = session.get('total', 0)
    # print(user_cart)
    return render_template('cart.html', name=page_name, cart=user_cart, total=total)


@app.route('/hoodies')
def hoodies():
    page_name = "Каталог кофт"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Hoodie)


@app.route('/<type>/<good>', methods=['POST', 'GET'])
def goods_page(type, good):
    db_session.global_init("db/shop.db")
    cart = session.get('cart', [])
    try:
        db_sess = db_session.create_session()
        if type == 'hoodies':
            item = db_sess.query(Hoodie).filter(Hoodie.name_id == good).first()
            page_name = item.name
        elif type == 'tshirts':
            item = db_sess.query(Tshirt).filter(Tshirt.name_id == good).first()
            page_name = item.name
    except AttributeError:
        return 'такого наименования нет'
    if request.method == 'GET':
        past = f"../{type}"
        return render_template('product.html', item=item, name=page_name, past=past, cart=cart)
    elif request.method == 'POST':
        # try:
        if request.form['action'] == 'add':
            cart = session.get('cart', [])
            cart += [[item.name_id, item.__table__.name]]
            session['cart'] = cart
            total = session.get('total', 0)
            total += item.price
            session['total'] = total
            # print(cart)
            print(session)
        if request.form['action'] == 'delete':
            cart = session.get('cart', [])
            if [item.name_id, item.__table__.name] in cart:
                cart.remove([item.name_id, item.__table__.name])
            else:
                return f"Товар {item.name} уже не в корзине"
            session['cart'] = cart
            total = session.get('total', 0)
            total -= item.price
            session['total'] = total
        # except Exception as e:
        #     print(e)
        return redirect(f'/{type}/{good}')


@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
        print('clicked')
        print(request.form['index'])
        testcart = session.get('testcart', [])
        session['testcart'] = testcart + ['d']
        print(session['testcart'])
        cart = session.get('cart', {})
        cart['testkey'] = 'testval'
        print(cart)

        session.pop('cart', None)
        # session.pop('testcart', None)
        return render_template('test.html')
    db_session.global_init("db/shop.db")
    # try:
    #     db_sess = db_session.create_session()
    #     if type == 'hoodies':
    #         item = db_sess.query(Hoodie).filter(Hoodie.name_id == good).first()
    #         page_name = item.name
    #     elif type == 'tshirts':
    #         item = db_sess.query(Tshirt).filter(Tshirt.name_id == good).first()
    #         page_name = item.name
    # except AttributeError:
    #     return 'такого наименования нет'
    # past = f"../{type}"
    # return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/tshirts')
def tshirts():
    page_name = "Каталог футболок"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Tshirt)


if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    app.run()
    db_session.global_init("db/shop.db")
    # print(Hoodie.__table__.name)
