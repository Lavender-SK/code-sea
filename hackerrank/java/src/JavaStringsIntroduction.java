import java.io.*;
import java.util.*;

/**
 * The elements of a String are called characters.
 * The number of characters in a String is called the length, and it can be retrieved with the String.length() method.
 *
 * Given two strings of lowercase English letters, A and B, perform the following operations:
 *
 * Sum the lengths of A and B.
 * Determine if A is lexicographically larger than B (i.e.: does  come before  in the dictionary?).
 * Capitalize the first letter in A and B and print them on a single line, separated by a space.
 */
public class JavaStringsIntroduction {
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        System.out.println(A.length() + B.length());

        if(A.compareTo(B) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        char[] aChar = A.toCharArray();
        aChar[0] -= 32;

        char[] bChar = B.toCharArray();
        bChar[0] -= 32;
        System.out.printf("%s %s", String.valueOf(aChar), String.valueOf(bChar));

    }
}

// 首字母大写
//    public static String captureName(String name) {
//   //     name = name.substring(0, 1).toUpperCase() + name.substring(1);
////        return  name;
//        char[] cs=name.toCharArray();
//        cs[0]-=32;
//        return String.valueOf(cs);
//        
//    }
