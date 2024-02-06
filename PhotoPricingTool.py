# Portrait Photography Pricing Tool:

class Welcome:
    def __init__(self):
        welcome_message = "Welcome to Alex's Photography Pricing tool!\n\n"
        print(welcome_message)

class Data:
    def __init__(self):
        pass
    def total_hours(self):
        print("Input the total time of the photoshoot in hours.\n")
        hours = input()
        print("Your photoshoot will last " + hours + " hours.\n")

# How many hours?
# How many people?
# What gear is needed?
# How many photos? (Calculate hours of editing with this)
test = Data()
test.total_hours()
