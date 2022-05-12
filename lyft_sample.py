#import requests

old_string = "iamyourlyftdriver"
new_string = ""
counter = 0


for char in old_string:
    counter+=1
    if counter % 3 == 0:
        new_string+=char
    else:
        pass

print(new_string)
#should print muydv
