import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(String my_string) {
        List<Integer> list = new ArrayList<>();
        my_string = my_string.replaceAll("[^0-9]", "");
        for(int i = 0; i < my_string.length(); i++){
            list.add(Integer.parseInt(String.valueOf(my_string.charAt(i))));
        }
        Collections.sort(list);
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }

}