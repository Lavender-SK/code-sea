import java.io.*;
import java.util.*;

/**
 * https://www.hackerrank.com/challenges/java-string-tokens/problem?h_r=next-challenge&h_v=zen
 *
 * Given a string, s, matching the regular expression [A-Za-z !,?._'@]+,
 * split the string into tokens.
 * We define a token to be one or more consecutive English alphabetic letters.
 * Then, print the number of tokens, followed by each token on a new line.
 *
 * Note: You may find the String.split method helpful in completing this challenge.
 */
public class JavaStringTokens {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.

        // step1: 拆分
        String[] sSplit = s.split("[ !,?._'@]");


        // step2: 统计
        int num = 0;
        for(String token : sSplit) {
            if(token.length() != 0) {
                num += 1;
            }
        }

        // step3: 输出
        System.out.println(num);
        for(String token : sSplit) {
            if(token.length() != 0) {
                System.out.println(token);
            }
        }

        // 最佳答案
//        String[] tokens = s.split("[ !,?._'@]+");
//        System.out.println(tokens.length);
//        for(String token : tokens) {
//            System.out.println(token);
//        }

         scan.close();
    }
}
