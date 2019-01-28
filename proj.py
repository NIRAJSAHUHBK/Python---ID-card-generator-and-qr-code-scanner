from datetime import datetime
import random
import string
from PIL import Image,ImageDraw
import qrcode


def getqr(name,dob,department,adress,number,png):
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4)
    data=[]
    data.append(name)
    data.append(dob)
    data.append(department)
    data.append(adress)
    data.append(number)
    data.append(png)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image()
    img.save("E:\\rsizee.jpg")

    img2=Image.new('RGB',(300,200),color=(73,109,137))
    d=ImageDraw.Draw(img2)
    d.text((10,10),name,fill=(255,255,0))
    d.text((10,20),dob,fill=(255,255,0))
    d.text((10,30),department,fill=(255,255,0))
    d.text((10,50),number,fill=(255,255,0))
    d.text((10,40),adress,fill=(255,255,0))
    
    img2.save("E:\\id.png")   
    
def myImage():
    try:
        img=Image.open("E:\\hola.jpg")
        print(type(img))
        img.save("E:\\rsize.jpg") 
    except IOError:
        print("invalid file")
    return img
    
        
    
def nameValiddate(name1):
    while True:
        name=str(input(name1))
        if((name.isalpha())):
            break
        else:
            print("invalid name")
            print("enter again")
            continue
    return name

def departmentValiddate(name1):
    while True:
        name=str(input(name1))
        if((name.isalpha())):
            break
        else:
            print("invalid department")
            print("enter again")
            continue
    return name
        
def addressValiddate(name1):
    while True:
        name=str(input(name1))
        if((name.isalpha())):
            break
        else:
            print("invalid address")
            print("enter again")
            continue
    return name

def validate(dob):
    while True:
        i=input(dob)
        try:
            dt_start = datetime.strptime(i, '%d/%m/%Y')
        except ValueError:
            print ("Incorrect format")
            print("enter again")
            continue
        if(int(i[len(i)-4:len(i)])<=2002 and int(i[len(i)-4:len(i)])>=1995):
            break
        else:
            print ("IInvalid year")
            print("enter again")
            continue
    return i
             
            

def numValiddate(number1):
    while True:
        number=input(number1)
        if(number.isdigit() and len(number)==10):
            break
        else:
            print("invalid number")
            print("enter valid number")
            continue
    return number
        
class Student:
    def __init__(self,name,dob,department,adress,number,png):
        self.name=name
        self.dob=dob
        self.adress=adress
        self.number=number
        self.png=png
        
        
    
        
        
def randomID():
    i=0
    randomm = ''.join([random.choice(string.ascii_uppercase + string.digits+str(i)) for n in range(8)])
    i+=1
    return randomm

name=nameValiddate("enter the name of student ")
        
dob=validate("enter the date of birth in date/month/years format (DD/MM/YYYY) ")
    
department=departmentValiddate("enter the department ")
    
adress=addressValiddate("enter the address ")
    
number=numValiddate("enter the number (10 digit)")

name2="Name: "+name
dob2="DOB: "+dob
dep="Department: "+department
add="Address: "+adress
num="Phone Number: "+str(number)
rid=randomID()

png=myImage()
    
getqr(name2,dob2,dep,add,num,png)


obj=Student(name,dob,department,adress,number,png)


