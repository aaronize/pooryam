# coding: utf-8


class Person(object):
    def __init__(self, name, age, gender, job):
        self._name = name
        self._age = age
        self._gender = gender
        self._job = job

    def do_action(self):
        pass


class Student(Person):
    def __init__(self, name, age, gender, score, job='student'):
        super(Student, self).__init__(name, age, gender, job)
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer.')
        if score < 0 or score > 100:
            raise ValueError('score must be 0~100.')
        self._score = score


class Screen(object):
    # 使用一个元组限制对象实例的字段
    __slots__ = ('_width', '_height')

    def __init__(self):
        self._width = None
        self._height = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # 只读属性
    @property
    def resolution(self):
        if self._width is None or self._height is None:
            raise ValueError('Plz assign values to width and height first.')
        return self._width * self._height

    def __str__(self):
        return 'Width: {}, Height: {}, Area: {}'.format(self._width, self._height, self.resolution)

    def __len__(self):
        length = 0
        if self._height is not None:
            length += 1
        if self._width is not None:
            length += 1

        return length


if __name__ == '__main__':
    s1 = Student('john', 20, 'male', 99)
    print 'score is:', s1.score
    s1.score = 100
    print 'score is:', s1.score

    print '-' * 60

    screen = Screen()
    screen.width = 16
    screen.height = 9
    print 'resolution is:', screen.resolution

    print screen
    print len(screen)

    # 由于__slot__限制不能随便给对象实例增加字段
    # screen._pixel = '960*1080'
    # print screen._pixel
