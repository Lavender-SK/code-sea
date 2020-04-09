import java.util.Scanner;

/**
 * https://www.hackerrank.com/challenges/java-anagrams/problem
 *
 * Two strings, a and b, are called anagrams if they contain all the same characters in the same frequencies.
 * For example, the anagrams of CAT are CAT, ACT, TAC, TCA, ATC, and CTA.
 *
 * Complete the function in the editor. If a and b are case-insensitive anagrams, print "Anagrams"; otherwise, print "Not Anagrams" instead.
 */
public class JavaAnagrams {

    static boolean isAnagram(String a, String b) {
        // Complete the function

        // step1: 字符串转数组
        char[] aChars = a.toLowerCase().toCharArray();
        char[] bChars = b.toLowerCase().toCharArray();

        // step2: 字符统计
        int[] aStats = new int[(int)'z'-(int)'a'+1];
        int[] bStats = new int[(int)'z'-(int)'a'+1];

        for(char aItem : aChars) {
            aStats[(int)aItem-(int)'a'] += 1;
        }

        for(char bItem : bChars) {
            bStats[(int)bItem-(int)'a'] += 1;
        }

        // step3: 判断 anagrams
        for(int i=0; i<aStats.length; i++){
            if(aStats[i] != bStats[i]) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
//        System.out.println((int)'A');
//        System.out.println((int)'Z');
//        System.out.println((char)91);
//        System.out.println((int)'a');
//        System.out.println((int)'z');
    }
}



