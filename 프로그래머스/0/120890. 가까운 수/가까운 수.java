import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int near = array[0];
        for(int i = 0; i < array.length; i++){
            if (Math.abs(n - near) > Math.abs(n - array[i])){
                near = array[i];
            }else if(Math.abs(n - near) == Math.abs(n - array[i])){
                if (n - array[i] > n - near){
                    near = array[i];
                }
            }
        }
        answer = near;
        return answer;
    }
}