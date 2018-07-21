#!/usr/bin/env python3

class PersonException( Exception):
    def __init__(self,m=""):
       self.m=m
       self.n=0

class Person(object):

    __slots__ = ( '__name', '__ort', "__alter")

    def __init__( self):
        self.__name=""
        self.__ort=""
        self.__alter=0

    def __getAlter(self): return self.__alter 
    def __setAlter(self,x): 
        if x <1 or x > 100: 
            raise( PersonException("FELER!!!!"))
            return
        self.__alter = x
    alter=property(__getAlter,__setAlter)

    def ausgeben(self):
        print()

if __name__ == "__main__":
    
    try: 
       p=Person()
       p.alter=7777777
       p.ausgeben()
    except PersonException as e:
       print("kkkk",e.m)
    except Exception as e:
       print("kkkk")
       

