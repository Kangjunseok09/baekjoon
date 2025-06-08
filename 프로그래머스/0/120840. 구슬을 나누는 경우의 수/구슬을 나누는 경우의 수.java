class Solution {
    public int solution(int balls, int share) {
        if(share >= balls) return 1;
        return (int) Math.round(fac(balls) / (fac(balls-share) * fac(share)));
    }
    
    public double fac(int n) {
        if(n==1) return 1;
        return n * fac(n-1);
    }   
}
