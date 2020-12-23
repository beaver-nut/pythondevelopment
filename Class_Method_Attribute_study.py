# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:25:00 2020

@author: Beaver
"""
class Box:

    # shared variable for all object create by this class
    color = 'green'

    # class method for object
    def __init__(self, width, height, dept):
        self.width = width
        self.height = height
        self.dept = dept

     # class method for object
    def getVolume(self,No_box=1):
        return self.width * self.height * self.dept*No_box

    @staticmethod
    def compare(a, b):
        if a.getVolume() > b.getVolume():
            return 'greater than'
        elif a.getVolume() == b.getVolume():
            return 'equal'
        else:
            return 'less than'
    def __del__(self):
        print("object deleted")

a = Box(2, 3, 4)
print(a.getVolume())
a.color="blue"
print(a.color)
del a
b = Box(1, 2, 5)

Box.color = 'red'

print('Box a volume = %d' % a.getVolume())
print('Box b volume = %d' % b.getVolume())

print('Box a color = %s' % a.color)
print('Box b color = %s' % b.color)

print('Box a volume a is %s box b' % Box.compare(a, b))