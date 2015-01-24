//
//  Combination.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/12.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <vector>
using namespace std;
class Solution {
public:
    void search(vector<int> &num, int target)
    {
        //递归
        if (target==0)
        {
            return;
        }
        
        if (find(num.begin(), num.end(), target)) {
            return;
        }
    
    }
    vector<vector<int> > combinationSum2(vector<int> &num, int target)
    {
     //对输入num进行排序
        sort(num.begin(),num.end());
     //寻找target和num的关系
        vector <int> buffer;
        vector <vector<int>> result;
        int len=num.size();
        for (int i=0;i<len;++i)
        {
            auto xiao=target-num[i];
            
        }
        }
        
    }
};

int main()
{
    Solution x;
    x.combinationSum2(<#vector<int> &num#>, <#int target#>)

}