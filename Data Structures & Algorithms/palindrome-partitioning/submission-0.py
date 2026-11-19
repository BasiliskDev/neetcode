class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def helper(curr_idx, curr_p, currstr):
            print(curr_p)
            if (currstr[::-1] == currstr and currstr != ""):
                if (curr_idx == len(s)):
                    curr_p.append(currstr)
                    ret.append(curr_p.copy())
                    curr_p.pop()
                    return
                helper(curr_idx + 1, curr_p, currstr + s[curr_idx])
                curr_p.append(currstr)
                helper(curr_idx + 1, curr_p, s[curr_idx])
                curr_p.pop()
            else:
                if (curr_idx == len(s)):
                    return
                helper(curr_idx + 1, curr_p, currstr + s[curr_idx])
        helper(0, [], "")
        return ret
                
        