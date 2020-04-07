import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


/**
 * Given a string, s, and two indices, start and end,
 * print a substring consisting of all characters in the inclusive range from start to end-1.
 * You'll find the String class' substring method helpful in completing this challenge.
 *
 * https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-int-
 */
public class JavaSubstring {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();

        System.out.println(S.substring(start, end));
    }
}