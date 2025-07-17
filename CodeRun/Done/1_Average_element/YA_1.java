import java.util.Scanner;
import java.util.Arrays;
public class YA_1 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int len = 3;
        int[] a = new int[len];
        for (int i = 0; i < len; i++) {
            a[i] = scanner.nextInt();
        }
        scanner.close();
        Arrays.sort(a);
        System.out.println(a[1]);
        
    }
}
