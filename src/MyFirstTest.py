username =  raw_input("please enter your name : ")

age = input("please enter your age : ")



while (1) :
    gender = raw_input("please enter your gender M/F : ")
    if gender == 'F' or gender == 'M' : break



weight = input("please enter your weight (kg) : ")

height = input("please enter your height (m) : ")

BMI = weight/(height*height)

print "Hello " + username + ", nice to meet you."

print "Here is your BMI :  %.2f "  %BMI

if BMI <18.5 : print "You have to gain more weight!"

elif BMI >24 : print "It's time to go on a diet!"

else : print "Congrats! You are in good shape."

