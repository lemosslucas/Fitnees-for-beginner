import csv
import sys
import os

from validator_collection import validators, errors
from tabulate import tabulate

def main():
    print("Welcome to Fitness for beginner!")
    menu()

def clean_output():
    os.system('clear')

def menu():
    # storage the user option
    option = input("[1] = Register account\n[2] = Login Account\n[3] = Exit\n")
    if option == "1":
        register()
    elif option == "2":
        login()
    elif option == "3":
        # Close the progam with bellow error menssage
        sys.exit("Thank for using Fitness to beginner, development for Lucas Lemos")
    else:
        print("Invalid option, choise in [1,3]")
        menu()

def register():
    name = input("UserName: ")
    email = input("Email: ")
    # Verift if is a valid email
    try :
        valid = validators.email(email)
    except (errors.InvalidEmailError, errors.EmptyValueError):
        clean_output()
        print("Invalid Email!")
        register()
    # Verify if is a valid password
    password = input("Password: ")
    if len(password) < 8:
        clean_output()
        print("Invalid Password needs for minim 8 characters")
        register()
    # write in th file in a dict format
    with open("accounts.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "email", "password"])
        writer.writerow({"name": name, "email": email, "password": password})
    clean_output()
    print("Your account was register with sucess!\n")
    menu()

def login():
    # Storage the datas users
    email_user = input("Email: ")
    password_user = input("Password: ")
    # read the file
    with open("accounts.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, email, password = row
            #verify if is register in system
            if email_user == email and password_user == password:
                print("Login was sucessful!\n")
                final_menu(name)
    clean_output()
    print("Account not found !")
    menu()

def final_menu(name):
    option = input(f"\nHello @{name}\nChoise one of these options?\n[1] = Nutrition\n[2] = Training sheet\n[3] = Your Datas\n[4] = Back to principal menu\n")
    if option == "1" :
        nutrition(name)
    elif option == "2" :
        training_sheet(name)
    elif option == "3" :
        user_data(name)
    elif option == "4" :
        menu()
    else:
        print("Invalid, choise a number [1,4]")
        final_menu(name)

def nutrition(name):
    print("Inform the following data ")
    try:
        weight = int(input("Weight (kg): "))
        height = int(input("Height (cm): "))
        age = int(input("Age: "))
        gender = input("Gender (female/male): ")
    except ValueError:
        print("Invalid data")
        nutrition(name)
    # Calculaded IMC
    height_m = height / 100
    imc = weight/(height_m * height_m)
    imc = round(imc, 2)
    creatine = "3g to 5g"
    # Calculaded the metabolic basic
    if gender.lower() == "female" :
        metabolic = 655 + (9.6 * height) + (1.8 * weight) - (4.7 * age)
    elif gender.lower() == "male":
        metabolic = 66 + (13.7 * height) + (5 * weight) - (6.8 * age)
    metabolic = round(metabolic, 2)
    clean_output()
    print("Calculating your datas...")
    # save the datas in a file with user name
    with open(f"{name}.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["weight", "height", "age", "gender", "imc", "creatine", "whey", "metabolic"])
        writer.writerow({"weight": weight, "height": height, "age": age, "gender": gender, "imc": imc, "creatine": creatine, "whey": "30g", "metabolic": metabolic})

    option = input("Your data has been saved, do you want see? y/n ")
    if option == "y":
        user_data(name)
    elif option == "n":
        print("Back to menu!")
        final_menu(name)

def training_sheet(name):
    print("Choise one of famous gym atlet for open his training.")
    famous = input("[1] = Cbum\n[2] = Ronnie Coleman\n[3] = Arnold Schwarzenegger\n[4] = Matheus Artico\n")
    clean_output()
    # output with the site of training
    if famous == "1":
        print("The actualy legend of Bodybuilding, CBUM, With 5 Mr.Olypia. Discover his sheet in the link below")
        link = "https://www.hipertrofia.org/blog/2023/08/31/chris-bumstead-cbum/"
    elif famous == "2" :
        print("The Legend of Bodybuilding, GOAT, Ronnie Coleman. With 8 Mr.Olypia. Discover his sheet in the link below.")
        link = "https://www.hipertrofia.org/blog/2020/02/19/ronnie-coleman-biografia-treino-dieta-e-historia-no-fisiculturismo/"
    elif famous == "3" :
        print("The Legend of Bodybuilding, and the cinema, Arnold Schwarzenegger. With 7 Mr.Olypia. Discover his sheet in the link below.")
        link = "https://www.hipertrofia.org/blog/2018/04/10/treino-arnold-schwarzenegger/"
    elif famous == "4" :
        print("The biggest man of Belo Horizonte, Brazil. Only 16 years and 45 cm in arms. A incridible work in the gym. Check out his sheet below")
        option = input("[1] = Upper body (chest, shoulders, and triceps)\n[2] = Upper body (back, biceps, abdominal)\n[3] = Lower body\n")
        if option == "1":
            print("Upper body (chest, shoulders, and triceps) workout:")
            table = ["| Exercise                                     | Sets |","|----------------------------------------------|------|","| Flat bench press                             | 4    |","| Flyes + push-ups on the ground               | 3    |","| Chest flyes (3 sets of 30 reps) + plank      | 3    |","| French press with dumbbells                  | 3    |","| Triceps pushdown with W bar                  | 4    |","| Incline bench press + push-ups on the ground | 4/3  |"]
        elif option == "2":
            print("Upper body (back, biceps, abdominal) workout:")
            table = ["| Exercise                        | Sets |","|--------------------------------|------|","| Front pulldown                 | 4    |","| Neutral grip machine row       | 3    |","| Neutral grip front pulldown    | 4    |","| Bicep curls 21s                | 3    |","| Concentration curls            | 3    |","| Straight abdominal crunches    | 4    |"]
        elif option == "3":
            print("Lower body (all) workout:")
            table = ["| Exercise                     | Sets |","|------------------------------|------|","| Leg extension machine        | 4    |","| Leg Press                    | 4    |","| Squats                       | 4    |", "| Leg Press calf raises        | 4    |","| Lunges                       | 3    |","| Sumo squats                  | 3    |"]
        # print the sheet
        for row in table:
            print(row)
        final_menu(name)
    print(f"Click in the link for access {link}")
    final_menu(name)

def user_data(name):
    datas = []
    # tem que verificar se exite o arquivo
    try :
        # Open a file
        with open(f"{name}.csv", "r") as CSVfile:
            # A variable for storage the line of file
            reader = csv.reader(CSVfile)
            # input the line in the array
            for row in reader:
                datas.append(row)
    # Verify if the file exists
    except FileNotFoundError:
        clean_output()
        print("Your datas doesnt exist, go to nutrition area")
        final_menu(name)
    print("|Weight |Height|Age   |Gender  |Imc      |Creatine    |Whey   |Metabolic  |")
    print(tabulate(datas[1:], headers = datas[0], tablefmt= "pipe"))
    final_menu(name)

if __name__ == "__main__" :
    main()
