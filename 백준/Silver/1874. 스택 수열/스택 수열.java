import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int top = 0;
        for (int i = 0; i < n; i++){
            int num = sc.nextInt();
            if (num > top) {
                for(int j = top+1; j <= num; j++){
                    stack.push(j);
                    sb.append("+").append("\n");
                }
                top = num;
            }else if (num != stack.peek()){
                System.out.println("NO");
                return;
            }
            stack.pop();
            sb.append("-").append("\n");
        }
        System.out.print(sb);
    }
}
