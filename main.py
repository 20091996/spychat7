print('Hello!') #print is a function in python to print whatever we want to
print('Let\'s get started')
input("What is your name?") #input is a function to input something from the spy
spy_name=input("What is your name?") #storing name in a variable called spy_name
print('Welcome ' + spy_name + '. Glad to have you back with us.') #symbol '+' used to join strings together.
spy_salutation=input("What should we call you (Mr. or Ms.)?") #Another variable to store the salutation
spy_salutation + " " + spy_name #We are joining the two strings together.
spy_name= spy_salutation + " " + spy_name #Variable re-assignment
print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')

###############################################module 2##############################################
spy_name=input("Welcome to spy chat, you must tell me your spy name first")
if len(spy_name) >0:  #if is used for condition
    #starting from here and seeing how this id under the if statement?
   print('Welcome ' + spy_name + ',Glad to have u back with us.')

   spy_salutation = input("Should i call u Mr. or Ms ?: ")

   spy_name= spy_salutation + " " + spy_name

   print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')
else:
    print("A spy needs to have a valid name.try again please.")
    spy_name=0 #initializing age with 0
    spy_rating=0.0 #initializing rating with 0
spy_age=int(input("What is your age?"))
if spy_age >12 and spy_age <50:
        spy_rating=int(input("What is your spy rating?"))
else:
        print('sorry you are not of the correct age to be a spy')

spy_rating=int(input("What is your spy rating?"))
if spy_rating > 4.5:
    print('Great ace!')
elif spy_rating >3.5 and spy_rating <=4.5:
    print('You are one of the good ones.')
elif spy_rating >2.5 and spy_rating <=3.5:
    print('You can always do better')
else:
    print('We can always use somebody to help in the office.')

print('Welcome to spychat '+ spy_salutation +' '+ spy_name + ' With age '+str(spy_age)+' and spy rating as '+ str(spy_rating)+'.')