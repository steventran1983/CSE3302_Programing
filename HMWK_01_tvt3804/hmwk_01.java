// Tran, Thang
// 1001-233-804
// 2018-02-18

import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.Arrays;

public class hmwk_01{

    public static void processToken(String token) {
        int notInt = 0, notID = 0, notFP = 0;
        try {
            int temp_digit = Integer.parseInt(token);
            System.out.println(">" + token + "< matches INT.");
        } catch (NumberFormatException e) {
            notInt++;
        }

        if ((token.contains(".")) && (token.charAt(0) != '.')
                && (token.charAt(token.length() - 1) != '.')) {
            try {
                Float.parseFloat(token);
                System.out.println(">" + token + "< matches FD.");
            } catch (NumberFormatException e) {
                notFP++;
            }
        } else {
            notFP++;
        }

        if ((Character.isLetter(token.charAt(0))) || (token.charAt(0) == '_')) {
            for (int i = 0; i < token.length(); i++) {
                char tempChar = token.charAt(i);
                if ((!Character.isLetter(tempChar))
                        && (!Character.isDigit(tempChar)) && tempChar != '_') {
                    notID++;
                    break;
                } else if (i == token.length() - 1) {
                    System.out.println(">" + token + "< matches ID.");
                }
            }
        } else {
            notID++;
        }
        if (notFP != 0 && notID != 0 && notInt != 0) {
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
