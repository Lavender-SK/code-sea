import java.io.*;
import java.util.*;

/**
 * "In computing, End Of File (commonly abbreviated EOF) is a condition in a computer operating system where no more data can be read from a data source."
 *
 * The challenge here is to read  lines of input until you reach EOF, then number and print all  lines of content.
 * Hint: Java's Scanner.hasNext() method is helpful for this problem.
 *
 *
 */
public class JavaEndOfFile {
    public static void main(String[] args){
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int num = 0;
        while(sc.hasNext()){
            String input = sc.nextLine();
            System.out.printf("%d %s%n", ++num, input);
        }
    }
}
