#!/usr/bin/env python3

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
