def main():
    print("Variables.")  # you can add comments to end of lines

    # Pythonn won't read this line!

    # Comment your code frequently :)

    # let's declare some variables
    j = 14      # int
    x = -2.3    # float
    yo_world = "Hi"     # str, this is snake_case
    statement = True    # bool variable 

    print(type(j), type(x), type(yo_world), type(statement))

    print(j, x, yo_world, statement)

    # Python uses dynamic typing (type of variable can change)
    yo_world = 2.718
    statement = "I hate Python :)"

    print(type(j), type(x), type(yo_world), type(statement))

    print(2*(j+5))
    print(x/4 +3.16)    # puculiarity of python operations

    # Python even alloes mixed type math
    print(x*j)

    print("After multiplication, j has typee", type(j))

    # we have threee additional operations
    print(14/3)     # 4.6666..
    print(14//3)     # this is integer division (4)
    print(14%3)      # this tells us the reminder (2)
    print(14**3)     # this gives us 14 to the power of 3

 
if __name__ == "__main__":
    main()