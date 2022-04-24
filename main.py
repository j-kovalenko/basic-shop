from flask import Flask, render_template, request, session, make_response
from data import db_session
from data.hoodies import Hoodie
from data.tshirts import Tshirt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

total = 0
# db_sess = db_session.create_session()


@app.route('/')
@app.route('/index')
def index():
    page_name = "Домашняя страница"
    return render_template('index.html', name=page_name)


@app.route('/cart')
def cart():
    page_name = "Корзина"
    return render_template('cart.html', name=page_name, items=ITEMS, cart=session['user_cart'], total=total)


@app.route('/hoodies')
def hoodies():
    page_name = "Каталог кофт"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Hoodie)


@app.route('/<type>/<good>')
def goods_page(type, good):
    db_session.global_init("db/shop.db")
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
    past = f"../{type}"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/tshirts')
def tshirts():
    page_name = "Каталог футболок"
    db_session.global_init("db/shop.db")
    db_sess = db_session.create_session()
    return render_template('section.html', name=page_name, db_sess=db_sess, sect=Tshirt)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    db_session.global_init("db/shop.db")
    print(Hoodie.__table__.name)
