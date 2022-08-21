

def count(string,char):
    print(f'the character "{char}" repeated {string.count(char)} times')


mystr=str(input('enter the string: '))
rep = str(input('enter the character you wanna to count it  : '))[:1]

count(mystr,rep)