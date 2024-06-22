# # Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

# Example:

# Given “25525511135”,

# return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
class Solution:
    def restoreIpAddresses(self, A):
        def backtrack(s, parts, result):
            # Base case: if we have 4 parts and used up all characters in s
            if len(parts) == 4 and not s:
                result.append(".".join(parts))
                return
            # If we have 4 parts but s is empty, or s is not empty but parts are already 4
            if len(parts) == 4 or not s:
                return
            
            # Try all possible lengths for the next part (1 to 3 digits)
            for i in range(1, min(4, len(s) + 1)):
                part = s[:i]
                # Check if part is valid (not starting with 0 unless it's "0" itself and <= 255)
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue
                # Recurse with the remaining string and updated parts
                backtrack(s[i:], parts + [part], result)
        
        result = []
        backtrack(A, [], result)
        return result