#!/usr/bin/env python3

class Person:
    def __init__(self, name, email, phone, friends=[]):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = 0
        self.greeting_list = []

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person not in self.greeting_list:
            self.greeting_list.append(other_person)

    def print_contact_info(self):
        print("{name}'s email: {email}, {name}'s phone number: {phone}"
        .format(name=self.name, email=self.email, phone=self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print(len(self.greeting_list))

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)

class Truck(Vehicle):
    def __init__(self, make, model, year, wheels):
        super().__init__(make, model, year)
        self.wheels = wheels
