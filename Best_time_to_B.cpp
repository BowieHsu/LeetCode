//
//  Best_time_to_B.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/1.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
/*Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
*/

#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
     //从i到j扫描
        int minmean=65536,maxvalue=0;
        if (prices.empty()) {
            return 0;
        }
        for (auto i=prices.begin(); i!=prices.end(); ++i)
        {
            minmean=min(minmean,*i);
            maxvalue=max(*i-minmean,maxvalue);
        }
        return maxvalue;
    }
};

int main()
{
    Solution x;
    vector<int> input={1,2,3,6};
    int result=x.maxProfit(input);
    cout<<result<<endl;

}