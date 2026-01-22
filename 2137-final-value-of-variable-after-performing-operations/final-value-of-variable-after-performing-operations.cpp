#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int X = 0;
        for (const string &op : operations) {
            // If the operation contains '+', increment X
            if (op.find('+') != string::npos) {
                X++;
            } else { // Otherwise, decrement X
                X--;
            }
        }
        return X;
    }
};
