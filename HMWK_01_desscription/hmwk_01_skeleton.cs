// Dalio, Brian A.
// 1000-123-456
// 2018-02-10

using System;
using System.IO;
using System.Text.RegularExpressions;

public class hmwk_01
{
  static public void processToken( string token ) {
    // Replace the following line with your code to classify
    // the string in 'token' according to your three Regular
    // Expressions and print the appropriate message.

    Console.WriteLine( ">" + token + "< is the proposed token." );
  }

  static public void Main( string[] args )
  {
    Console.WriteLine( "processing tokens from " + args[ 0 ] + " ..." );

    foreach ( string line in File.ReadAllLines( args[ 0 ] ) ) {
      foreach ( string token in line.Split( (char []) null, StringSplitOptions.RemoveEmptyEntries ) ) {
        processToken( token );
      }
    }
  }
}
