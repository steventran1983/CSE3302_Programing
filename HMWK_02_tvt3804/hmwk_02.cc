# Tran, Thang
# 1001-233-804
# 2018-03-10

#include <iostream>
#include <fstream>

using namespace std;

void processToken( string token )
{
  // Replace the following line with your code to classify
  // the string in 'token' according to your Regular
  // Expressions and print the appropriate message.

  cout << ">" << token << "< is the proposed token.\n";
}

int main( int argc, char *argv[] )
{
  if ( argc > 1 ) {
    cout << "processing tokens from " << argv[ 1 ] << " ...\n";

    ifstream inputFile;
    string   token;

    inputFile.open( argv[ 1 ] );

    if ( inputFile.is_open() ) {
      for ( inputFile >> token; !inputFile.eof(); inputFile >> token ) {
        processToken( token );
      }
      inputFile.close();
    } else {
      cout << "unable to open " << argv[ 1 ] << "?\n";
    }
  } else {
    cout << "No input file specified.\n";
  }
}
