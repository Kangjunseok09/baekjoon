class Solution {
    public String[] solution(String my_str, int n) {
        int len = my_str.length() % n == 0 ? my_str.length() / n: my_str.length() / n + 1;
        
        String[] answer = new String[len];
        for(int i = 0; i < len; i++){
            answer[i] = my_str.substring(i * n, Math.min(i * n + n, my_str.length()));
        }
        return answer;
    }
}