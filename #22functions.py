
# CREATING FUNCTIONS
def functionname():
    #code
    a = 5
    b = 8
    print(f"A + B = {a + b}")

# CALLING FUNCTION
# functionname()


def returnsomething():
    return "Hello My Name Is Function"

a = returnsomething()
# print(a)

# PARAMETERS IN FUNCTION
def Add(num1,num2):
    return num1 + num2

print(Add("Hello World",", SAlman Khan"))

# Default Paramters
def AddFunc(num1=0,num2=0):
    return num1 + num2
print(AddFunc())