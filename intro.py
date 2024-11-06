name = "kendall"
last_name = "payne"
cohort = 52
is_active = True
print(name + last_name + str(cohort))

integer = 10 # Integer
float_num = 3.14 # Float
text = "Hello" #String
is_sunny = False # Boolean

#=====Type Conversion========
num = 9.75
print(int(num))# convert a float to an integer

age =25
print(str(age)) #convert an integer to a string

price = "19.99"
print(float(price)) # convert a string to a float, output:19.99

#Challenge
# Create some variables called name, last_name, age and show them in a print

print("Hello " + name + last_name + " you are " + str(age) + " years old.")

#or you can  do this
print(f"Hello, {name} {last_name}, you are {str(age)} years old.")

#====Operators=====
x = 5
y= 3

print(x+y) # addition
print(x-y) # subtraction
print(x*y) # multiplication
print(x/y) # division
print(x%y) # modulus
print(x**y) #exponents

#====Comparison Operators=====
a = 10
b = 5

print(a==b) #equal to
print(a != b) # not equal to
print(a>b) # greater than
print(a<b) # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

x = 5
y = 10
print(x > 3 and y < 15) # True, because both conditions are true
print(x > 3 or y > 15) # True in or only one has to be true
print(not(x > 3)) # false, not inverts the answer


#========Lists=====

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1]) # -1 goes to last element

# lists methods
fruits.append("grape") # adds grape to the list
print(fruits)

fruits.remove("banana") # removes banana from list
print(fruits)

print(fruits.pop(1)) # removes and prints item at index 1 "cherry"
print(fruits)

print(fruits.index("grape")) # returns index of grape
print(fruits.count("apple")) # returns how many times "apple" appears
      

      #====If statements=====

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

    x = 10

    if x > 10:
        print("x is greater than 1o")
    elif x == 10:
        print("x is equal to 10")
    else:
        print("x is less than 10")

        #====For Loops=====
for i in range(5):  # loop from 0 to 4
    print(i)    #indentation is important

    fruits = ["apple", "banana", "cherry"]  #fruits list

    for fruit in fruits:
        print(fruit)
        print (f"fruit: {fruit}")

        #==== Functions =====

        def greet():
            print("Hello from greet function")
        greet() # calls the function

        def say_hi(name):
            print("Hi, " + name)

        say_hi("Bruce")

        def comment_division():
            print("=============================") # can use to seperate sections in Terminal
            