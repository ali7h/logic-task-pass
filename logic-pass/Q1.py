
def removechar(string):
    remove=str(input('enter the char you wanna to remove it from string : '))[:1]
    if remove not in string:
        print("this string doesn't have this character")

    return string.replace(remove,'')




mystr=str(input('enter the string: '))
print('the string befor remove  the char: '+mystr)
mystr=removechar(mystr)
print('the string after remove  the char: '+mystr)
