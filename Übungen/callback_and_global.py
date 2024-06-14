# var1 = [10, 23]
var2 = 20

# functions link a piece of code to a name
def var1():
    print("Hello SWD!")

function_reference = var1
print(function_reference)

# with () we can call an object --> python tries to "execute" the piece of code that's linked to this name
# since function_reference points to a callable function, this works:
function_reference()

# var2 is an integer object (non-callable) --> triggers an error
var2()


# to manipulate a global variable from inside a function, you need to use the global keyword
remaining_guesses = 10 

def test_function():
    global remaining_guesses
    remaining_guesses = 2 
    