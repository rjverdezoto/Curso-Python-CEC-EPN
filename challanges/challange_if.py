space=" "
while True:
    x = input("Continue adding information (c/q)? ")
    if x == 'q' or x =="quit":
        break
    firstName=input("What is your first name? ")
    lastName=input("What is your last name? ")
    location=input("What is your current location? ")
    age=int(input("What is your age? ")) 
    
    print()
    print("Hi"+space+firstName+space+lastName+"."+space+"You are in"+space+location+space+"and you are"+space+str(age)+space+"years old")
    if(age > 0 and age < 25):
        print("You are so young")
    elif(age >= 25 and age < 40):
        print("You are young")
    elif(age >= 40):
        print("You are not so young anymore")
