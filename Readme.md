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

Пример заполнения таблиц:

![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/55da28ea-924c-4074-bb30-ec88cc93e047)

![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/40323cc7-48eb-4d96-8c30-20caf8936cd5)

![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/0765cae4-bb3d-4bee-be58-40c0dac8e352)


![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/113b18b8-1e55-4dcb-b4ac-3b21dab2c5ea)

![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/c12f8eca-4230-43da-9819-32a4df0be518)

![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/a77093e3-c4d8-47a4-9eff-ceff2e0acba1)

![image](https://github.com/JackBlack178/oait_parser_script/assets/71118110/0e899130-626c-4f06-8b71-81b73f7d1c4c)




