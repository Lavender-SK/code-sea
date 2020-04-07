import java.io.*;
import java.util.*;


/**
 * A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.(Wikipedia)
 */
public class JavaStringReverse {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        /* Enter your code here. Print output to STDOUT. */

        char[] aChars = A.toCharArray();
        boolean flag = true;

        for(int i=0; i<aChars.length; i++) {
            if(aChars[i] != aChars[aChars.length-1])
                flag = false;
                break;
        }

        if(flag)
            System.out.println("Yes");
        else
            System.out.println("No");

        // best solution
        // System.out.println( A.equals( new StringBuilder(A).reverse().toString()) ? "Yes" : "No" );

    }
}
