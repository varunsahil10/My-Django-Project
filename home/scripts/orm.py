from home.models import *
from django.db import connection
import random
from pprint import pprint

def run():
    # delete_restaurant()
    # create_restaurant()

    # create_ratings()

    restaurant = Restaurant.objects.first()

    print(restaurant.ratings.all())

    pprint(connection.queries)
    print("Data Inserted Successfully")

def create_ratings():
    random_restaurants = get_random_restaurants()
    for restaurant in random_restaurants:
        print(restaurant)
        Rating.objects.create(restaurant=restaurant, rating=random.randint(1, 5))

def get_random_restaurants():
    return Restaurant.objects.order_by('?')[:10]  # Adjust the number to get the desired amount of random restaurants
def delete_restaurant():
    Restaurant.objects.all().delete()

def create_restaurant():
    Restaurant.objects.create(name='Pizza Hut', restaurant_type='Veg')
    Restaurant.objects.create(name='Dominos', restaurant_type='Veg')
    Restaurant.objects.create(name='KFC', restaurant_type='Non-Veg')
    Restaurant.objects.create(name='Subway', restaurant_type='Both')
    Restaurant.objects.create(name='Burger King', restaurant_type='Non-Veg')
    Restaurant.objects.create(name='McDonalds', restaurant_type='Both')
