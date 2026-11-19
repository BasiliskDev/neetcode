class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def traverse(idx, ls, currsum):
            if (currsum > target):
                return
            if (idx == len(candidates)):
                if (currsum == target):
                    ret.append(ls.copy())
            else:
                ls.append(candidates[idx])
                traverse(idx+1, ls, currsum + candidates[idx])
                ls.pop()
                new_idx = idx+1;
                while (new_idx < len(candidates) and candidates[new_idx] == candidates[idx]):
                    new_idx += 1
                traverse(new_idx, ls, currsum)
        candidates = sorted(candidates)
        print(candidates)
        traverse(0, [], 0)
        return ret


        