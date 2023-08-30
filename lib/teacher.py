#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        pass
    # class User:
    # pass  # Placeholder for the User class

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge

    def teach(self):
        return self.knowledge