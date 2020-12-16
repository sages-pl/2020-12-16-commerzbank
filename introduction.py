from unittest import TestCase


class MyClass:
    def __init__(self, firstname=None, lastname=None):
        self.lastname = lastname
        self.firstname = firstname


class MyClassTest(TestCase):
    def test_create_instance(self):
        my = MyClass()
        self.assertIsInstance(my, MyClass)

    def test_init(self):
        my = MyClass('Mark', 'Watney')
        self.assertEqual(my.firstname, 'Mark')
        self.assertEquals(my.lastname, 'Watney')
