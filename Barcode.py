# Made by Isaiah Hamilton
from barcode import EAN13
from barcode.writer import ImageWriter

def generator(number):
    my_code = EAN13(number, writer=ImageWriter())
    my_code.save("bar_code")

if __name__ == "__main__":
    generator(input("Enter 12 Diget Number To Generate Bar Code: "))