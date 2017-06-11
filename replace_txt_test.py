import re
text ='Hello how are you  # @ . ?!'

test = re.sub(r'[^a-zA-Z.,!?\']', ' ','Hello testing  # @ . ?!')
print(test)
print(list(set(text)))