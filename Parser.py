__author__ = 'Mina37'
#print('hello')




def comment(k):
    i = 1
    while i < len(k):
        if k[i] == '}' and  len(k[i+1:]) > 0:
            start(k[i+1:])
        i = i +1
    return


def inNum(k):
    i = 1
    while(k[i].isnumeric()):
        i = i+1
    if len(k[i:])>0:
        if k[i].isalpha():
            print(k[:i] + ' | Error')
        else:
            print(k[:i] + ' | Number')
        start(k[i:])

def inId(k):
    i = 1
    while(k[i].isalnum()):
        i = i + 1
    if len(k[i:])>0:
        if(k[:i] == 'if'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'then'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'else'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'end'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'repeat'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'until'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'read'):
            print(k[:i] + ' | Reserved')
        elif(k[:i] == 'write'):
            print(k[:i] + ' | Reserved')
        else:
            print(k[:i] + ' | Identifier')
        start(k[i:])

def inAssign(k):
    if k[1] == '=' and len(k) > 2:
        print(k[:2] + ' | Assign')
        start(k[2:])

def start(k):
    i = 0
    while (k[i] == ' ' or k[i] == '\t' or k[i] == '\r' or k[i] == '\n') and i < len(k):
        i = i + 1
        if(i>=len(k)):
            break
            return
    if i >= len(k) or len(k) == 0: #
        return
    elif(k[i] == '{'):
        comment(k[i:])
    else:
        if k[i].isnumeric():
            inNum(k[i:])
        elif k[i].isalpha():
            inId(k[i:])
        elif k[i] == ':':
            inAssign(k[i:])
        elif k[i] == '+' or k[i] == '-' or k[i] == '*' or k[i] == '/' or k[i] == '=' or k[i] == '<' or k[i] == '(' or k[i] == ')' or k[i] == ';':
            if(k[i] == '+'):
                print(k[i]+' | Plus')
            elif(k[i] == '-'):
                print(k[i] + ' | Minus')
            elif(k[i] == '*'):
                print(k[i] + ' | Multiplication')
            elif(k[i] == '/'):
                print(k[i] + ' | Division')
            elif(k[i] == '='):
                print(k[i]+ ' | Equals')
            elif(k[i] == '<'):
                print(k[i] + ' | Less Than')
            elif(k[i] == '('):
                print(k[i] +' | Opened Bracket')
            elif(k[i] == ')'):
                print(k[i] + ' | Closed Bracket')
            elif(k[i] == ';'):
                print(k[i] + ' | Semi')
            start(k[i+1:])

        #else:
         #   if(len(k) == 0):
         #       return
          #  else:
          #      start(k[i+1:])






s = input('Enter a file name you want to parse without extension')
print('File to be parsed: ' + s + '.tiny')
f = open(s+'.tiny')
cont = f.read()
print(cont[0])
start(cont)

