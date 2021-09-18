class Solution {
    // Time: O(n**3)
    // Space: O(n**2)
    public List<String> addOperators(String num, int target) {
        List<String> res = new ArrayList<>();
           StringBuilder sb = new StringBuilder();
        dfs(res, sb, num, 0, target, 0, 0);
        return res;
    }

    public void dfs(List<String> res, StringBuilder sb, String num, int pos, int target, long prev, long multi) { 
        if (pos == num.length()) {
            if (target == prev) {
                res.add(sb.toString());
            }
            return;
        }
        for (int i = pos; i < num.length(); i++) {
            if (startsWithZero(num, i, pos)) {
                break;
            }
            long curr = Long.parseLong(num.substring(pos, i + 1));
            int len = sb.length();
            if (pos == 0) {
                dfs(res, sb.append(curr), num, i + 1, target, curr, curr); 
                sb.setLength(len);
            } else {
                dfs(res, sb.append("+").append(curr), num, i + 1, target, prev + curr, curr); 
                sb.setLength(len);
                dfs(res, sb.append("-").append(curr), num, i + 1, target, prev - curr, -curr); 
                sb.setLength(len);
                dfs(res, sb.append("*").append(curr), num, i + 1, target, prev - multi + multi * curr, multi * curr); 
                sb.setLength(len);
            }
        }
    }
        private boolean startsWithZero(String num, int start, int curr) {
            return num.charAt(curr) == '0' && start != curr;
        }
    }