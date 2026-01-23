class Solution:
    def recoverOrder(self, order, friends):
        friends_set = set(friends)
        result = []
        
        for x in order:
            if x in friends_set:
                result.append(x)
        
        return result
