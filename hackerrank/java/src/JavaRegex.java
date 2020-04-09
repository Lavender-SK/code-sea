import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;


/**
 * https://www.hackerrank.com/challenges/java-regex/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
 *
 * Write a class called MyRegex which will contain a string pattern.
 * You need to write a regular expression and assign it to the pattern such that it can be used to validate an IP address.
 * Use the following definition of an IP address:
 *
 * IP address is a string in the form "A.B.C.D", where the value of A, B, C, and D may range from 0 to 255.
 * Leading zeros are allowed. The length of A, B, C, or D can't be greater than 3.
 *
 * Some valid IP address:
 * 000.12.12.034
 * 121.234.12.12
 * 23.45.12.56
 *
 * Some invalid IP address:
 * 000.12.234.23.23
 * 666.666.23.23
 * .213.123.23.32
 * 23.45.22.32.
 * I.Am.not.an.ip
 */
public class JavaRegex {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }

    }
}


//Write your code here
class MyRegex {
    private static String zeroTo255 = "([0-9]{1,2}|(0|1)[0-9]{2}|2[0-4][0-9]|25[0-5])";
    public static final String pattern = zeroTo255 + "." + zeroTo255 + "." + zeroTo255 + "." + zeroTo255;
}
