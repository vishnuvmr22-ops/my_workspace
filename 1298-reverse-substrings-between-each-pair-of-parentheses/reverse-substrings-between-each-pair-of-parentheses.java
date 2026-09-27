import java.util.Stack;

class Solution {
    public String reverseParentheses(String s) {
        int n = s.length();
        int[] pair = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        // Step 1: Pre-process the string to find matching parenthesis pairs
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else if (s.charAt(i) == ')') {
                int j = stack.pop();
                pair[i] = j;
                pair[j] = i; // Map both brackets to each other's index
            }
        }
        
        // Step 2: Traverse the string using the "Wormhole" technique
        StringBuilder result = new StringBuilder();
        int curr = 0;
        int direction = 1; // 1 means moving forward, -1 means moving backward
        
        while (curr < n) {
            char c = s.charAt(curr);
            if (c == '(' || c == ')') {
                // Teleport to the matching bracket's index
                curr = pair[curr];
                // Reverse the direction of traversal
                direction = -direction;
            } else {
                // Append the character to our result
                result.append(c);
            }
            // Move to the next character based on current direction
            curr += direction;
        }
        
        return result.toString();
    }
}