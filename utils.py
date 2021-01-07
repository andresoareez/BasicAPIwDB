from models import People, Users


def insert_people(name, age):
    person = People(name=name, age=age)
    print(person)
    person.save()


def people_query():
    people = People.query.all()
    print(people)
    person = People.query.filter_by(name='name').first()
    print(person.age)


def people_change(name):
    person = People.query.filter_by(name=name).first()
    person.name = name
    person.save()


def people_delete():
    person = People.query.filter_by(name='name').first()
    person.delete()


def user_insert(login, password):
    user = Users(login=login, password=password)
    user.save()


def all_users_query():
    users = Users.query.all()
    print(users)


if __name__ == '__main__':
    user_insert('André', '12345')
    user_insert('Paulo', '54321')
    all_users_query()
    #people_delete()
