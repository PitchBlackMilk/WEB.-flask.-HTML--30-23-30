from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    # Добавление капитана
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"

    user_1 = User()
    user_1.surname = "Scott"
    user_1.name = "Washington"
    user_1.age = 24
    user_1.position = "engineer"
    user_1.speciality = "search engineer"
    user_1.address = "module_2"
    user_1.email = "scott_washin@mars.org"
    user_1.hashed_password = "eng"

    user_2 = User()
    user_2.surname = "Nikolai"
    user_2.name = "Pirogov"
    user_2.age = 212
    user_2.position = "doctor"
    user_2.speciality = "surgeon"
    user_2.address = "module_3"
    user_2.email = "nik_pirn@mars.org"
    user_2.hashed_password = "doc"

    user_3 = User()
    user_3.surname = "Isaac"
    user_3.name = "Newton"
    user_3.age = 380
    user_3.position = "scientist"
    user_3.speciality = "physicist, mathematician, mechanic and astronomer"
    user_3.address = "module_4"
    user_3.email = "isaac@mars.org"
    user_3.hashed_password = "sci"

    db_sess.add(user)


if __name__ == '__main__':
    main()
