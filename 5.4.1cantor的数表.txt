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
    
    vector<int> calc(int b)
    {//判断是否为空字符串
        int num=0;
        int a=1;
        while(num+a<b)
        {   num+=a;
            ++a;
        }
        //判断是奇数还是偶数
        //分子和分母
        int c=0;
        int d=0;
        if(a%2==0)
        {
             c=b-num;
             d=a+1-c;
            
        }
        else
        {
             d=b-num;
             c=a+1-d;
        }
        //float out=c/d;
        vector<int> out;
        out.push_back(c);
        out.push_back(d);
        return out;
    }
};

int main()
{
    int input=14;
    vector <int> ans;
    Solution x;
    ans=x.calc(input);
    cout<<ans[0]<<ans[1]<<endl;
    cout<<"what?"<<endl;

}

