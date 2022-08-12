class Human:
    """Людина має"""

    def __init__(self, first_name: str, last_name: str, date_birthday: int, gender: str):
        """Параметри людини"""
        self.first_name = first_name
        self.last_name = last_name
        self.date_birthday = date_birthday
        self.gender = gender
        self.energy = 100

    def human_eat(self):
        """Коли людина їсть енергія зростає"""
        self.energy += 5

    def human_sleep(self):
        """Коли людина спить енергія зростає"""
        self.energy += 10

    def human_talk(self):
        """Коли людина говорить енергія зменшуэтся"""
        self.energy -= 5

    def human_walk(self):
        """Коли людина ходить енергія зменшуэтся"""
        self.energy -= 10

    def human_do_home_work(self):
        """Коли людина робить домашку енергія зменшуэтся"""
        self.energy -= 90


# class Child(Human):
#     def __init__(self):
#         super().__init__(self.energy)
#         self.count = max(man_1.energy, man_2.energy, man_3.energy, woman_1.energy, woman_2.energy)



if __name__ == "__main__":

    man_1 = Human(first_name='Vasilyi', last_name='Groot', date_birthday=29, gender='Male')
    man_2 = Human(first_name='Roman', last_name='Pool', date_birthday=25, gender='Male')
    man_3 = Human(first_name='Serega', last_name='Pupkin', date_birthday=44, gender='Male')
    woman_1 = Human(first_name='Tonya', last_name='Rokojop', date_birthday=19, gender='Female')
    woman_2 = Human(first_name='Nata', last_name='Vernaja', date_birthday=28, gender='Female')

    man_1.human_eat(), man_1.human_sleep()
    man_2.human_sleep(), man_2.human_sleep()
    man_3.human_walk(), man_3.human_eat()
    woman_1.human_talk(), woman_1.human_sleep()
    woman_2.human_do_home_work(), woman_2.human_talk()



    print(man_1.first_name, man_1.last_name, man_1.date_birthday, man_1.gender, man_1.energy)
    print(man_2.first_name, man_2.last_name, man_2.date_birthday, man_2.gender, man_2.energy)
    print(man_3.first_name, man_3.last_name, man_3.date_birthday, man_3.gender, man_3.energy)
    print(woman_1.first_name, woman_1.last_name, woman_1.date_birthday, woman_1.gender, woman_1.energy)
    print(woman_2.first_name, woman_2.last_name, woman_2.date_birthday, woman_2.gender, woman_2.energy)

    '''Или можно'''
    print(man_1.__dict__)
    print(man_2.__dict__)
    print(man_3.__dict__)
    print(woman_1.__dict__)
    print(woman_2.__dict__)


    count = max(man_1.energy, man_2.energy, man_3.energy, woman_1.energy, woman_2.energy)

    if man_1.energy == count:
        print(f'Найбільше енергії лишилося: '
              f'{man_1.first_name, man_1.last_name, man_1.date_birthday, man_1.gender, man_1.energy}')
    elif man_2.energy == count:
        print(f'Найбільше енергії лишилося: '
              f'{man_2.first_name, man_2.last_name, man_2.date_birthday, man_2.gender, man_2.energy}')
    elif man_3.energy == count:
        print(f'Найбільше енергії лишилося: '
              f'{man_3.first_name, man_3.last_name, man_3.date_birthday, man_3.gender, man_3.energy}')
    elif woman_1.energy == count:
        print(f'Найбільше енергії лишилося: '
              f'{woman_1.first_name, woman_1.last_name, woman_1.date_birthday, woman_1.gender, woman_1.energy}')
    elif woman_2.energy == count:
        print(f'Найбільше енергії лишилося: '
              f'{woman_2.first_name, woman_2.last_name, woman_2.date_birthday, woman_2.gender, woman_2.energy}')