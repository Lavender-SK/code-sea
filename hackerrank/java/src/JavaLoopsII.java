import java.util.*;
import java.io.*;

public class JavaLoopsII {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i=0; i<t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            int item2 = b;
            int item1 = a;
            for(int j=0; j<n; j++){
                System.out.printf("%d ", item1 + item2);
                item1 = item1 + item2;
                item2 *= 2;
            }

            System.out.println();
        }
        in.close();
    }
}
