# this is a one line comment

"""
this is 
a
multi line
comment
"""

# there are two ways to run a python file (AKA module)
# 1. directly: e.g. python hello_world.py
# __name__ that when a module is run directly stores "__main__"

def main():
    print("hello CPSC 322")

if __name__ == "__main__":
    #run a main function or similar
    main()

print("hello CPSC 322")

#cmd + shift + p gives the comman pallette 