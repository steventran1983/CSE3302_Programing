# Tran, Thang
# 1001-233-804
# 2018-03-10
#--------------------------------------------------
import re
import sys

#--------------------------------------------------
def processToken( token ) :

    isID = r"^[a-mN-Z_][n-zA-M0-9_]*$"
    isInt = r"^(0d|0D)[0-9]+$"
    isnotEFP = r"^[0-9]+$"
    isHexInt = r"^(0x|0X)[0-9a-fA-F]+$"
    isFP = r"^[0-9]+[\.][0-9]+$"
    isEFP = r"(([0-9]+\.)|(\.[0-9]+)|([0-9]+\.[0-9]+)|([0-9]+))([eE][-+]?[0-9]+)?$"

    if re.match(isID, token):
        print('>%s<  matches ID.' % token)
    elif re.match(isInt, token):
        print('>%s<  matches INT.' % token)
    elif re.match(isnotEFP,token):
         print('>%s<  does not match.' % token)
    elif re.match(isHexInt,token):
        print('>%s<  matches HEXINT.' % token)
    elif re.match(isFP, token):
        print('>%s<  matches FP.' % token)
    elif re.match(isEFP,token):
        print('>%s<  matches EFP.' % token)
    else:
        print('>%s<  does not match.' % token)

#--------------------------------------------------
def main() :
  fName = sys.argv[1]
  print( 'processing tokens from ' + fName + ' ...' )

  with open( fName, 'r' ) as fp :
    lines = fp.read().replace( '\r', '' ).split( '\n' )

  for line in lines :
    for token in line.split() :
      processToken( token )

#--------------------------------------------------
if ( __name__ == '__main__' ) :
  main()

#--------------------------------------------------
