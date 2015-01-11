//
//  Best_Time_to_Buy3.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/9.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>
#include <set>
using namespace std;
class Solution {
public:
    //You may complete at most two transactions
    //先筛选high和low，在寻找split点，分两次遍历求得结果
    int maxProfit(vector<int> &prices)
    {
        int Totalprofit=0;
        int high=0,low=0;
        pair<int, int> pailie;
        vector<pair<int, int>> combine;
        //如果后面的比前面的高，就添加到profit上
        for (auto i=prices.begin(); i!=prices.end(); ++i)
        {
            if (*(i+1)>*i)
            {
                //Totalprofit+=*(i+1)-*i;
                high=*(i+1);
                pailie=make_pair(low, high);
                
            }
            else if(*(i+1)<*i)
            {
                //如果后面的数字比前面的小，记录下新的low
                low=*(i+1);
                combine.push_back(pailie);
            }
            }
        //建立好high-low表，遍历high-low表，寻找最大的两个profit的和
        //int i=0,j=combine.size();
        int left=0,right=0;
        //设置三个指针，遍历整个容器
        for (int i=0; i!=combine.size(); ++i)
        {
            //遍历0到i的组合
            int j=0;
            while(j<i)
            {
                right=combine[i].second-combine[j].first;
                ++j;
            }
            //遍历i到n的组合
            int jj=i+1;
            while (jj<combine.size())
            {
                left=combine[jj].second-combine[i].first;
                ++jj;
            }
            Totalprofit=max(Totalprofit,right+left);
            
        }
            
        return Totalprofit;
    }
};

int main()
{
    Solution x;
    vector<int> input={3,1,8,4,5,9,5,10};
    int result;
    result=x.maxProfit(input);
    cout<<result<<endl;

}