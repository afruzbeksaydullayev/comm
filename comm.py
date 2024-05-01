import email
from colorama import Fore
import psycopg2


db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'test',
    'user': 'postgres',
    'password': '2008',
}


class DbConnect:
    def init(self, db_params):
        self.db_params = db_params

    def enter(self):
        self.conn = psycopg2.connect(**self.db_params)
        return self.conn

    def exit(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


with DbConnect(db_params) as conn:
    with conn.cursor() as cur:
        select_query = 'select * from persons'
        cur.execute(select_query)
        for row in cur.fetchall():
            print(row)


def print_response(message: str, RESET=None):
    print(Fore.BLUE + message + Fore.RESET)


class Person:
    def init(self,
                 id: int | None = None,
                 full_name: str | None = None,
                 age: int | None = None,
                 email: str | None = None, ):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.email = email


def insert_person():
    full_name = str(input('Enter your full name: '))
    age = int(input('Enter book your age : '))
    insert_into_query = "insert into persons(full_name, age, email) values (%s,%s);"
    insert_into_params = (full_name, age, email)
    cur.execute(insert_into_query, insert_into_params)
    conn.commit()
    print_response('INSERT 0 1')


def select_all_persons():
    select_query = 'select * from Person;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print_response(str(row))


def select_one_person():
    _id = int(input('Enter person id : '))
    select_query = 'select * from person where id = %s;'
    cur.execute(select_query, (_id,))
    person = cur.fetchone()
    if person:
        print_response('Person')
    else:
        print_response('No such person')


def update_person():
    select_all_persons()
    _id = int(input('Enter person id : '))
    full_name = str(input('Enter new full name : '))
    age = int(input('Enter new age : '))
    email = str(input('Enter new email : '))
    update_query = 'update person set name = %s, author = %s where id =%s;'
    update_query_params = (full_name, age, email, _id)
    cur.execute(update_query, update_query_params)
    conn.commit()
    print_response('Successfully updated person')


def delete_person():
    select_all_persons()
    _id = int(input('Enter person id : '))

    delete_query = 'delete from books where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Successfully deleted person')

    def create_table_query(Error=None):
        try:
            cur.execute(
                "Create table if not exist Persons (id serial primary key, full_name varchar(200) not null, age int , email varchar(200) example@gmail.com)")
            print("Table created successfully")
        except Error as e:
            print(f"Error creating table: {e}")



def menu():
    try:
        print('Insert person      => 1')
        print('Select all person  => 2')
        print('Delete person      => 3')
        print('Select one person  => 4')
        print('Update person      => 5')
        choice = int(input('Enter your choice : '))

    except ValueError as e:

        choice = -1

    return choice


def run():
    while True:
        choice = menu()
        match choice:
            case 1:
                insert_person()
            case 2:
                select_all_persons()
            case 3:
                delete_person()
            case 4:
                select_one_person()
            case 5:
                update_person()
            case _:
                break


if name == 'main':
    run()