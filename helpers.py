import faker


def get_sign_up_date():
    fake = faker.Faker()
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return user_data
