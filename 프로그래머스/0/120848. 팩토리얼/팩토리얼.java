class Solution {
    public int solution(int n) {
        int answer = 0;
        int fac = 1;
        for(int i = 1; i <= n; i++){
            fac *= i;
            if(fac == n){
                return i;
            }else if(fac > n){
                return i-1;
            }
        }
        return answer;
    }
}