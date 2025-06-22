import java.util.*;
class Solution {
    public int solution(int order) {
        int answer = 0;
        String intorder = String.valueOf(order);
        int count = 0;
        for(int i = 0; i < intorder.length(); i++){
            if(intorder.charAt(i) == '3' || intorder.charAt(i) == '6' || intorder.charAt(i) == '9') count++;
        }
        answer = count;
        return answer;
    }
}