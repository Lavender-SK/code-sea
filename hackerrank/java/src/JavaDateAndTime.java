import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * The Calendar class (https://docs.oracle.com/javase/7/docs/api/java/util/Calendar.html) is an abstract class
 * that provides methods for converting between a specific instant in time
 * and a set of calendar fields such as YEAR, MONTH, DAY_OF_MONTH, HOUR, and so on,
 * and for manipulating the calendar fields, such as getting the date of the next week.
 */
public class JavaDateAndTime {
    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */
    public static String findDay(int month, int day, int year) {
        // 获取日期对象
        String strDate = year + "-" + month + "-" + day;
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        Date date = null;
        try{
            date = format.parse(strDate);
        } catch (ParseException e) {

        }

        // 获取指定日期对象是周几
        SimpleDateFormat sdf = new SimpleDateFormat("EEEE", Locale.ENGLISH);
        String week = sdf.format(date);
        return week.toUpperCase();

        // return LocalDate.of(year, month, day).getDayOfWeek().name();
    }

    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = findDay(month, day, year);
        System.out.println(res);

        // bufferedWriter.write(res);
        // bufferedWriter.newLine();

        bufferedReader.close();
        // bufferedWriter.close();
    }
}
