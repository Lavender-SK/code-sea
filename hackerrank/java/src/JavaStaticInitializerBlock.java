import java.util.*;


/**
 * Static initialization blocks are executed when the class is loaded, and you can initialize static variables in those blocks.
 *
 * It's time to test your knowledge of Static initialization blocks. You can read about it here.
 * https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html
 *
 * ref:
 * https://magiclen.org/hackerrank-java-static-initializer-block/
 * https://blog.csdn.net/qq_36522306/article/details/80584595
 */
public class JavaStaticInitializerBlock {
    private static int B = 0;
    private static int H = 0;
    private static boolean flag = true;

    static {
        Scanner sc = new Scanner(System.in);
        B = sc.nextInt();
        H = sc.nextInt();
        if(B <= 0 || H <= 0 ) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
            flag = false;
        }
    }

    public static void main(String[] args){
        if(flag){
            int area = B*H;
            System.out.print(area);
        }
    }
}
