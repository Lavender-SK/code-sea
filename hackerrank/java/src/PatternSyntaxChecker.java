import java.util.Scanner;
import java.util.regex.*;


/**
 * https://www.hackerrank.com/challenges/pattern-syntax-checker/problem?h_r=next-challenge&h_v=zen
 *
 * Using Regex, we can easily match or search for patterns in a text.
 * Before searching for a pattern, we have to specify one using some well-defined syntax.
 *
 * In this problem, you are given a pattern.
 * You have to check whether the syntax of the given pattern is valid.
 *
 * Note: In this problem, a regex is only valid if you can compile it using the Pattern.compile method.
 * https://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#compile%28java.lang.String%29
 *
 * input:
 * 3
 * ([A-Z])(.+)
 * [AZ[a-z](a-z)
 * batcatpat(nat
 *
 * output:
 * Valid
 * Invalid
 * Invalid
 */
public class PatternSyntaxChecker {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while(testCases>0){
            String pattern = in.nextLine();
            //Write your code
            try{
                String test = "hello world";
                Pattern p = Pattern.compile(pattern);
                Matcher m = p.matcher(test);
                boolean b = m.matches();
                System.out.println("Valid");
            } catch (Exception e) {
                System.out.println("Invalid");
            }

            testCases--;
        }
    }
}




