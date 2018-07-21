#!/usr/bin/env python3

from person import Person

class Student(Person):

    def __init__( self):
        Person.__init__(self)
        self.bafoeg=0

    def ausgeben(self):
        Person.ausgeben(self)
        print( "STUDENT:")

if __name__ == "__main__":
    
    s=Student()
    s.name="bauer"
    s.alter=7777777
    s.ausgeben()

