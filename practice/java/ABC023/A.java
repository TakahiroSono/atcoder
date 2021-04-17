// package ABC023;

import java.util.*;

public class A {
    public static void main(String[] args) {
        Scanner sr = new Scanner(System.in);
        String S = sr.next();
        int num1 = Integer.parseInt( S.substring(0, 1));
        int num2 = Integer.parseInt( S.substring(1, 2));
        System.out.println(num1 + num2);
    }
}
