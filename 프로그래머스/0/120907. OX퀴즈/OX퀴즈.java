class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];

        for(int i = 0; i < quiz.length; i++){
            String[] s = quiz[i].split(" ");
            int x, y, z;
            String op;
            x = Integer.parseInt(s[0]);
            y = Integer.parseInt(s[2]);
            z = Integer.parseInt(s[4]);
            op = s[1];
            if(op.equals("+")){
                answer[i] = (x + y == z) ? "O":"X";
            }else{
                answer[i] = (x - y == z) ? "O":"X";
            }
        }
        
        return answer;
    }
}