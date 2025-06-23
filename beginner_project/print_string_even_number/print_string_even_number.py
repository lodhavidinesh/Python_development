# first get input from the user
# then string length for loop
# get event index 
# print even index string
user_input = input("Enter a string: ")
for i in range(len(user_input)):
    if i % 2 == 0:
        print(user_input[i])