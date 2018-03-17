# Tran, Thang
# 1001-233-804
# 2018-02-18
# --------------------------------------------------
import re
import sys
# --------------------------------------------------


def processToken(token):

    isInt = r"^[0-9][0-9]*$"
    isFP = r"^[0-9][0-9]*[.][0-9]+$"
    isID = r"^[A-Za-z_][a-zA-Z0-9_]+$"
    if re.match(isInt, token):
        print('>%s<  matches INT' % token)
    elif re.match(isFP, token):
        print('>%s<  matches FP' % token)
    elif re.match(isID, token):
        print('>%s<  matches ID' % token)
    else:
        print('>%s<  does not match.' % token)
# --------------------------------------------------


def main():
    fName = sys.argv[1]
    #fName  = "inputdata.txt"
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
