from PIL import Image
import os
from PIL import ImageFilter
from PIL import Image



#Asking a user to choose from a list of images and then asking what they want to modify
def manipulate():
    while True:
        user_choice = input("Which image would you like to modify? (pic1, pic2, pic3?) ")
        usershow = Image.open(user_choice + ".jpg")
        usershow.show()
        user_confimation = input("Is this the correct image? (yes/no) ")
        if user_confimation == "yes":
            break



    choice = input("How would you like to modify your image (resize, png, bw, blur, or rotate) ")


    #the code to rotate an image
    if choice == "rotate":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.rotate(90).save('rotate/'+user_choice+'_rotate.jpg')
        pic2 = Image.open('rotate/'+user_choice+'_rotate.jpg')
        pic2.show()
        
    #the code to blur an image
    if choice == "blur":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.show()
        pic2 = pic1.filter(ImageFilter.BLUR)
        pic2.show()
        pic2.save('blur/' + user_choice + '_blur.jpg')

    #if you want to make an image black/white
    if choice == "bw":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.save('bw/' + user_choice + '_bw.jpg')
        pic2 = pic1.convert('L')
        pic2.show()

    #when you want to change the size of a picture
    if choice == "resize":
        newsize = (300, 300)
        pic1 = Image.open(user_choice + ".jpg")
        pic2 = pic1.resize(newsize)
        pic2.show

    # what to do if you want a picture in PNG format
    if choice == "png":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.save('png/' + user_choice + '_png.png')
        pic1.show()

manipulate()
second_round = input("do you want to restart, and manipulate another image? y/n: ")
if second_round == "y":
    manipulate()
else:
    print("Good bye")



 

 


