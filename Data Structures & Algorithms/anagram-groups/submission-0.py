class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            strs[i] = (''.join(sorted(strs[i])), strs[i])
        strs.sort(key=lambda x: x[0])
        ret = []
        curr = []
        for i in range(len(strs)):
            if (curr == [] or curr[0][0] == strs[i][0]):
                curr.append(strs[i])
            else:
                ret.append(curr)
                curr = []
                curr.append(strs[i])
        ret.append(curr)
        final_ret = []
        for x in ret:
            ls = []
            for r in x:
                ls.append(r[1])
            final_ret.append(ls)
        return final_ret