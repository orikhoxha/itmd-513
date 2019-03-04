import matplotlib.pyplot as plt
import random
import os
import sys

'''
    This program reads the expenses from the file entered by the user and uses matplotlib to plot a pie chart showing how
    you spend your money in percentage(%).

    Name: Orik Hoxha
    Class: ITMD 513

'''


'''
    fn: generate_random_color_hex()
    Generates a random hex color.


    Returns
    ---------
    string

'''


def generate_random_color_hex():
    return "#" + hex(int(str(random.uniform(0, 1))[2:]))[-6:].upper()



'''
    fn: get_category_colors(colors_num)
    Generates n number of colors for each of the categories.

    Parameters
    ----------
    arg1 : int
        Number of colors to be generated.

    Returns
    ---------
    list of strings.

'''


def get_category_colors(colors_num):
    colors = []
    for i in range(colors_num):
        colors.append(generate_random_color_hex())

    return colors


'''
    fn: get_next_row_file(file)
    Returns the next line from the file.

    Parameters
    ----------
    arg1 : file
        File to read the line from.

    Returns
    ---------
    list a string from the file row.

'''


def get_next_row_file(file):
    return file.readline()


'''
    fn: convert_string_to_list(string)
    Converts a string to a list.

    Parameters
    ----------
    string : string
        the string to be converted to a list.

    Returns
    ---------
    list
        returns a list of string split based on the space.
'''


def convert_string_to_list(string):
    list_converted = string.split()
    return list_converted


'''
    fn: convert_str_list_to_nr_list(list)
    Converts a string list to a number list. If it encounters an error on conversion, throws an exception.

    Parameters
    ----------
    list : list(strings)
        the string list to be converted to a number list.

    Returns
    ---------
    list or false
        returns the list if the conversion successful, otherwise returns false.
'''


def convert_str_list_to_nr_list(lst):
    try:
        lst = [float(numeric_string) for numeric_string in lst]
        return lst
    except ValueError:
        return False


'''
    fn: plot_pie(row_expense_float_list, expense_cagegories_list, colors)
    Plots the pie chart with the parameters supplied.

    Parameters
    ----------
    row_expense_float_list : list(number)
        The expenses extracted from the file.
    
    expense_cagegories_list : list(string)
        The categories extracted from the file.
    
    colors : list(string)
        The colors generated for each category.

    Returns
    ---------
    void
'''


def plot_pie(row_expense_float_list, expense_cagegories_list, colors):
    plt.pie(row_expense_float_list, labels=expense_cagegories_list, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


'''
    fn: file_exists(file)
    Checks if a file exists.

    Parameters
    ----------
    file : file
        The file to check if it exists.



    Returns
    ---------
    Boolean
        returns true if the file exists. Otherwise returns false.
'''


def file_exists(file):
    return os.path.isfile(file)


'''
    fn: main()
    Calls the methods for getting the categories, expenses and colors. If the file exists then it calls the method
    plot_pie to plot the pie with the data to be displayed.

    Returns
    ---------
    void
'''


def main(file_path):

    if file_exists(file_path):

        expenses_file = open(file_path, "r")

        expense_cagegories_list = convert_string_to_list(get_next_row_file(expenses_file))

        colors = get_category_colors(len(expense_cagegories_list))

        row_expense_string_list = convert_string_to_list(get_next_row_file(expenses_file))

        row_expense_float_list = convert_str_list_to_nr_list(row_expense_string_list)

        print("Reading file %s" % file_path)

        if min(row_expense_float_list) < 0:
            print("Value %s" % min(row_expense_float_list) + " exists in the file.")
            print("List can only contain positive numbers.")
        else:
            print(expense_cagegories_list)
            print(row_expense_float_list)

            plot_pie(row_expense_float_list, expense_cagegories_list, colors)

            expenses_file.close()

    else:
        print("The file %s " % file_path + "doesn't exist")


if __name__ == '__main__':
    file_path = input("Enter file name: ")
    main(file_path)


