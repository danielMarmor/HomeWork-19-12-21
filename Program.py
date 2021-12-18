import datetime
from User import User
from Car import Car
from DbRepository import DbRepository
from sqlalchemy import asc, desc, text
from db_cofig import local_session, create_all_entities
import sys


def main():
    try:
        create_all_entities()
        repo = DbRepository(local_session)

        # get all
        all_users = repo.get_all(User)
        all_cars = repo.get_all(Car)

        # get all  limit
        all_users_limit = repo.get_all_limit(User, 3)
        all_cars_limit = repo.get_all_limit(Car, 3)

        # add
        # user1 = User(id=10, username='Efrat', email='efrat@iec.co.il', date_created=datetime.date.today())
        # user2 = User(id=11, username='Shimshon', email='shimshon@iec.co.il', date_created=datetime.date.today())
        # user3 = User(id=12, username='Adina', email='adina@iec.co.il', date_created=datetime.date.today())
        # user4 = User(id=13, username='Doron', email='doron@iec.co.il', date_created=datetime.date.today())

        # repo.add(user1)
        # repo.add(user2)
        # repo.add_all([user3, user4])
        # updated_user_details = {'email': 'efrat-update@iec.co.il', 'date_created': datetime.now()}
        # repo.update_by_id(User, 'id', 10, updated_user_details)

        doron = repo.get_by_column_value(User, 'username', 'Doron')
        all_users = repo.get_by_column_like(User, 'email', 'shimshon')

        filters = {'date_created': datetime.date.today(), 'username': 'Adina'}
        efrat = repo.get_by_columns_values(User, filters)
        print(efrat)
        print(doron)
        print(all_users)

        user1 = User(id=20, username='Efrat', email='efrat@iec.co.il', date_created=datetime.date.today())
        user15 = User(id=15, username='Dandush', email='dandush@iec.co.il', date_created=datetime.date.today())

        # repo.add_with_vaild(User, user1, ['id', 'username'])
        repo.add_with_vaild(User, user15, ['id', 'username'])

    except Exception as e:
        print(f'Error! : {str(e)}')



main()






