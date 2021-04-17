// package ABC176;

import java.util.Scanner;

public class C {
    public static void main(String[] args) {
        Scanner sr = new Scanner(System.in);
        int N = sr.nextInt();
        long[] a = new long[N];
        long cnt = 0;
        long max = 0;

        for(int i = 0; i < N; i++) {
            a[i] = sr.nextInt();
        }

        for (int i = 0; i < N; i++) {
            max = Math.max(max, a[i]);
            cnt += max - a[i];
        }
        System.out.println(cnt);
    }
}
