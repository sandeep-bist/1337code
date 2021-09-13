class Solution {
    public String validIPAddress(String IP) {
        if (isValidIPv4(IP)) {
            return "IPv4";
        }
        if (isValidIPv6(IP)) {
            return "IPv6";
        }
        return "Neither";
    }

     private boolean isValidIPv4(String IP) {
        return (isValidIPv4Length(IP) && isValidIPv4Format(IP));
    }

    private boolean isValidIPv4Length(String IP) {
        int cnt = 0;
        for (char ch : IP.toCharArray()) {
            if (ch == '.') {
                cnt++;
            }
        }
        return cnt == 3;
    }

    private boolean isValidIPv4Format(String IP) {
        String[] fields = IP.split("\\.");
        if (fields.length != 4) {
            return false;
        }
        for (String field : fields) {
            if (field.isEmpty() || field.length() > 3) {
                return false;
            }
            int sz = field.length();
            for (int i = 0; i < sz; ++i) {
                if (!Character.isDigit(field.charAt(i))) {
                    return false;
                }
            }
            int num = Integer.valueOf(field);
            if (!String.valueOf(num).equals(field) || num < 0 || num > 255) {
                return false;
            }
        }
        return true;
    }
        
    private boolean isValidIPv6(String IP) {
        return isValidIPv6Length(IP) && isValidIPv6Format(IP);
    }

    private boolean isValidIPv6Length(String IP) {
        int cnt = 0;
        for (char ch : IP.toCharArray()) {
            if (ch == ':') {
                cnt++;
            }
        }
        return cnt == 7;
    }

    private boolean isValidIPv6Format(String IP) {
        String[] fields = IP.split(":");
        if (fields.length != 8) {
            return false;
        }
        for (String field : fields) {
            if (field.isEmpty() || field.length() > 4) {
                return false;
            }
            int sz = field.length();
            for (int i = 0; i < sz; ++i) {
                if (!isValidIPv6Char(field.charAt(i))) {
                    return false;
                }       
            }
        }
        return true;
    }

    private boolean isValidIPv6Char(char ch) {
        return (ch >= '0' && ch <= '9') || 
               (ch >= 'A' && ch <= 'F') || 
               (ch >= 'a' && ch <= 'f');
    }
}