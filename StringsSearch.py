#Chistian Byrd, Stephany Argueta, Shivani Rajendran
#Generic search for keywords or inputs

def file_name_search(input_string,input_file):

    file = open(input_file) #basic syntax for opening a file

    appearances = 0
    uppercase_apperances = 0

    for line in file:

        input_line = line
        input_line_split = []
        input_line_split = input_line.split(' ')
        alternate_case = []


        for i in input_line_split:
            current_word = i

            if i == input_string.lower():
                appearances += 1
            elif i.upper() == input_string.upper(): #This isn't quite how to do it, I'm sure
                uppercase_apperances += 1
                alternate_case.append(current_word)

    if uppercase_apperances == 0:
        print("Looking for " + str(input_string) + " it occurs " + str(appearances) + " times in the document and there were no uppercase variants.")
    else:
        print("Looking for " + str(input_string) + " it occurs " + str(appearances) + " times in the document and there were " + str(uppercase_apperances) +
            " uppercase variants of " + str(input_string))
        print(alternate_case)

        file.close()


while True:
    search_string = input("What string would you like to search for? ")
    search_file = input("What file are we looking in? ")

    file_name_search(search_string,search_file)

    try_again = input("Would you like to look for anything else? ")

    if try_again.lower() == "no":
        break




