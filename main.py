stdform = input('Enter a number in scientific notation: ').strip(" ")
output = stdform[0:stdform.find("x10^")] + "E" + stdform[stdform.find("^")+1::]
print(f"This number in E notation is {output}.")