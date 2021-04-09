#
# try:
#     file = open("a nonexistent file.txt")
# except FileNotFoundError as error_message:
#     print(error_message)
#     open("a nonexistent file.txt", "w")
# else:
#     content =file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("file was closed")
#
#     raise KeyError

height = float(input('Height: '))
weight = int(input("Weight: "))

if height>3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)