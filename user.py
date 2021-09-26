from faker import Faker


class User(object):

    def __init__(self, email: str, first_name: str, last_name: str,
                 age: int, address: str, gender: str, job: str,
                 has_children_under_sixteen: bool):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.gender = gender
        self.job = job
        self.has_children_under_sixteen = has_children_under_sixteen

    def to_json(self) -> dict:
        return self.__dict__

    @staticmethod
    def generate_random_user():
        fake = Faker()
        fake_gender = fake.random_element(elements=('F', 'M'))
        fake_age: int = fake.pyint(min_value=12, max_value=75, step=1)
        fake_first_name = fake.first_name_female() if fake_gender == 'F' else fake.first_name_male()
        fake_last_name = fake.last_name_female() if fake_gender == 'F' else fake.last_name_male()
        return User(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake.email(),
            address=fake.address(),
            age=fake_age,
            job=fake.job(),
            gender=fake_gender(),
            has_children_under_sixteen=fake.pybool() if fake_age in (19, 60) else False
        )
