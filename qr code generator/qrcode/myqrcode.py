import qrcode 

from pyzbar.pyzbar import decode # pyzbar is a submodule from the pyzbar libary and decode is a function from this module

from PIL import Image # from the pillow libary we imported the image class

# for qr code generation 

def generate_code(input) :
    myqrcode=qrcode.make(input) # this creates an image object 
    myqrcode.save("code.png") # save the result in your actual folder
    print("check your folder the result is saved there, exactly in code.png")

# for qr code decoding 

def scan_code(input) :
    decoding=decode(Image.open(input)) # this will return a list of decoded objects, if the photo contains more than one qrcode it will return more than object in the list each object is for the decoded code 
    # print(decoding[0]) : this will print the raw datas of the object 
    # print(decoding[0].data) : this will print the data attribute of the object which is a binary data with the prefix b not string, see the github description to understand
    print(decoding[0].data.decode("ascii")) # see github description to understand why we used decode("ascii")


your_string = input("enter the string you want to transform into qr code : ")
generate_code(your_string)

the_scan= input("enter the image path you want to scan or the image name if the image is already saved in the code folder : ")
scan_code(the_scan)