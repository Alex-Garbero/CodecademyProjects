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
    def select_gear(self):
        gear_options = {
            'Camera: Lumix S5II': 2000,
            'Tripod: Peak Design Carbon Fiber Tripod': 600,
            'Lens: Panasonic Lumix S 85mm f/1.8': 600,
            'Bag: Peak Design Everyday Sling V2 (6L)': 120,
            'Camera Strap: Peak Design Slide': 70,
            'Camera Strap: Peak Design Cuff Camera Wrist Strap': 35
        }
        selected_gear = []
        
        print("Select gear options for the photoshoot. Enter 'done' when finished.")
        while True:
            print("Available gear options:")
            for gear, cost in gear_options.items():
                print(f"{gear.capitalize()}: ${cost}")
                
            gear_choice = input("Enter the gear option (or 'done' to finish): ").lower()

            if gear_choice == 'done':
                break

            if gear_choice in gear_options:
                selected_gear.append(gear_choice)
                print(f"{gear_choice.capitalize()} added to the selection.\n")
            else:
                print("Invalid choice. Please select a valid gear option.\n")


# How many photos? (Calculate hours of editing with this)
test = Data()
test.total_hours()
test.num_people()
test.select_gear()
