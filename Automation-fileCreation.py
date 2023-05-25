fileName=input('Enter your File Name:')
fileExtension=input('Enter your file Extension:')

filePath=f"{fileName}.{fileExtension}"
#Using f-strings makes it easier to concatenate variables and expressions within a string

with open(filePath,"w") as file:
    pass
print(f"File: {filePath} created Successfully :) ")

