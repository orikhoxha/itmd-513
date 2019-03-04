import matplotlib.pyplot as plt
import os
import sys

'''
    This program reads the prices from the file entered by the user and uses matplotlib to plot a line chart showing the
    line in x and y axis for weekly gas average prices.

    Name: Orik Hoxha
    Class: ITMD 513

'''


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
    fn: read_prices_list(file_path)
    Reads the file. Gets the prices and convets them to number list.

    Parameters
    ----------
    file_path : string
        The file path to open



    Returns
    ---------
    list(float)
        returns a list of float.
'''


def read_prices_list(file_path):
    file_r = open(file_path, "r")
    prices_string = file_r.read().splitlines()
    lst_prices = [float(numeric_string) for numeric_string in prices_string]
    return lst_prices


'''
    fn: plot_line(x_weeks, y_prices)
    Plots the line chart with x and y axis.

    Parameters
    ----------
    x_weeks : list(float)
        The weeks of the prices.

    y_prices : list(float)
        The prices.

    Returns
    ---------
    void
'''


def plot_line(x_weeks, y_prices):
    plt.rcParams['figure.figsize'] = 10, 10

    plt.xlabel("Weeks")
    plt.ylabel("Prices in $")
    plt.title("Line plot of gas average prices per week.")

    plt.plot(x_weeks, y_prices)

    print("Plot showing")

    plt.show()


'''
    fn: main()
    Checks if the file path exists. Pulls out the list of prices from the file. Calls the
    plot method for displaying the line chart for weeks and their corresponding prices.

    Returns
    ---------
    void
'''


def main(file_path):
    print("Reading file %s" % file_path)
    if file_exists(file_path):
        prices_list = read_prices_list(file_path)
        if min(prices_list) < 0:
            print("Value %s" % min(prices_list) + " exists in the file.")
            print("List can only contain positive numbers.")
        else:
            num_weeks = len(prices_list)
            weeks = list(range(num_weeks))
            plot_line(weeks, prices_list)
    else:
        print("The file %s " % file_path + "doesn't exist")


if __name__ == '__main__':
    file_path = input("Enter file name: ")
    main(file_path)


