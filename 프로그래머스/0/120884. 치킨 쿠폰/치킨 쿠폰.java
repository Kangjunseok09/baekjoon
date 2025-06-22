class Solution {
    public int solution(int chicken) {
        int coupon = chicken;
        int order = 0;
        while (coupon / 10 != 0){
            coupon -= 10;
            order += 1;
            coupon += 1;
        }
        
        return order;
    }
}