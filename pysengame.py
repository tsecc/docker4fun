import sys

SYSMSG = "[SYSTEM]: "
def sys_msg(msg):
    print("[SYSTEM]: {}".format(msg))

class Room():
    desc = "This is a room, where the Py-Sen world begins."
    direction = () #東西南北

    def __init__(self, location):
        self.location = location

class User():
    desc = "You are an user, nothing else..."
    location_current = ()

    def __init__(self, id, name):
        self.id = id
        self.name = name


def welcome(User):
    print("\nHi {}, welcome to Py-Sen Game!\n".format(User.name))

def loc(User): print("Current location: {}".format(User.location_current))

def info(User):
    print("Your Name is {}\n".format(User.name))
    print("Information:  {}".format(User.desc))

def look(User):
    print(room.desc)

def exitgame(User):
    print("OK....bye!")
    sys.exit(0)

def helper(User):
    print("You can run following commands:")
    for cmd in action_dict.keys():
        print("{} ".format(cmd)),

def listener(user):
    action = ""
    readline = input("> ").split()
    print()

    if len(readline) == 0: sys_msg("Wait...You need to do SOMETHING!"); return
    else: command = readline[0]

    if command in action_dict:
        action = action_dict[command]
        action(user)
    else: sys_msg("Sorry what? What do you mean \"{}\" ?".format(command))

# ------------------------------------------------------------------------------
action_dict = {
    "loc": loc,
    "info": info,
    "exit": exitgame,
    "help": helper,
    "ls": look
}
# ------------------------------------------------------------------------------

login = False
user = User(1, "Freddy")
user.location_current = (0, 0)

while True:
    # Initialize environment for User
    if login == False:
        welcome(user)  # (TODO): Think about making a class for game_init
        room = Room(user.location_current)

        print(room.desc)

        login = True

    listener(user)