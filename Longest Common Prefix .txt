//
//  main.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 29/11/21.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include "stdio.h"
#include "ctype.h"

using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string Com=" ";
        string max=" ";
        //第0个字符串和后面的依次比较
        auto lenth=strs.size();
        if(lenth==0)return "";
        auto num=strs[0].size();
        for (int i=1; i<lenth; ++i)
        {
            int j;
            for(j=0;j<min(strs[0].size(),strs[i].size());++j)
            {
               if(strs[0][j]!=strs[i][j])
                break;
            }
         if(num>j)num=j;
         }
        Com=strs[0].substr(0,num);
        return Com;
    }
};

int main()
{
    vector<string> str={"aab","aad","aae"};
    string ans;
    Solution absolute;
    ans=absolute.longestCommonPrefix(str);
    cout<<ans<<endl;
   // cout<<"what the fuck?";
}

