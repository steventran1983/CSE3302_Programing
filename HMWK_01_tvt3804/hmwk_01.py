# Thang , Tran
# 1001233804
# 2018-02-17
# --------------------------------------------------
import re
import sys
# --------------------------------------------------

def processToken(token):
    # Handle the INT type
    notInt = notID = notFP = 0
    is_Interger = token
    if is_Interger.isdigit():
        print('>%s<  matches INT' %token)
    else:
        notInt = notInt + 1

    # Handle the ID type
    is_ID = token
    if is_ID[0].isalpha() is True or is_ID[0] == "_":
        for i in range(1, len(is_ID)):
            if is_ID[i].isalpha() is False and is_ID[i].isdigit() is False and is_ID[i] != "_":
                notID = notID + 1
                break
            elif i == len(is_ID) - 1:
                print('>%s<  matches ID' % is_ID)
    else:
        notID = notID + 1
    # Handle the IP type
    is_FP = token
    if "." in is_FP and is_FP[0] != "." and is_FP[0].isdigit() is True and int(is_FP[0]) > 0 \
            and is_FP[len(is_ID)-1] != "." and is_FP.replace('.', '', 1).isdigit():
            print('>%s<  matches FP' % is_FP)
    else:
        notFP = notFP + 1

    if notID != 0 and notFP != 0 and notInt != 0:
        print('>%s<  does not match.' % token)
# --------------------------------------------------

def main():
    fName = sys.argv[1]
    # fName  = "inputdata.txt"
    print('processing tokens from ' + fName + ' ...')
    with open(fName, 'r') as fp:
        lines = fp.read().replace('\r', '').split('\n')
    for line in lines:
        for token in line.split():
            processToken(token)
# --------------------------------------------------

if (__name__ == '__main__'):
    main()

# --------------------------------------------------
