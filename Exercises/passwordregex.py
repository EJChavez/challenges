# password checker
# at least 8 char long, any sort letters, numbers, $%#@, must end in a digit

import re
pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$!%*?&]{8,}\d$")

while True:
    password = input("please enter your password: ")
    passwordcheck = pattern.search(password)
    if passwordcheck:
        print('welcome to club penguin')
        break
    else:
        print('try again')
        continue
