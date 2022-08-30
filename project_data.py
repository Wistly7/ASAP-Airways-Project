import random
import mysql.connector as sql

mydb = sql.connect(host="localhost", user="root", passwd="98711", database='project')
mycursor = mydb.cursor()

names = ["Lilian", "Julietta", "Kaila", "Miguel", "Ariane", "Dusti", "Malcom", "Dagmar", "Elnora", "Angila", "Starr",
         "Margy", "Dusty", "Jeanette", "Camie", "Tatyana", "Annett", "Shawanna", "Jaye", "Neomi", "Melody", "Alida",
         "Wm", "Melvin", "Flossie", "Leah", "Glennie", "Vito", "Jacinda", "Malissa", "Magali", "Alix", "Lin",
         "Carolann", "Damian", "Sanjuanita", "Roberta", "Karena", "Orlando", "Debbi", "Angeles", "Bill", "Grady",
         "Chara", "Gita", "Kareem", "Ilona", "Jim", "Marg", "Louetta", "Elois", "Delmy", "Sherrie", "Ludie",
         "Maragaret", "Thalia", "Fidela", "Emerita", "Rosio", "Darby", "Lekisha", "Alysa", "Lucio", "Rosalind", "Lorri",
         "Lupe", "Rodney", "Reita", "Shemeka", "Becki", "Jaimee", "Vernell", "Arlena", "Trenton", "Nohemi", "Eustolia",
         "Etsuko", "Glenn", "Yuriko", "Brigida", "Darrick", "Sherrell", "Natividad", "Agnes", "Yelena", "Lyndia",
         "Thea", "Suk", "Jonah", "Chantelle", "Pandora", "Adrian", "Katharyn", "Elaina", "Tammi", "Ivelisse", "Jo",
         "Alexa", "Pasquale", "Emilio"]
sur_names = ["Weiss", "Ritter", "Clements", "Pruitt", "Hutchinson", "Chandler", "Pham", "Frederick", "Christian",
             "Simpson", "Johnston", "Larsen", "Clark", "Schmidt", "Hester", "Zavala", "Lee", "Mathis", "Cherry",
             "Richards", "Gonzalez", "Stone", "Shea", "Thomas", "Castro", "Callahan", "Bush", "Dalton", "Bradshaw",
             "Mullins", "Alvarez", "Stein", "Leach", "Wall", "Fuller", "Mcneil", "Peters", "Elliott", "Blanchard",
             "Meadows", "Armstrong", "Shelton", "Mora", "Wilkerson", "Chang", "Dean", "Hicks", "Jefferson", "Compton",
             "Strong", "Roy", "Golden", "Nichols", "Horton", "Leblanc", "Giles", "Mcguire", "Rojas", "Kelly",
             "Mcdowell", "Barrera", "Hall", "Rodriguez", "Austin", "Reyes", "Crane", "Galvan", "Mccoy", "Chan", "Keith",
             "Kent", "Watson", "Stephens", "Reed", "Montes", "Cross", "Greer", "Morton", "Parsons", "Kirk", "Manning",
             "Lowe", "Mueller", "Wilkinson", "Cisneros", "Pratt", "Wilson", "Mendez", "Castillo", "Bonilla", "Howell",
             "Downs", "Floyd", "Esparza", "Lozano", "Mcbride", "Adams", "Whitaker", "Watts", "Montoya"]
flights = ["LT449","TE417","WB105","CT415","EV272","JF221","DA144","BX113","PA105","UC281"]
destinations = ["Tokyo", "Seoul", "Mexico City", "New York City", "Mumbai", "Jakarta", "Sao Paulo", "Osaka", "Shanghai",
                "Hong Kong", "Los Angeles", "Kolkata", "Moscow", "Cairo", "London", "Beijing", "Tokyo", "Seoul",
                "Mexico City", "New York City", "Mumbai", "Jakarta", "Sao Paulo", "Osaka", "Shanghai", "Hong Kong",
                "Los Angeles", "Kolkata", "Moscow", "Cairo", "London", "Beijing", "Karachi", "Pune", "Bangalore",
                "Ahmedabad", "Jaipur", "Lucknow", "Bhopal", "Patna", "Vadodara", "Amritsar", "Chandigarh", "Ranchi",
                "Dehradun", "J&K", "Belgium", "Cape Town"]

for i in range(20):
    seat = str(random.randint(1, 10)) + random.choice("ABCD")
    date1 = random.randint(1, 30)
    date2 = random.randint(1, 12)
    date3 = random.randint(2020, 2021)
    date = str(date3) + '-' + str(date2) + '-' + str(date1)
    time1=random.randint(0,23)
    time2=random.choice(['30','00'])
    time=str(time1)+time2+'00'
    name = random.choice(names) + " " + random.choice(sur_names)
    flight = random.choice(flights)
    destination = random.choice(destinations)
    age=random.randint(2,65)
    gender=random.choice(["M","F"])
    no=random.randint(100000,999999)

    # mycursor.execute("create table flight_details(SNO varchar(150),Name varchar(200),Age int(3),Gender enum('M','F'),Flight_No varchar(20),Seat varchar(10),Destination varchar(200),Date_of_Departure date,Time_of_Departure time)")
    mycursor.execute("insert into flight_details(SNO,Name,Age,Gender,Flight_No,Seat,Destination,Date_of_Departure,Time_of_Departure) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(no,name,age,gender,flight,seat,destination,str(date),time))

    mydb.commit()   #importance don't forget
# mycursor.execute('select * from flight_details where age<5')
# for i in mycursor:
#     # a=str(i[0])
#     print(i)

    # if i[-2].year<=2021:
    #     print(i)

    # if int(a[0])==5:
    #     print(i)

# print("Name         Airplane    Seat      To     date")
# print(name,flight,seat,destination,"(",date,")")
