def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_min_max_temperature(num_list)
    cal_average_temperature(num_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")
    return 0
def get_user_input():
    x = input("Enter: ")
    input_list = x.split(",")
    num_list = input_list
    return num_list
def cal_average_temperature(num_list):
    average = sum(num_list)/len(num_list)
    print("Average temperature = " + average)
    return average
def calc_min_max_temperature(num_list):
    max_value = max(num_list)
    print("Maximum number is " + max_value)
    min_value = min(num_list)
    print("Minimum number is " + min_value)

if __name__ == "__main__":
    main()
