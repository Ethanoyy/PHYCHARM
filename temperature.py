def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5, 67, 32)")

def get_user_input():
    x = input()
    return x

def calc_average():
    num_list = get_user_input()
    total = sum(num_list)
    average = total / len(num_list)
    average2 = float(average)
    print("The average temperature is", "%.2f" % average2)

#def min_max():
    #num_list = get_user_input()
    #num_list.sort()
    #print("maximum is ", num_list[0])
    #print("minimum is ", num_list[-1])
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")
    display_main_menu()
    num_list = get_user_input()
    temperature = num_list.split(",")
    print(temperature)

if __name__ == "__main__":
    main()
    calc_average()
    #min_max()