//
//  Best_Time_to_Buy3.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/8.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    //在合适的时机买入和卖出股票，可以多次买卖，但必须先买才能卖
    //简直醉到不行，这个题目的bug在于可以同一天买卖，于是总的利润就是所有差距之和
    int maxProfit(vector<int> &prices)
    {
        if (prices.empty()) {
            return 0;
        }
        int maxvalue=0;
        for (auto i=prices.begin(); i!=prices.end()-1; ++i)
        {
            if (*i<*(i+1))
            {
                maxvalue+=*(i+1)-*i;
            }
        }
        return maxvalue;
        
    }
};

int main()
{
    Solution x;
    int answer;
    vector<int> input={1,2,3,4,5};
    answer=x.maxProfit(input);
    cout<<answer<<endl;

}