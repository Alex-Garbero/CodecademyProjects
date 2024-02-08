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
            1: 'Camera: Lumix S5II ($2000)',
            2: 'Tripod: Peak Design Carbon Fiber Tripod ($600)',
            3: 'Lens: Panasonic Lumix S 85mm f/1.8 ($600)',
            4: 'Bag: Peak Design Everyday Sling V2 (6L) ($120)',
            5: 'Camera Strap: Peak Design Slide: ($70)',
            6: 'Camera Strap: Peak Design Cuff Camera Wrist Strap: ($35)',
        }
        selected_gear = []
        
        # Instruct user
        print("Select gear for the photoshoot by typing the corresponding number and pressing ENTER. Type 'DONE' when finished.")
        # Infinite loop until break
        while True:
            print("\n Available gear options:")
            print("-------------------------")
            for num, option in gear_options.items():
                # Print options neatly
                print(f"{num} - {option}")
            
            print("\n Selected gear options:")
            print("------------------------")
            # Print selected gear options
            for item in selected_gear:
                print(item)
            
            # Prompt user to select from gear 
            print("\nEnter number here (or type 'DONE' to finish): ")
            gear_choice = input()

            if gear_choice.upper() == 'DONE':
                break
            
            # Check if the input is a valid gear number
            if gear_choice.isdigit() and int(gear_choice) in gear_options.keys():
                selected_gear.append(gear_options[int(gear_choice)])
            else:
                print("Invalid choice. Please enter a valid gear number.")

        print("\n Final selected gear options:")
        print("------------------------------")
        for item in selected_gear:
            print(item)

        # Print items from the dictionary that were not selected
        not_selected_gear = [value for key, value in gear_options.items() if value not in selected_gear]
        print("\n Available gear options not selected:")
        print("\n--------------------------------------")
        for item in not_selected_gear:
            print(item)

        



# How many photos? (Calculate hours of editing with this)
test = Data()
#test.total_hours()
#test.num_people()
test.select_gear()
