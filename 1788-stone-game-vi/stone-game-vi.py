class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)
        
        stones = []
        for i in range(n):
            stones.append((aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]))
        
        # Sort by total value descending
        stones.sort(reverse=True)
        
        alice_score = 0
        bob_score = 0
        
        for i in range(n):
            if i % 2 == 0:   # Alice's turn
                alice_score += stones[i][1]
            else:           # Bob's turn
                bob_score += stones[i][2]
        
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0
