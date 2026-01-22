#include <unordered_set>
#include <string>
using namespace std;

class Solution {
public:
    int maxDistinct(string s) {
        unordered_set<char> usedStartChars;
        int count = 0;

        for (char c : s) {
            if (usedStartChars.find(c) == usedStartChars.end()) {
                count++;
                usedStartChars.insert(c);
            }
        }

        return count;
    }
};
