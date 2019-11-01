import json
from difflib import get_close_matches


def findword():
    with open("Dictdata.json", "r") as file:
        data = json.load(file)
        userinput = input("Enter the word to find the meaning: \n").lower()

        if userinput in data:
            print("Here is the result")
            return data[userinput]
        elif len(get_close_matches(userinput, data.keys())) > 0:
            print(f"Did you mean {get_close_matches(userinput, data.keys())[0]}?")
            # remember the array is outside parameters
            refactor = input("Type Y for Yes and N for No?\n").upper()
            if refactor == "Y":
                return data[get_close_matches(userinput, data.keys())[0]]
            elif refactor == "N":
                return "Exiting system"
            else:
                return "please choose a valid option"
        else:
            return "Word not found in the dictionary"


run = findword()
if type(run) == list:
    for i in run:
        print(i)
else:
    print(run)
