class Solution {
    public String solution(String s) {
        String answer = "";
        int arr[] = new int[26];
        for(int i = 0; i < s.length(); i++){
            arr[s.charAt(i) - 'a']++;
        }
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == 1) answer += (char)(i + 'a');
        }
        return answer;
    }
}