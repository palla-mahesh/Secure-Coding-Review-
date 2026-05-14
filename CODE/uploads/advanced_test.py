import os

password = "root123"

user_input = input("Enter command: ")

eval(user_input)

exec("print('Dangerous Execution')")

os.system(user_input)