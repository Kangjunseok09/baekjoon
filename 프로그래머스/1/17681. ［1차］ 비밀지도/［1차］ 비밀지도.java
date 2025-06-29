class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for(int i = 0; i < n; i++){
            int binary = arr1[i] | arr2[i];
            
            String map = String.format("%" + n + "s", Integer.toBinaryString(binary));

            
            map = map.replace('1', '#');
            map = map.replace('0', ' ');
            
            answer[i] = map;
        }
        
        return answer;
    }
}