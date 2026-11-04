class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        all_muls = []
        num1 = num1[::-1]
        num1 = [int(num) for num in num1]
        num2 = num2[::-1]
        num2 = [int(num) for num in num2]
        max_len = 0
        #print(num1)
        #print(num2)
        for idx, d2 in enumerate(num2):
            carry_over = 0
            curr_mul = []
            for j in range(idx):
                curr_mul.append(0)
            for d1 in num1:
                curr_mul.append((d2 * d1 + carry_over)%10)
                #print(d2)
                #print(d1)
                #print(d2*d1+carry_over)
                carry_over = (d2*d1+carry_over)//10
                #print(carry_over)
                #print()
            if (carry_over != 0):
                curr_mul.append(carry_over)
            all_muls.append(curr_mul)
            max_len = max(max_len, len(curr_mul))
        for i in range(len(all_muls)):
            all_muls[i].extend([0] * (max_len - len(all_muls[i])))
            #print(all_muls[i])
        ret = [0] * max_len
        #print(all_muls)
        carry_over = 0
        for i in range(max_len):
            running_sum = 0
            for j in range(len(all_muls)):
                running_sum += all_muls[j][i]
            ret[i] = (running_sum + carry_over)%10
            carry_over = (running_sum + carry_over)//10
        if (carry_over != 0):
            ret.append(carry_over)

        ret = ret[::-1]
        final_ret = ""
        for c in ret:
            if (c == 0 and len(final_ret)==0):
                continue
            final_ret += str(c)
        if (len(final_ret) == 0):
            return "0"
        return final_ret
        



        