class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ls = []
        def helper(curr_open, remaining_att, currstr):
            if (remaining_att == 0):
                for i in range(curr_open):
                    currstr += ")"
                ls.append(currstr)
            else:
                helper(curr_open+1, remaining_att-1, currstr + "(")
                if (curr_open > 0):
                    helper(curr_open-1, remaining_att, currstr + ")")
        helper(0, n, "")
        return ls
        
        