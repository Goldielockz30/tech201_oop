# print(__name__)

# print("This is mod1's name -> " + __name__)

def main():
    # pass     # a key word statement which means none/null its just a placeholder
    print("This is mod1's name -> " + __name__)
if __name__ == "__main__": # the name cannot be imported it only runs this within the base file, it allows us to know when code is being ran by the current file or another file
    main()
    # to understand where the code is being run from and determine where you would want it to run
 # this helps you to have more control over what gets executed and what doesnt
