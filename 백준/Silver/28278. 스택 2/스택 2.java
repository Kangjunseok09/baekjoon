import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            String[] parts = s.split(" ");

            int num = Integer.parseInt(parts[0]);
            switch (num) {
                case 1:
                    stack.push(Integer.parseInt(parts[1]));
                    break;
                case 2:
                    if (stack.isEmpty()){
                        sb.append(-1).append("\n");
                    } else{
                        sb.append(stack.pop()).append("\n");
                    }
                    break;
                case 3:
                    sb.append(stack.size()).append("\n");
                    break;
                case 4:
                    if (stack.isEmpty()){
                        sb.append(1).append("\n");
                    } else{
                        sb.append(0).append("\n");
                    }
                    break;
                case 5:
                    if (stack.isEmpty()){
                        sb.append(-1).append("\n");
                    }else{
                        sb.append(stack.peek()).append("\n");
                    }
                    break;
            }
        }
        System.out.print(sb);
    }
}
