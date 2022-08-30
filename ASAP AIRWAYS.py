from tkinter import *
from tkinter.ttk import *

import mysql.connector as sql
from tkinter import scrolledtext
from PIL import ImageTk, Image
import random
from datetime import *
import tkinter.messagebox

mydb = sql.connect(host="localhost", user="root", passwd="98711", database='project')
mycursor = mydb.cursor()

window = Tk()
window.geometry('500x400')
window.title('ASAP Airways')

window.iconbitmap('C:/Users/pc/PycharmProjects/ASAP AIRWAYS/icon.ico')

# Photos
image = Image.open('C:/Users/pc/PycharmProjects/ASAP AIRWAYS/background header.png')
new_image = image.resize((500, 100))
image_ = ImageTk.PhotoImage(new_image)

image2 = Image.open('C:/Users/pc/PycharmProjects/ASAP AIRWAYS/background.jpg')
new_image2 = image2.resize((500, 300))
image2_ = ImageTk.PhotoImage(new_image2)

image3 = Image.open('C:/Users/pc/PycharmProjects/ASAP AIRWAYS/background.jpg')
new_image3 = image3.resize((500, 400))
image3_ = ImageTk.PhotoImage(new_image3)

#Styling
s=Style()
s.configure('.',font=('Times New Roman',12))
s.configure('my.TButton',font=('Helvetica',12),width=8)


def nav(x):
    if x == 'home':
        home.tkraise()
    if x == 'booking':
        booking.tkraise()
    if x == 'search':
        details.tkraise()
    if x == 'search1':
        search1.tkraise()
    if x == 'search2':
        search2.tkraise()
    if x == 'cancel':
        cancel.tkraise()


def clicked():
    nam = s1_e.get()
    no = s1_e2.get()

    T.config(state=NORMAL)  # Text is now editable
    T.delete(0.0, 'end')  # Delete the previous search

    mycursor.execute('select * from flight_details')
    t = False
    for i in mycursor:
        if nam == i[1] or no == str(i[0]):
            a = 'Id No.             :' + str(i[0]) + '\n' \
                'Name               :' + str(i[1]) + '\n' \
                'Age                :' + str(i[2]) + '\n' \
                'Gender             :' + str(i[3]) + '\n' \
                'Flight No          :' + str(i[4]) + '\n' \
                'Seat No            :' + str(i[5]) + '\n' \
                'Destination        :' + str(i[6]) + '\n' \
                'Date of Departure  :' + str(i[7]) + '\n' \
                'Time of Departure  :' + str(i[8])

            T.insert(INSERT, a)

            t = True
        else:
            pass
    if t == False:
        s1_l2.configure(text="Nothing Found")
    elif t == True:
        s1_l2.configure(text="Found")

    T.config(state=DISABLED)  # Text is now not editable

    clear()


def clicked1():
    name = s2_e.get()

    T1.config(state=NORMAL)  # Text is now editable
    T1.delete(0.0, 'end')  # Delete the previous search

    mycursor.execute('select * from flight_details')
    t = False
    for i in mycursor:
        if name == i[4]:
            T1.insert(INSERT, i)
            T1.insert(INSERT, '\n')
            t = True
        else:
            pass
    if t == False:
        s2_l2.configure(text="Nothing Found")


    elif t == True:
        s2_l2.configure(text="Found")


    T1.config(state=DISABLED)  # Text is now not editable

    clear()


def cancellation():
    a = str(c_e.get())
    b = str(c_e1.get())

    mycursor.execute('select * from flight_details')
    t = False
    for i in mycursor:
        if a == i[1] and b == str(i[4]):
            t = True
        else:
            pass

    if t == False:
        c_l2.configure(text='Booking Not Found')
    elif t == True:
        mycursor.execute('delete from flight_details where Name=%s and Flight_No=%s', (a, b))
        mydb.commit()

        c_l2.configure(text='Your Flight Has Been Cancelled')


def book():
    no = random.randint(100000, 999999)
    name = b_name.get()
    age = b_age.get()
    gender = b.get()
    gen = ''
    if gender == 0:
        gen = 'M'
    elif gender == 1:
        gen = 'F'
    flight = b_flight_number.get()
    seat = b_seat.get()
    dest = b_destination.get()
    dod = b_date_of_departure.get()
    tod = b_time_of_departure.get()

    if name != '' and age != '' and flight != '' and seat != '' and dest != '' and str(dod) != '' and tod != '':


        mycursor.execute("insert into flight_details(SNO,Name,Age,Gender,Flight_No"
                         ",Seat,Destination,Date_of_Departure,Time_of_Departure) "
                         "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(no,name,age,gen,flight,seat,dest,str(dod),tod))
        mydb.commit()
        message = tkinter.messagebox.showinfo(title='Seat Booked', message="Your Id No. is :"+str(no)+'\n Name :'+name)
    else:
        message1 = tkinter.messagebox.showerror(title='Error', message="Don't leave Any Fields Empty")
    clear()


def clear():
    # Clear Booking Page
    b_name.delete(first=0, last=END)
    b_age.set('')
    b.set(2)
    b_destination.set('')
    b_flight_number.set('')
    b_date_of_departure.set('')
    b_time_of_departure.set('')
    b_seat.set('')

    # Clear Search By Name Page
    s1_e.delete(first=0, last=END)
    s1_e2.delete(first=0, last=END)

    # Clear Search By Flight Page
    s2_e.delete(first=0, last=END)

    # Clear Cancellation Page
    c_e.delete(first=0,last=END)
    c_e1.delete(first=0,last=END)


home = Frame(window, height=400, width=500)
home.place(x=0, y=0)
booking = Frame(window, height=400, width=500)
booking.place(x=0, y=0)
details = Frame(window, height=400, width=500)
details.place(x=0, y=0)
search1 = Frame(window, height=400, width=500)
search1.place(x=0, y=0)
search2 = Frame(window, height=400, width=600)
search2.place(x=0, y=0)
cancel = Frame(window, height=400, width=500)
cancel.place(x=0, y=0)

# Home Page
h_canvas = Canvas(home, bg="Blue", height=100, width=500, highlightthickness=0)
h_canvas.place(x=0, y=0)
h_canvas.create_image(0, 0, image=image_, anchor=NW)


h_canvas2 = Canvas(home, bg="Brown", height=300, width=500, highlightthickness=0)
h_canvas2.place(x=0, y=100)
h_canvas2.create_image(0, 0, image=image2_, anchor=NW)

h_btn = Button(h_canvas2, text="Booking", command=lambda: nav('booking'))
h_btn.place(x=250, y=50, width=300, height=50, anchor="center")
h_btn2 = Button(h_canvas2, text="Flight Details", command=lambda: nav('search'))
h_btn2.place(x=250, y=100, width=300, height=50, anchor="center")
h_btn3 = Button(h_canvas2, text="Fight Cancellation", command=lambda: nav('cancel'))
h_btn3.place(x=250, y=150, width=300, height=50, anchor="center")

## Booking page
b_canvas = Canvas(booking, bg="Blue", height=400, width=500)
b_canvas.place(x=0, y=0)
b_canvas.create_image(0, 0, image=image3_, anchor=NW)

back_btn = Button(booking, text="Back", command=lambda: nav('home'),style='my.TButton')
back_btn.place(x=10, y=350)

#   Labels
Heading = Label(booking, text="BOOKING", font=('Times New Roman', 30), anchor="center")  # font=('font',size)
name = Label(booking, text='Enter your Name: ')
age = Label(booking, text='Enter your Age: ')
gender = Label(booking, text='Gender: ')
destination = Label(booking, text='Select Your Destination: ')
date_of_departure = Label(booking, text='Select Date of departure: ')
flight_number = Label(booking, text='Select Your Flight: ')
seat = Label(booking, text='Select Your Seat: ')
time_of_departure = Label(booking, text='Select Time of departure: ')

#   Label :Place
Heading.place(x=250, y=40, height=50, width=200, anchor='center')
name.place(x=29, y=80)
age.place(x=29, y=110)
gender.place(x=29, y=140)
destination.place(x=29, y=170)
date_of_departure.place(x=29, y=200)
flight_number.place(x=29, y=230)
seat.place(x=29, y=260)
time_of_departure.place(x=29, y=290)

#   Entry
b_name = Entry(booking)
b_age = Spinbox(booking, from_=0, to=100, state='readonly')

b = IntVar()
b.set(2)
b_gender1 = Radiobutton(booking, text='M', value=0, variable=b)
b_gender2 = Radiobutton(booking, text='F', value=1, variable=b)

flight = ["LT449", "TE417", "WB105", "CT415", "EV272", "JF221", "DA144", "BX113", "PA105", "UC281"]
flight_ = []
for i in range(random.randint(4, 8)):
    x = random.choice(flight)
    if x in flight_:
        pass
    else:
        flight_.append(x)
b_flight_number = Combobox(booking, state='readonly')
b_flight_number['values'] = flight_

seat_ = []
for i in range(random.randint(4, 20)):
    seat = str(random.randint(1, 9)) + random.choice("ABCD")
    if seat in seat_:
        pass
    else:
        seat_.append(seat)
b_seat = Combobox(booking, state='readonly')
seat_.sort()
b_seat['values'] = seat_

b_destination = Combobox(booking, state='readonly')
b_destination['values'] = ["Tokyo", "Seoul", "Mexico City", "New York City", "Mumbai", "Jakarta", "Sao Paulo", "Osaka",
                           "Shanghai",
                           "Hong Kong", "Los Angeles", "Kolkata", "Moscow", "Cairo", "London", "Beijing", "Tokyo",
                           "Seoul",
                           "Mexico City", "New York City", "Mumbai", "Jakarta", "Sao Paulo", "Osaka", "Shanghai",
                           "Hong Kong",
                           "Los Angeles", "Kolkata", "Moscow", "Cairo", "London", "Beijing", "Karachi", "Pune",
                           "Bangalore",
                           "Ahmedabad", "Jaipur", "Lucknow", "Bhopal", "Patna", "Vadodara", "Amritsar", "Chandigarh",
                           "Ranchi",
                           "Dehradun", "J&K", "Belgium", "Cape Town"]

b_date_of_departure = Combobox(booking, state='readonly')
b_date_of_departure['values'] = (date.today(),
                                 date.today() + timedelta(days=1),
                                 date.today() + timedelta(days=2),
                                 date.today() + timedelta(days=3),
                                 date.today() + timedelta(days=4),
                                 date.today() + timedelta(days=5),
                                 date.today() + timedelta(days=6),
                                 date.today() + timedelta(days=7))

time_ = []
for i in range(random.randint(4, 8)):
    time1 = random.randint(0, 23)
    time2 = random.choice(['30', '15', '45', '00'])
    timen = timedelta(hours=int(time1), minutes=int(time2), seconds=00)
    if timen in time_:
        pass
    else:
        time_.append(timen)
time_.sort()
b_time_of_departure = Combobox(booking, state='readonly')
b_time_of_departure['values'] = time_

book_btn = Button(booking, text="Book", command=book)

#   Entry: Place
b_name.place(x=190, y=80, width=144)
b_age.place(x=190, y=110)

b_gender1.place(x=190, y=140)
b_gender2.place(x=250, y=140)

b_destination.place(x=190, y=170)
b_date_of_departure.place(x=190, y=200)
b_flight_number.place(x=190, y=230)
b_seat.place(x=190, y=260)
b_time_of_departure.place(x=190, y=290)

book_btn.place(x=250, y=350, width=300, height=50, anchor="center")

# Details page

d_canvas = Canvas(details, bg="Green", height=400, width=500)
d_canvas.create_image(0, 0, image=image3_, anchor=NW)
Heading1 = Label(details, text="FLIGHT DETAILS", font=('Times New Roman', 30), anchor="center")  # font=('font',size)
d_btn = Button(details, text="Back", command=lambda: nav('home'),style='my.TButton')
searchn_btn = Button(details, text="Search By Name", command=lambda: nav("search1"))
searchf_btn = Button(details, text="Search By Flight Number", command=lambda: nav("search2"))

d_canvas.place(x=0, y=0)
Heading1.place(x=250, y=40, height=50, width=320, anchor='center')
d_btn.place(x=10, y=350)
searchn_btn.place(x=250, y=180, anchor='center', height=50, width=200)
searchf_btn.place(x=250, y=250, anchor='center', height=50, width=200)

# search by name

s1 = Canvas(search1, bg="yellow", height=400, width=500)
s1.place(x=0, y=0)
s1.create_image(0, 0, image=image3_, anchor=NW)

s1_heading = Label(s1, text="SEARCH BY NAME", font=('Times New Roman', 30), anchor="center")
s1_heading.place(x=240, y=40, height=50, width=355, anchor='center')

x_btn = Button(search1, text="Back", command=lambda: nav('search'),style='my.TButton')
x_btn.place(x=10, y=350)

s1_l = Label(search1, text="Enter Name")
s1_l.place(x=130, y=100)

s1_e = Entry(search1)
s1_e.place(x=240, y=100)

s1_l1 = Label(search1, text="Enter ID Number")
s1_l1.place(x=130, y=128)

s1_e2 = Entry(search1)
s1_e2.place(x=240, y=128)

s1_bt = Button(search1, text="Submit", command=clicked)
s1_bt.place(x=130, y=160)

s1_l2 = Label(search1, text="")
s1_l2.place(x=280, y=190, anchor="center")

T = scrolledtext.ScrolledText(search1, height=5, width=40)
T.insert(INSERT, "")
T.place(x=100, y=205)

# search by flight no.

s2 = Canvas(search2, bg="orange", height=400, width=500)
s2.place(x=0, y=0)
s2.create_image(0, 0, image=image3_, anchor=NW)

s2_heading = Label(s2, text="SEARCH BY FLIGHT NO.", font=('Times New Roman', 30), anchor="center")
s2_heading.place(x=250, y=40, height=50, width=450, anchor='center')
y_btn = Button(search2, text="Back", command=lambda: nav('search'),style='my.TButton')
y_btn.place(x=10, y=350)
s2_l = Label(search2, text="Enter Flight No.")
s2_l.place(x=130, y=100)
s2_e = Entry(search2)
s2_e.place(x=240, y=100)
s2_bt = Button(search2, text="Submit", command=clicked1)
s2_bt.place(x=130, y=150)

s2_l2 = Label(search2, text="")
s2_l2.place(x=280, y=185, anchor="center")

T1 = scrolledtext.ScrolledText(search2, height=5, width=50)
T1.insert(INSERT, "")
T1.place(x=250, y=250, anchor='center')

# cancellation page
c_canvas = Canvas(cancel, bg="red", height=400, width=500)
c_canvas.place(x=0, y=0)
c_canvas.create_image(0, 0, image=image3_, anchor=NW)

c_heading = Label(c_canvas, text="FLIGHT CANCELLATION", font=('Times New Roman', 30), anchor="center")
c_heading.place(x=250, y=40, height=50, width=455, anchor='center')
c_btn = Button(cancel, text="Back", command=lambda: nav('home'),style='my.TButton')
c_btn.place(x=10, y=350)

c_l = Label(cancel, text="Enter Name")
c_l.place(x=130, y=100)
c_l1 = Label(cancel, text="Enter Flight No.")
c_l1.place(x=130, y=150)

c_e = Entry(cancel)
c_e.place(x=240, y=100)
c_e1 = Entry(cancel)
c_e1.place(x=240, y=150)
c_bt = Button(cancel, text="Submit", command=cancellation)
c_bt.place(x=130, y=200)

c_l2 = Label(cancel, text="")
c_l2.place(x=280, y=250, anchor="center")

home.tkraise()
window.mainloop()
