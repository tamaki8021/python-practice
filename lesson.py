import sys

from termcolor import colored

print('hi')

print(colored('test', 'red'))


print(sys.path)

print(__name__)


class Person(object):
    def __init__(self):
        print('First')

    def say_something(self):
        print('hello')

    def __del__(self):
        print('end')

person = Person()
person.say_something()

del person

print('############################')

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TestlaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, password='123'):
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.password = password

    # 読み取りだけ可
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # 条件に合う場合だけ書き込み可
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar('honda')
print(toyota_car.model)
toyota_car.run()

tesla_car = TestlaCar('Model S', password='456')
tesla_car.enable_auto_run = True
tesla_car.run()
tesla_car.auto_run()
print(tesla_car.enable_auto_run)

class p(object):

    kind = 'human'

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about {}'.format(year))

print(p.kind)
print(p.what_is_your_kind())

p.about(1900)

class Word(object):

    def __init__(self, text):
        self.text = text

    # 文字列時に呼ばれる
    def __str__(self):
        return 'Word!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word) :
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('test')
w2 = Word('test')

# len
print(len(w))

# add
print(w + w2)

# eq
print(w == w2)
