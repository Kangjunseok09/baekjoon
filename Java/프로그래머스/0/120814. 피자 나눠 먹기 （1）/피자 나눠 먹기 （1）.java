class Solution {
    public int solution(int n) {
        int answer = 0;
        int cnt = 1;
        int pizza = 7;
        while (true){
            if(pizza - n >= 0){
                answer = cnt;
                break;
            }else{
                pizza += 7;
                cnt += 1;
            }
        }
        return answer;
    }
}