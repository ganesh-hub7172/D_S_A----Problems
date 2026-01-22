#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> answer(n, 0);
        
        // Left to right
        int balls = 0;
        int ops = 0;
        for (int i = 0; i < n; i++) {
            answer[i] += ops;
            if (boxes[i] == '1') balls++;
            ops += balls;
        }
        
        // Right to left
        balls = 0;
        ops = 0;
        for (int i = n-1; i >= 0; i--) {
            answer[i] += ops;
            if (boxes[i] == '1') balls++;
            ops += balls;
        }
        
        return answer;
    }
};
