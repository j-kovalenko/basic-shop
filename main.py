from flask import Flask, render_template, request, session, redirect
from data import db_session
from data.hoodies import Hoodie
from data.tshirts import Tshirt
from data.accessories import Acc
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/shop.db")


@app.route('/')
@app.route('/index')
def index():
    page_name = "Домашняя страница"
    return render_template('index.html', name=page_name)


@app.route('/cart2')
def cart2():
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    if request.method == 'GET':
        page_name = "Корзина"
        cart = session.get('cart', {})
        user_cart = []
        for it in cart:
            if cart[it]["type"] == 'hoodies':
                item = db_sess.query(Hoodie).filter(Hoodie.name_id == it).first()
            elif cart[it]["type"] == 'tshirts':
                item = db_sess.query(Tshirt).filter(Tshirt.name_id == it).first()
            elif cart[it]["type"] == 'accessories':
                item = db_sess.query(Acc).filter(Acc.name_id == it).first()
            user_cart.append(item)
        total = session.get('total', 0)
    return render_template('cart2.html', name=page_name, cart=user_cart, sess_cart=cart, total=total)


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    if request.method == 'GET':
        page_name = "Корзина"
        cart = session.get('cart', {})
        user_cart = []
        for it in cart:
            if cart[it]["type"] == 'hoodies':
                item = db_sess.query(Hoodie).filter(Hoodie.name_id == it).first()
            elif cart[it]["type"] == 'tshirts':
                item = db_sess.query(Tshirt).filter(Tshirt.name_id == it).first()
            elif cart[it]["type"] == 'accessories':
                item = db_sess.query(Acc).filter(Acc.name_id == it).first()
            user_cart.append(item)
        total = session.get('total', 0)
        return render_template('cart2.html', name=page_name, cart=user_cart, sess_cart=cart, total=total)
    elif request.method == 'POST':
        act = request.form['action'][-3:]
        resp = request.form['action'][:-3]
        if act == 'del':
            cart = session.get('cart', {})
            if cart[resp]["type"] == 'hoodies':
                item = db_sess.query(Hoodie).filter(Hoodie.name_id == resp).first()
            elif cart[resp]["type"] == 'tshirts':
                item = db_sess.query(Tshirt).filter(Tshirt.name_id == resp).first()
            elif cart[resp]["type"] == 'accessories':
                item = db_sess.query(Acc).filter(Acc.name_id == resp).first()
            total = session.get('total', 0)
            total -= item.price * cart[resp]["amount"]
            session['total'] = total
            if resp in cart:
                del cart[resp]
            else:
                return render_template("message.html", text=f"Товар {item.name} уже не в корзине")
            session['cart'] = cart
        if act == 'add':
            cart = session.get('cart', {})
            if cart[resp]["type"] == 'hoodies':
                item = db_sess.query(Hoodie).filter(Hoodie.name_id == resp).first()
            elif cart[resp]["type"] == 'tshirts':
                item = db_sess.query(Tshirt).filter(Tshirt.name_id == resp).first()
            elif cart[resp]["type"] == 'accessories':
                item = db_sess.query(Acc).filter(Acc.name_id == resp).first()
            if resp in cart:
                cart[resp]["amount"] += 1
                total = session.get('total', 0)
                total += item.price
                session['total'] = total
                session['cart'] = cart
            else:
                return render_template("message.html", text=f"Товар {item.name} уже не в корзине")
        if act == 'rem':
            cart = session.get('cart', {})
            if cart[resp]["type"] == 'hoodies':
                item = db_sess.query(Hoodie).filter(Hoodie.name_id == resp).first()
            elif cart[resp]["type"] == 'tshirts':
                item = db_sess.query(Tshirt).filter(Tshirt.name_id == resp).first()
            elif cart[resp]["type"] == 'accessories':
                item = db_sess.query(Acc).filter(Acc.name_id == resp).first()
            if resp in cart:
                cart[resp]["amount"] -= 1
                total = session.get('total', 0)
                total -= item.price
                session['total'] = total
                session['cart'] = cart
            else:
                return render_template("message.html", text=f"Товар {item.name} уже не в корзине")
        return redirect(f'/cart')



@app.route('/hoodies/')
@app.route('/hoodies')
def hoodies():
    page_name = "Каталог кофт"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Hoodie)


@app.route('/<type>/<good>', methods=['POST', 'GET'])
def goods_page(type, good):
    db_session.global_init("db/shop.db")
    cart = session.get('cart', {})
    try:
        db_sess = db_session.create_session()
        if type == 'hoodies':
            item = db_sess.query(Hoodie).filter(Hoodie.name_id == good).first()
            page_name = item.name
        elif type == 'tshirts':
            item = db_sess.query(Tshirt).filter(Tshirt.name_id == good).first()
            page_name = item.name
        elif type == 'accessories':
            item = db_sess.query(Acc).filter(Acc.name_id == good).first()
            page_name = item.name
    except AttributeError:
        return render_template("message.html", text='Такого наименования нет')
    if request.method == 'GET':
        past = f"../{type}"
        return render_template('product.html', item=item, name=page_name, past=past, cart=cart)
    elif request.method == 'POST':
        if request.form['action'] == 'add':
            cart = session.get('cart', {})
            cart[item.name_id] = {}
            cart[item.name_id]["type"] = item.__table__.name
            cart[item.name_id]["amount"] = 1
            session['cart'] = cart
            total = session.get('total', 0)
            total += item.price
            session['total'] = total
        if request.form['action'] == 'delete':
            cart = session.get('cart', {})
            if item.name_id in cart:
                del cart[item.name_id]
            else:
                return render_template("message.html", text=f"Товар {item.name} уже не в корзине")
            session['cart'] = cart
            total = session.get('total', 0)
            total -= item.price
            session['total'] = total
        return redirect(f'/{type}/{good}')


@app.route('/tshirts/')
@app.route('/tshirts')
def tshirts():
    page_name = "Каталог футболок"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Tshirt)


@app.route('/accessories/')
@app.route('/accessories')
def accessories():
    page_name = "Каталог аксессуаров"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Acc)


if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # serve(app)
