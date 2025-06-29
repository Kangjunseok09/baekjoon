import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[][] sp = {{1,2,3,4,5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int[] scores = {0, 0, 0};
        for(int i = 0; i < answers.length; i++){
            if(answers[i] == sp[0][i % sp[0].length]){
                scores[0] += 1;
            }
            if(answers[i] == sp[1][i % sp[1].length]){
                scores[1] += 1;
            }
            if(answers[i] == sp[2][i % sp[2].length]){
                scores[2] += 1;
            }
        }
        
        int max = Math.max(scores[0], Math.max(scores[1], scores[2]));
        
        for (int i = 0; i < 3; i++){
            if (max == scores[i]){
                answer.add(i+1);
            }
        }
        
        int[] result = new int[answer.size()];
        for(int i = 0; i < answer.size(); i++){
            result[i] = answer.get(i);
        }
        return result;
    }
}