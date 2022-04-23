from flask import Flask, render_template, request, session, make_response
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# cart1 = []

total = 0
db_sess = db_session.create_session()
ITEMS = {
    "turquoise_jacket": {
        "name": "Бирюзовая кофта",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/hoodie-with-zipper-2.jpg",
        "description": "Кофта с застежкой, сделанная из натурального хлопка и бережно отшитая швеями",
        "composition": "100% хлопок",
        "type": "hoodies",
        "id": "turquoise_jacket",
        "page": "hoodies/turquoise_jacket",
        "price": 60,
        "incart": 0
},
    "emoji_hoodie": {
        "name": "Худи с эмоджи",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/hoodie-with-logo-2.jpg",
        "description": "Худи с капюшоном, сделанное из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "hoodies",
        "id": "emoji_hoodie",
        "page": "hoodies/emoji",
        "price": 75,
        "incart": 0
    },
    "peachy_hoodie": {
        "name": "Персиковое худи",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/hoodie-2.jpg",
        "description": "Худи с капюшоном, сделанное из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "hoodies",
        "id": "peachy_hoodie",
        "page": "hoodies/peachy",
        "price": 75,
        "incart": 0
    },
    "turquoise_hoodie": {
        "name": "Бирюзовое худи",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/hoodie-green-1.jpg",
        "description": "Худи с капюшоном, сделанное из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "hoodies",
        "id": "turquoise_hoodie",
        "page": "hoodies/turquoise",
        "price": 75,
        "incart": 0
    },
    "blue_polo": {
        "name": "Голубое поло",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/polo-2.jpg",
        "description": "Голубое поло, сделанное из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "tshirts",
        "id": "blue_polo",
        "page": "tshirts/blue",
        "price": 60,
        "incart": 0
    },
    "white_tshirt": {
        "name": "Белая футболка",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/tshirt-2-460x460.jpg",
        "description": "Белая футболка, сделанная из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "tshirts",
        "id": "white_tshirt",
        "page": "tshirts/white",
        "price": 50,
        "incart": 0
    },
    "emoji_tshirt": {
        "name": "Футболка с эмоджи",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/t-shirt-with-logo-1.jpg",
        "description": "Футболка с эмоджи, сделанное из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "tshirts",
        "id": "emoji_tshirt",
        "page": "tshirts/emoji",
        "price": 55,
        "incart": 0
    },
    "peachy_tshirt": {
        "name": "Персиковая футболка",
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/vneck-tee-2.jpg",
        "description": "Персиковая футболка, сделанное из натурального хлопка и бережно отшитое швеями",
        "composition": "100% хлопок",
        "type": "tshirts",
        "id": "peachy_tshirt",
        "page": "tshirts/peachy",
        "price": 55,
        "incart": 0
    },
         }


@app.route('/')
@app.route('/index')
def index():
    page_name = "Домашняя страница"
    return render_template('index.html', name=page_name)


# @app.route("/session_test")
# def session_test():
#     visits_count = session.get('visits_count', 0)
#     session['visits_count'] = visits_count + 1
#     return make_response(
#         f"Вы пришли на эту страницу {visits_count + 1} раз")


@app.route('/process_data/', methods=['POST'])
def doit():
    global total
    item = request.form['index']
    # session.pop('user_cart', None)
    # session.pop('visits_count', None)
    user_cart = session.get('user_cart', [])
    # if "delete" in item and item[:-6] in session['user_cart']:
    #     item = item[:-6]
    #     session['user_cart'][item] = user_cart - 1
    #     total -= ITEMS[item]["price"]
    #     page = "../cart"
    # # elif item not in session['user_cart']:
    # #     session['user_cart'][item] = 1
    # #     total += ITEMS[item]["price"]
    # #     ITEMS[item]["incart"] += 1
    # #     page = "../" + ITEMS[item]["page"]
    # else:
    session['user_cart'] = user_cart + [item]
    total += ITEMS[item]["price"]
    ITEMS[item]["incart"] += 1
    page = "../" + ITEMS[item]["page"]
    print(session)
    # print(session)
    print(session["user_cart"])
    return render_template('redirect.html', page=page)


@app.route('/cart')
def cart():
    page_name = "Корзина"
    return render_template('cart.html', name=page_name, items=ITEMS, cart=session['user_cart'], total=total)


@app.route('/hoodies')
def hoodies():
    page_name = "Каталог кофт"
    return render_template('hoodies.html', name=page_name)


@app.route('/hoodies/turquoise_jacket')
def turquoise_jacket():
    item = ITEMS["turquoise_jacket"]
    page_name = item["name"]
    past = f"../hoodies"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/hoodies/emoji')
def emoji_hoodie():
    item = ITEMS["emoji_hoodie"]
    page_name = item["name"]
    past = f"../hoodies"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/hoodies/peachy')
def peachy_hoodie():
    item = ITEMS["peachy_hoodie"]
    page_name = item["name"]
    past = f"../hoodies"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/hoodies/turquoise')
def turquoise_hoodie():
    item = ITEMS["turquoise_hoodie"]
    page_name = item["name"]
    past = f"../hoodies"
    return render_template('product.html', item=item, name=page_name, past=past)

@app.route('/tshirts')
def tshirts():
    page_name = "Каталог футболок"
    return render_template('tshirts.html', name=page_name)


@app.route('/tshirts/blue')
def blue_polo():
    item = ITEMS["blue_polo"]
    page_name = item["name"]
    past = f"../tshirts"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/tshirts/white')
def white_tshirt():
    item = ITEMS["white_tshirt"]
    page_name = item["name"]
    past = f"../tshirts"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/tshirts/emoji')
def emoji_tshirt():
    item = ITEMS["emoji_tshirt"]
    page_name = item["name"]
    past = f"../tshirts"
    return render_template('product.html', item=item, name=page_name, past=past)


@app.route('/tshirts/peachy')
def peachy_tshirt():
    item = ITEMS["peachy_tshirt"]
    page_name = item["name"]
    past = f"../tshirts"
    return render_template('product.html', item=item, name=page_name, past=past)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    db_session.global_init("db/shop.db")
    # try:
    #     if not session.get('cart'):
    #         session['cart'] = []
    # except:
    #     pass
# print(session['cart'], total)
