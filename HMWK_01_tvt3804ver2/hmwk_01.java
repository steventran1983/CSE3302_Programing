// Tran, Thang
// 1001-233-804
// 2018-02-18

import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.Arrays;

public class hmwk_01 {

    public static void processToken(String token) {

        if (token.matches("^[0-9][0-9]+$")) {
            System.out.println(">" + token + "< matches INT.");
        } else if (token.matches("^[0-9]+[.][0-9]+$")) {
            System.out.println(">" + token + "< matches FD.");
        } else if (token.matches("^[A-Za-z_][a-zA-Z0-9_]+$")) {
            System.out.println(">" + token + "< matches ID.");
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