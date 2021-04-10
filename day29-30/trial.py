from google_speech import Speech
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


speech = Speech("Yes","en")
speech.play()