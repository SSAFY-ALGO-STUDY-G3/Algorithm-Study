import java.util.*;

class Solution {
    static boolean[] visited = new boolean[10001];
    static List<String> allRoute = new ArrayList<>(); 
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        
        dfs("ICN", "ICN", tickets, 0);
        
        Collections.sort(allRoute);
        answer = allRoute.get(0).split(" ");
        
        return answer;
    }
    
    public void dfs(String start, String route, String[][] tickets, int cnt){
        if(cnt == tickets.length){
            allRoute.add(route);
            return;
        }
        
        for(int i=0; i < tickets.length; i++){
            if(start.equals(tickets[i][0]) && !visited[i]){
                visited[i] = true;
                dfs(tickets[i][1], route + " " + tickets[i][1], tickets, cnt + 1);
                visited[i] = false;
            }
        }
    }
    
}