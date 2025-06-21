

import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
//      StringBuffer sb1 = new StringBuffer();
//      StringTokenizer st = new StringTokenizer("");
        Stack<Integer> stack = new Stack<>();
        int n = sc.nextInt();
        for (int i = 0; i <= n; i++){
            String s = sc.nextLine();
            String cmd = s.split(" ")[0];
            switch (cmd) {
                case "push":
                    stack.push(Integer.parseInt(s.split(" ")[1]));
                    break;
                case "pop":
                    if (stack.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(stack.pop()).append("\n");
                    break;
                case "size":
                    sb.append(stack.size()).append("\n");
                    break;
                case "empty":
                    if (stack.isEmpty()) sb.append(1).append("\n");
                    else sb.append(0).append("\n");
                    break;
                case "top":
                    if (stack.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(stack.peek()).append("\n");
                    break;
            }

        }
        System.out.println(sb.toString());

    }

}
