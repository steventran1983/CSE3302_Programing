//Tran, Thang
//1001-233-804
//2018-03-10

import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.Arrays;

public class hmwk_02 {

    public static void processToken(String token) {

        if (token.matches("^[a-mN-Z_][n-zA-M0-9_]*$")) {
            System.out.println(">" + token + "< matches ID.");
        } else if (token.matches("^(0d|0D)[0-9]+$")) {
            System.out.println(">" + token + "< matches INT.");
        } else if (token.matches("[0-9]+$")) {
            System.out.println(">" + token + "< does not match.");
        } else if (token.matches("^(0x|0X)[0-9a-fA-F]+$")) {
            System.out.println(">" + token + "< matches HEXINT.");
        } else if (token.matches("^[0-9]+\\.[0-9]+$")) {
            System.out.println(">" + token + "< matches FP.");
        } else if (token.matches("(([0-9]+\\.)|(\\.[0-9]+)|([0-9]+\\.[0-9]+)|([0-9]+))([eE][-+]?[0-9]+)?$")) {
            System.out.println(">" + token + "< matches EFP.");
        } else {
            System.out.println(">" + token + "< does not match.");
        }
    }
    
    public static void main(String[] args) {
        System.out.println("processing tokens from " + args[0] + " ...");
        try {
            Files.lines(Paths.get(args[0])).forEachOrdered(
                    line -> Arrays.stream(line.split("\\s+"))
                            .forEachOrdered(token -> processToken(token)));
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }
    }
}
