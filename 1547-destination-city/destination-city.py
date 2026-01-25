class Solution:
    def destCity(self, paths):
        # Step 1: collect all starting cities
        start_cities = set(path[0] for path in paths)
        
        # Step 2: find the city that is never a starting city
        for path in paths:
            if path[1] not in start_cities:
                return path[1]
