#include<iostream>
#include<bits/stdc++.h>
class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        int n = nums.size();
        //int smallest = INT_MAX;
        int allOne = findAllOne(n);
        int smallest = allOne;
        vector<bool> visited(n,false);
        for(int i = 0 ; i < n; i ++){
            if(i == nums[i])
                visited[i] = true;
            else if (visited[i] == false){
                //int tmp = allOne;
                int start = i;
                while (!visited[start]){
                    //tmp = tmp & nums[start];
                    smallest = smallest & nums[start];
                    visited[start] = true;
                    start = nums[start];
                }
                //smallest = min(smallest, tmp);
            }
        }
        return smallest != allOne ? smallest : 0;
    }
private:
    int findAllOne(int a){
        int val = 1;
        while(a){
            val = val << 1;
            a /= 2;
        }
        return val - 1;
    }
};