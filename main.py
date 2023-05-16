from faker import Faker
import random
import numpy as np
import xlrd
import numpy as np
import pandas as pd
import csv
import random
from random import randrange

users_size =  152
pickup_location_size = 303
price_size =  123
device_size =  876
rented_device_size = 514
feedback_size = 172
delivery_size = 459


def user_inserts():
    with open('users.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            email = row[1]
            username = row[2].replace(" ", "")
            phone_number = row[4]
            print(f"INSERT INTO USERS (username, phone, email) values ('{username}', '{phone_number}', '{email}');")



def price():
    with open('Mobile phone price.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            brand = row[0]
            model = row[1]
            myPrice = randrange(5, 20) + randrange(1, 10) / 10
            memory = row[2]
            ram = row[3]
            screenSize = row[4]
            frontCamera = row[5]
            batteryCapacity = row[6]
            has5G = bool(random.random()%2)
            rating = row[4]
            description  = f"Phone {brand} {model} costs {myPrice} dollars per month and has {rating} scores on the shop website. Android version: {random.random()%13 + 6}, screen_size: {screenSize}, 4g: Yes, 5g: {has5G}, rear_camera_mp: {frontCamera}, memory: {memory}, ram: {ram}, battery: {batteryCapacity} mAh, weight: {random.random() % 500} g and released day was in {random.random()%8 + 2015}"
            print(f"INSERT INTO price (brand, deviceName, description , price) values ('{brand}', '{model}', '{description }', '{myPrice}');")


def feedback():
    with open('feedaback_device.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            text = row[0]
            rating = randrange(1,5) + randrange(1,10) / 10
            date = row[3]
            user_id = randrange(users_size - 1) + 1
            rented_device_id = randrange(rented_device_size - 1) + 1
            print(f"INSERT INTO feedback (text, rating, date, user_id, rented_device_id) values ('{text}', '{rating}', '{date}', '{user_id}', '{rented_device_id}');")


def delivery():
    with open('delivers.sql', mode='r', encoding='utf-8') as infile, open('deliveers_final.sql', 'w', encoding='utf-8') as outfile:
        for line in infile:
            option = ''
            if (randrange(2)):
                option = f'Apt: {randrange(1, 157)}'
            else:
                option = f'Stage: {randrange(1, 27)}, Apt: {randrange(1, 157)}'
            line = line.replace("Apt:", option)
            outfile.write(line)

    infile.close()
    outfile.close()


if __name__ == "__main__":
    feedback()
    # price()
    # user_inserts()
    # pass



