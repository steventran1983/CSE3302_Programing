// Dalio, Brian A.
// dalioba
// 2018-03-09

import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.Arrays;

public class hmwk_02_skeleton {
  public static void processToken( String token ) {
    // Replace the following line with your code to classify
    // the string in 'token' according to your Regular
    // Expressions and print the appropriate message.

    System.out.println( ">" + token + "< is the proposed token." );
  }

  public static void main( String[] args ) {
    System.out.println( "processing tokens from " + args[ 0 ] + " ..." );

    try {
      Files.lines( Paths.get( args[ 0 ] ) ).forEachOrdered(
        line -> Arrays.stream( line.split( "\\s+" )  )
            .forEachOrdered( token -> processToken( token ) ) );
    } catch ( java.io.IOException e ) {
      e.printStackTrace();
    }
  }
}
