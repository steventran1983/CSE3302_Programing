//Tran, Thang
//1001-233-804
//2018-03-10

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
    filename = "inputdata_02.txt";
    System.out.println( "processing tokens from " + filename + " ..." );

    try {
      Files.lines( Paths.get( filename ).forEachOrdered(
        line -> Arrays.stream( line.split( "\\s+" )  ))
            .forEachOrdered( token -> processToken( token ) ) );
    } catch ( java.io.IOException e ) {
      e.printStackTrace();
    }
  }
}
