class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.rec(digits, 0, res, "")
        return res
    def rec(self, digits, curr_idx, res, curr_str):
        if (curr_idx == len(digits)):
            if (curr_str != ""):
                res.append(curr_str)
            return
        if (digits[curr_idx] == '2'):
            self.rec(digits, curr_idx+1, res, curr_str+'a')
            self.rec(digits, curr_idx+1, res, curr_str+'b')
            self.rec(digits, curr_idx+1, res, curr_str+'c')
        if (digits[curr_idx] == '3'):
            self.rec(digits, curr_idx+1, res, curr_str+'d')
            self.rec(digits, curr_idx+1, res, curr_str+'e')
            self.rec(digits, curr_idx+1, res, curr_str+'f')
        if (digits[curr_idx] == '4'):
            self.rec(digits, curr_idx+1, res, curr_str+'g')
            self.rec(digits, curr_idx+1, res, curr_str+'h')
            self.rec(digits, curr_idx+1, res, curr_str+'i')
        if (digits[curr_idx] == '5'):
            self.rec(digits, curr_idx+1, res, curr_str+'j')
            self.rec(digits, curr_idx+1, res, curr_str+'k')
            self.rec(digits, curr_idx+1, res, curr_str+'l')
        if (digits[curr_idx] == '6'):
            self.rec(digits, curr_idx+1, res, curr_str+'m')
            self.rec(digits, curr_idx+1, res, curr_str+'n')
            self.rec(digits, curr_idx+1, res, curr_str+'o')
        if (digits[curr_idx] == '7'):
            self.rec(digits, curr_idx+1, res, curr_str+'p')
            self.rec(digits, curr_idx+1, res, curr_str+'q')
            self.rec(digits, curr_idx+1, res, curr_str+'r')
            self.rec(digits, curr_idx+1, res, curr_str+'s')
        if (digits[curr_idx] == '8'):
            self.rec(digits, curr_idx+1, res, curr_str+'t')
            self.rec(digits, curr_idx+1, res, curr_str+'u')
            self.rec(digits, curr_idx+1, res, curr_str+'v')
        if (digits[curr_idx] == '9'):
            self.rec(digits, curr_idx+1, res, curr_str+'w')
            self.rec(digits, curr_idx+1, res, curr_str+'x')
            self.rec(digits, curr_idx+1, res, curr_str+'y')
            self.rec(digits, curr_idx+1, res, curr_str+'z')

        