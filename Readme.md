# Python OAIT Parser

## Цель

Задача заключалась в том, чтобы заполнить базу данных более настоящими и правдоподобными данными, чем с теми данными, которые генирируются при помощи ресурстов, как mockaroo или библиотек python на подобии faker.

База данных описывает предметную облатсь аренды девайсов и содержит такие сущности, как:

Пользователь, место самовывоза, девайс, арендованный девайс, цена, доставка и отзыв

С помощью парсера были заполнены таблицы пользователь, цена и отзыв.

Таблица доставок была заполнена при помощи парсера и генератора данных, другие таблицы были заполнены только генерирумыми данными

## Источники

[Dataset with user data](https://www.kaggle.com/datasets/jatinpanghal/media-consumption-and-mental-health?resource=download)

[Dataset with feedbacks](https://www.kaggle.com/datasets/parve05/customer-review-dataset)

[Dataset about used phones and its parameters](https://www.kaggle.com/datasets/ahsan81/used-handheld-device-data)

[Dataset about phones with price, brand, model and etc](https://www.kaggle.com/datasets/rkiattisak/mobile-phone-price)


## В результате алгоритма использованного в main.py, а также генераторов для сущностей
Получается команды на sql языке вида: 


INSERT INTO <table.name>(col1, col2, ..., coln)
VALUES (val1, val2, ..., valn);

Пример заполнения таблиц



