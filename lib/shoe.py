#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9):
        self.brand = brand
        self.size = size
        

    @property
    def brand(self):
        '''The brand property'''
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        print(f"Setting brand to {brand}")
        self._brand = brand

    @property
    def size(self):
        '''The brand property'''
        return self._size
    
    @size.setter
    def size(self, size):

        if isinstance(size, int):
            print(f"Setting size to {size}")
            self._size = size

        else:
            print("size must be an integer")

    def cobble(self):
        '''Sets the condition after repair.'''
        self.condition = "New"
        print("Your shoe is as good as new!")
        


shoe = Shoe("Nike", 11)
shoe.brand = "Under Armour"
shoe.size = 8
shoe.cobble()
print(shoe.brand, shoe.size)