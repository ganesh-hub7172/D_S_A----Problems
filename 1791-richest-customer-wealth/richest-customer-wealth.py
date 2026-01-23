class Solution:
    def maximumWealth(self, accounts):
        # Compute wealth for each customer and return the max
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
