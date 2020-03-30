import java.util.Scanner;


public class JavaOutputFormatting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("================================");

        for(int i=0; i<3; i++){
            String s1 = sc.next();
            int x = sc.nextInt();

            // String s2 = "               ";
            // 在默认的情况下，数据是右对齐的，通过"-"标志可以改变对齐的方向。
            // d	整数型(10进制 )
            // s	String
            System.out.printf("%-15s%03d", s1, x );
            System.out.println();

        }
    }
}

