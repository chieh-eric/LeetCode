class Solution {
public:
    int maxJump(vector<int>& stones) {
        int max_forward = 0;
        int max_backward = 0;
        int n = stones.size();
        for(int i = 2; i < n ; i+= 1){
            if (i%2)
                max_forward = max(max_forward, stones[i] - stones[i-2]);
            else
                max_backward = max(max_backward,  stones[i] - stones[i-2]);
        }
        return n > 2 ? max(max_forward, max_backward): stones[1];
    }
};