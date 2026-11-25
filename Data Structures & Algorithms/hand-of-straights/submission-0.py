from collections import defaultdict, deque

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)
        groups = defaultdict(deque)

        for card in hand:
            if groups[card]:
                prev_cards = groups[card].popleft()
                curr_size = prev_cards + 1
            else:
                curr_size = 1

            if curr_size < groupSize:
                groups[card + 1].append(curr_size)

        return all(not q for q in groups.values())