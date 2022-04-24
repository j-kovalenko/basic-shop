from data import db_session
from data.hoodies import Hoodie
from data.tshirts import Tshirt

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
        "image": "https://miakademi.com.tr/wp-content/uploads/2019/03/tshirt-2.jpg",
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

db_session.global_init("db/shop.db")
for clo in ITEMS:
    if ITEMS[clo]["type"] == "hoodies":
        item = Hoodie()
        item.name = ITEMS[clo]["name"]
        item.description = ITEMS[clo]["description"]
        item.image = ITEMS[clo]["image"]
        item.composition = ITEMS[clo]["composition"]
        item.name_id = ITEMS[clo]["id"]
        item.price = ITEMS[clo]["price"]
        db_sess = db_session.create_session()
        db_sess.add(item)
        db_sess.commit()
    elif ITEMS[clo]["type"] == "tshirts":
        item = Tshirt()
        item.name = ITEMS[clo]["name"]
        item.description = ITEMS[clo]["description"]
        item.image = ITEMS[clo]["image"]
        item.composition = ITEMS[clo]["composition"]
        item.name_id = ITEMS[clo]["id"]
        item.price = ITEMS[clo]["price"]
        db_sess = db_session.create_session()
        db_sess.add(item)
        db_sess.commit()