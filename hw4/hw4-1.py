'''
    fn: get_user_input(message)
    Gets the user input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user
'''


def get_user_input(message):
    return input(message)


'''
    fn: validate_input_blank(message)
    Validate the user input basic case. Checks for the blank input.

    Parameters
    ----------
    arg1 : string
        message for the console

    Returns
    ---------
    string
        returns the input of the user after validation.

'''


def validate_input_blank(message):

    # Runs until the user inputs a non-blank value.
    while True:
        user_input = get_user_input(message)
        if user_input == '':
            print("Please do not leave the input blank")
        else:
            break
    return user_input


'''
    fn: main()
    Opens the file to generate the html for the data input by a user.
'''


def main():

    name = validate_input_blank("Enter your name:")
    description = validate_input_blank("Describe yourself:")

    html_tags = "<html> \n" \
                "<head> \n" \
                "</head> \n" \
                "<body> \n" \
                "\t<center> \n" \
                "\t\t<h1> " + name + "</h1> \n" \
                "\t</center> \n" \
                "\t<hr /> \n" \
                "\t" + description + "\n" \
                "\t<hr/> \n" \
                "</body> \n" \
                "<html>"

    file = open("home.html", "w")
    file.write(html_tags)
    file.close()


if __name__ == '__main__':
    main()
