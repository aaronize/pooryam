# coding: utf-8


class Employee:
    emp_count = 0
    emp_job = ''
    emp_info = []

    def __init__(self, name, salary, job):
        self.name = name
        self.salary = salary
        # 这里相当于定义了一个对象属性emp_job，通过实例调用，它和上面的类属性emp_job没啥关系
        self.emp_job = job

        # 给类属性赋值，通过类名调用
        Employee.emp_job = job
        # 类属性会绑定到类，emp_count每新建一个对象实例，都会自增1，达到计数的目的
        Employee.emp_count += 1

    @staticmethod
    def display_count():
        # 加上@staticmethod后self就没用了，如果加上会被当做一个参数
        # 访问类属性只能通过类名
        # 对象属性不能访问了
        print 'Total Employee: {}'.format(Employee.emp_count)

        # 静态方法中不能调用其他方法
        # Employee.display_employee()

    def display_employee(self):
        # print 'count in display_employee:', self.display_count()
        print 'Name: {}, Salary: {}'.format(self.name, self.salary)

    @classmethod
    def display_job(cls):
        # cls是类本身
        print 'Job is:{}'.format(cls.emp_job)

    @property
    def get_property(self):
        return 'properties: {}'.format(self.emp_job)


class Goods(object):

    def __init__(self):
        self.original_price = 100
        self.discount = 0.88

    @property
    def price(self):
        final_price = self.original_price * self.discount
        return final_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

    # 和@property
    # @price.getter
    # def price(self):
    #     return self.original_price


if __name__ == '__main__':
    emp = Employee('aaron', '100', 'engineer')
    emp.display_count()
    emp.display_employee()
    # print emp.emp_job
    emp.display_job()

    # 类名直接调用静态方法
    Employee.display_count()  # 1
    # 可以证明self是对象实例
    Employee.display_employee(emp)

    Employee.display_job()

    emp2 = Employee('Shawn', '200', 'Sales')
    emp.display_job()
    emp.display_count()  # 2

    # 属性的调用,直接调用不用()
    print emp.get_property
    print '-'*60

    gd = Goods()
    print 'price is ', gd.price
    gd.price = 200
    print 'price is ', gd.price
    # print 'price is ', gd.price

    del gd.price
    # 删除origin_price字段
    # print 'price is ', gd.price