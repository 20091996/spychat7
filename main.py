from spy_details import Spy, ChatMessage
from steganography.steganography import Steganography
from datetime import datetime
import csv

frnds_list = []

print "Welcome To Spychat"

def load_frnds():
    with open("friends.csv", "a") as friends:
        reader = csv.reader(friends)

        for row in reader:
            frnds_list.append(Spy(row[0], row[1], row[2], row[3]))


load_frnds()
def_name = raw_input("Would you like to continue with default  Spy profile? (y/n)")  ##whether the user wants a default name

if def_name.upper() == "N":
    name = raw_input("Choose Your SpyName")
    if len(name) > 0:

        salutation = raw_input("What should be your salutation Mr or Ms ") ##asking for salutation
        print "Alright %s.%s I'd like to know a little bit more about you..." % (salutation, name)

        age = int(raw_input("What is your age?")) ##asking other details

        # checking for spy eligibility
        if age in range(13, 51):
            rating = float(raw_input("Enter your rating."))
        else:
            print "Sorry you are not suitable to be a spy."
            exit()
        spy = Spy(name, salutation, age, rating)
    else:
        print "You have to enter your name to proceed."
        exit()
else:
    spy = Spy("singh", "Mr", 34, 3.3)

print '''\nWelcome %s.%s to the Spy Chat. So, you are %d old with a %.1f rating.
        ''' % (spy.salutation, spy.name, spy.age, spy.rating)

## displaying messages according to the ratings
if spy.rating > 4.5:
    print "According to your Spy Rating, You are a Pro!!!"
elif spy.rating > 3.5 and spy.rating <= 4.5:
    print "According to your Spy Rating, you are perfect!!!"
elif spy.rating >= 2.5 and spy.rating <= 3.5:
    print "According to your Spy Rating, You can do better."
else:
    print "Sorry, %s your rating is too low to be a spy." % spy.name
    exit()


def app_menu():
    show_menu = True
    current_status_message = None

    ## providing user with the menu options
    menu_choices = "Select the option. \n 1. Add a Status Update \n 2. Add a Friend \n 3. Send a Secret Message \n 4. Read a Secret Message \n 5. Read chats from a 'User' \n 6. Close application"
    while show_menu:
        choice = raw_input(menu_choices)
        if choice == "1":
            current_status_message = add_status(current_status_message)
        elif choice == "2":

            num_of_friends = add_friend()
            print "You have ", num_of_friends, " friends.\n"

        elif choice == "3":
            send_message()
        elif choice == "4":
            read_message()
        elif choice == "6":
            show_menu = False


status_updates = ["Hey, there!!", "Available", "Sleeping"] ##Setting status updates


def add_status(current_status_message):
    if current_status_message is None:
        print "You don't have any current status."
    else:
        print "Your current status message is " + '"' + current_status_message + '"'

    status_change = raw_input("Would you like to choose from old status updates?  (y/n)") ##displaying old status updates
    if status_change.upper() == "Y":
        j = 1
        for i in status_updates:
            print j, ". ", i
            j += 1
        status_num = int(raw_input("Select the position of the status from above list."))
        current_status_message = status_updates[status_num - 1]
        print '"' + current_status_message + '"', " is the current status message.\n"
        return current_status_message
    else:
        current_status_message = raw_input("Add the desired Status Message.")
        if len(current_status_message) > 0:
            print current_status_message, " is the current status message.\n"
            status_updates.append(current_status_message)
            return current_status_message
        else:
            print "Invalid status!!"


def add_friend():
    name = raw_input("Enter the friend's name.")
    salutation = raw_input("Salutation for friend's name.")
    age = int(raw_input("What's the friend's age?"))
    rating = float(raw_input("Enter the friend's rating."))
    # name = new_salutation + "." + new_name
    # chats = []
    # checking frnds's eligibility
    if len(name) > 0 and age in range(13, 51) and rating > spy.rating:

        friend = Spy(name, salutation, age, rating)
        with open("friends.csv", "a") as friends:
            writer = csv.writer(friends)
            writer.writerow([friend.name, friend.salutation, friend.age, friend.rating, friend.is_online])
        frnds_list.append(friend)
        print "Friend added!!"

    else:
        print "Sorry, your friend is not eligible to be a spy. \n"
    return len(frnds_list)


def select_a_friend():
    friend_num = 1
    for friend_name in frnds_list:
        print "%d. %s " % (friend_num, friend_name.name)
        friend_num += 1
    print "Enter the number of the respective friend from the above list: "
    return raw_input()


def send_message():
    receiver_friend = int(select_a_friend()) - 1
    image_path = raw_input("Enter the path/name of image: ")
    output_path = raw_input("Give the path/name for output: ")
    text = raw_input("Enter the message to send: ")
    Steganography.encode(image_path, output_path, text)
    present_time = datetime.now()
    chat = ChatMessage(text, True)
    with open("chats.csv", "a") as chats:
        writer = csv.writer(chats)
        writer.writerow([text, present_time, "Sent by "+spy.name])
    frnds_list[receiver_friend].chats.append(chat)

    print "Your secret message is ready. \n"


def read_message():
    sender_friend = int(select_a_friend()) - 1
    path = raw_input("Enter the path/name of the file: ")
    message = Steganography.decode(path)
    present_time = datetime.now()
    print "Your secret message is ready:\n"
    print message, "\n"
    chat = ChatMessage(message, False)
    with open("chats.csv", "a") as chats:
        writer = csv.writer(chats)
        writer.writerow([message, present_time, "Sent by "+frnds_list[sender_friend].name])
    frnds_list[sender_friend].chats.append(chat)


app_menu()
