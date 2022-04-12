# File Handling -- Basic

# there are 3 points to be noted 

# 1. Source/ Destination dicrectory of this file

# 2. Mode --> Crete Mode, Write Mode, Append mode, read
# mode
# 1. create 'x' --> to create new file. raise FileExistError if the file already exist.
# 2. write 'w' 
# --> to add new/fresh content in the file
# --> create new file if the file doesn't exist
# --> removes or wipes all existing data/content or the file and adds all the new contents

# 3. append 'a' 
# --> to add new content after existing content of the file 
# --> creats new file if the file doesn't exist

# 4. read 'r'
# --> to read the content of the file
# --> raise error if the file doesn't exist

# example
# 1. single backslash

# open() --> this method takes two parameter 1. source/destination 2. mode

file = open("C:/Users/Heisenberg/Desktop/payment.txt", "r")
print(file.read()) # read() --> reads all the content of the file
file.close() # close() --> closes or destroy the file object
print("-------------------------------------")

# 2. double backslash

file_one = open("C:\\Users\\Heisenberg\\Desktop\\payment.txt", "r")
print(file_one.readline()) # readline() --> returns the file line of the file content if the method is executed for the first time
print(file_one.readline())
file.close()

# append 'a'
file_two = open("C:/Users/Heisenberg/Desktop/payment.txt", "a")
file_two.write("\nAppend test file.")
file_two.close()

# append 'a' if file doesnot exist
file_two = open("C:/Users/Heisenberg/Desktop/payments.txt", "a")
file_two.write("\nAppend test file.")
file_two.close()

# write 'w'
# file_two = open("C:/Users/Heisenberg/Desktop/payment.txt", "w")
# file_two.write("\nAppend test file.")
# file_two.close()

# write 'w' if file doesnot exist
file_two = open("C:/Users/Heisenberg/Desktop/paymentss.txt", "w")
file_two.write("\nAppend test file.")
file_two.close()

# create 'x'
# file_three = open("C:/Users/Heisenberg/Desktop/payment_payment.txt", "x")
# file_three.write("New file created")
# file_three.close

# raise FileExistError if the file already exist

# readlines()
# --> returns all data in list
print("--------------------")
file_four = open("C:\\Users\\Heisenberg\\Desktop\\payment.txt")
print(file_four.readlines())
file_four.close()

# readline() with parameter (int)
print("--------------------")
file_four = open("C:/Users/Heisenberg/Desktop/payment.txt")
print(file_four.readline(10))
print(file_four.readline(3))
file_four.close()
 
# 3. Methods --> open(), close(), read(), readline(), readlines(), write()

