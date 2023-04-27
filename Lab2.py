def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")
    return 0
def get_user_input():
    x = input("Enter: ")
    input_list = x.split(",")
    num_list = input_list
    print(num_list)

def cal_average_temperature(num_list):
    return sum(num_list)/len(num_list)

def calc_min_max_temperature():

def sort_temperature():
def calc_median_temperature():

if __name__ == "__main__":
    main()
