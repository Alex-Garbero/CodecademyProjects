# Portrait Photography Pricing Tool:

class Welcome:
    def __init__(self):
        welcome_message = "Welcome to Alex's Photography Pricing tool!\n\n"
        print(welcome_message)

class Data:
    def __init__(self):
        pass

    # How many hours?
    def total_hours(self):
        print("Input the total time of the photoshoot in hours: ")
        hours = input()
        print("Your photoshoot will last " + hours + " hours.\n")

    # How many people?
    def num_people(self):
        print("How any people will be photographed?: ")
        people = input()
        print(people + " people will be photographed.\n")
# What gear is needed?
# How many photos? (Calculate hours of editing with this)
test = Data()
test.total_hours()
test.num_people()
