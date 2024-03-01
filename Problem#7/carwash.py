'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = base_wash

    #type your code here
    output = ["ZyCar Wash", f"Base car wash - ${base_wash}"]

    if service_choice1 != '-':
        cost1 = services.get(service_choice1, 0)
        total += cost1
        output.append(f"{service_choice1} - ${cost1}")

    if service_choice2 != '-':
        cost2 = services.get(service_choice2, 0)
        total += cost2
        output.append(f"{service_choice2} - ${cost2}")

    output.append(f"-----")
    output.append(f"Total price: ${total}")

    # Print the captured output
    print("\n".join(output))

if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)