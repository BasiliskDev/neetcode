class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        composite_list = [[position[i], (target - position[i])/speed[i]] for i in range(len(position))]
        composite_list.sort(key=lambda x: x[0], reverse=True)
        print(composite_list)

        prev_time = -1
        fleets = 0
        for pos, time in composite_list:
            if (time > prev_time):
                prev_time = time
                fleets += 1
        
        return fleets

                    


        

        