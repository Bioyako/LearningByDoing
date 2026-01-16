# def function_name(parameters)
# definition

def sum_two_ints(a:int, b;int) -> int:     # generic way to define a function; int and arrow are optionals
    """                 # Documentation 
    Returns the sum of two imput integers.

    Parameters:         # thinking your function as blocks
    - a (int)
    - b (int)

    Returns:
    int; a + b
    """
    return a+b              # this is the output of the function

# Function cacn also return more than one value
def double_and_duplicate(x: float) -> tuple[float, float] # multiple variable associated to the same thing (race) - fix number of things - tuple = an ordered pair of possibly multiple variables   
    """
    Double the input variable and return two copies of it.

    Parameters:   
    - x (float)

    Returns:
    Two copies of 2*x
    """
    return 2*x, 2*x

def print_hi():
    """
    Take no input and simply prints "Hi" to the console
    """
    print("Hi")
    # other things could happen here 
    # nothing ultimately gets returned by the function (any output)

def add_one(k :int) -> input:
    """
    Add one to the input variable and return the result.

    Parameters:
    - k (int)

    Returns:
    int: k+1
    """
    # when you see variable assignement (x + blah)
    # the left side of the equation
    # everything on the right innvolves values
    k = k+1
    return k
    # k has served its meaningful life (has been destroyed)

def main()
    """
    Special function that takes no inputs,produces no outputs,
    but that constitutes the runnable component of our program.
    """

def main():
    print("Functions in Python.")

    x = 3
    n = sum_two_ints(x, 4)
    print("Thee sum of 3 and 4 is", n)

    print(sum_two_ints(-2.1, 4.78))

    # type hints are just that; they are hints. 
    # You can still maybe do things that you might not intend 
    # due to Python's hyper-flexibility

    # identation is important - order is not important until it is important
    # the definition of a function can occcur in any order
    # BUT... when executions are executed, definitions must have already been encountered
    
    print(double_and_duplicate(2,7))

    print_hi()  # print something is not returning something

    # let's call add_one()
    m = 17
    print(add_one(m))

    # we are non changing the underlying value of m
    print("m is now:", m)

    # With basic types (str, int, float, etc.) Python uses "pass by value" =
    # When a variable is passed into a function as a parameter, a copy is created.
   
    # "Pass by reference" means that when you pass a variable
    # into a function, you can channge it! k m k m 

    #Python does use pass by reference for some things

    # All of this is not technically quite right (is not true for ALL the types - true for the types seen today)
    # Cool feature of Python


    # # # # # 


    def euclid_gcd(a: int, b:int) -> int:
        """
        Returns the GCD of two integers using Euclid's beautiful
        algorithm from over 2000 years ago.
        """

# the below says, run what is inside def main()
if __name__ == "__main__":
    main()