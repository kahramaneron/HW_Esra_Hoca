

pw = input('define a password: ')

while len(pw)!=4 or pw.isdigit()!=True:
    print('TRY AGAIN WITH 4 DIGIT NUMBERS PLS!')
    pw=input('define a password: ')

print('your new pw is: ', pw)
