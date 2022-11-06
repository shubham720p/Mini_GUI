
from tkinter import *

root = Tk()

def getvals():
    print("form submitted")

    with open ("record.txt","a") as f :
            f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), foodDetailvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")


root.geometry("644x344")
root.title("shubham meals")
Label(root, text="Welcome to shubham meals", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
foodDetail = Label(root, text="foodDetail ")
paymentmode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
foodDetail.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
foodDetailvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()



nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
foodDetailentry = Entry(root, textvariable=foodDetailvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
foodDetailentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)


Button(text="Submit to shubham meals", command=getvals).grid(row=7, column=3)



root.mainloop()
