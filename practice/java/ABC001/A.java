import java.util.*;

// package ABC001;

/**
 * A
 */
public class A {

    public static void main(String[] args) {
        Scanner sr = new Scanner(System.in);
        String[] S = sr.nextLine().split(" ");
        System.out.println(S[0].substring(0,1).toUpperCase() + S[1].substring(0,1).toUpperCase() + S[2].substring(0,1).toUpperCase());
    }
}
