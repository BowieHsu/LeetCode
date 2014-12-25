//
//  GenerateParentheses.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/25.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
class Solution
{
public:
    vector <string> generateParenthesis(int n)
    {
        vector<string> r=*new vector <string>;
        feedback(r, "", n, 0);
        return r;
    }
    
    //建立递归式，表达所有括号的可能组合
    void feedback (vector<string> &v,string ass,int left,int right)
    {
        if (left==0&&right==0)
        {
            v.push_back(ass);
            return ;
        }
        //m表示“(”号的个数
        //n表示“）”号的个数
        //递归调用两个条件，形成所有可能的组合
        if (left>0)
            feedback(v,ass+"(",left-1,right+1);
        if (right>0)
            feedback(v,ass+")",left,--right);
    }
};