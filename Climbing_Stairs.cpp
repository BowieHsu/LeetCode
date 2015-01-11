//
//  Climbing_Stairs.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/11.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
class Solution {
public:
    //定义递归函数，计算阶乘
    int mux(int r)
    {
        if (r==0) {
            return 1;
        }
        int result=r*mux(r-1);
        return result;
    }

    int climbStairs(int n)
    {
    
        int len=0;
        int len2=0;
        int len3=0;
        int num=0;
        int total=0;
        if(n==0)
            return 0;
        //输入数字为偶数
        if(n%2==0)
        {
            for(int i=0;i<n/2;++i)
            {
                len=mux(n-i);
                len2=mux(n-2*i);
                len3=mux(i);
                num+=len/(len2*len3);
               // total=total+num;
            }
        }
        //输入数字为奇数
        else if(n%2!=0)
        {
            for(int i=0;i<(n-1)/2;++i)
            {
                len=mux(n-i);
                len2=mux(n-2*i);
                len3=mux(i);
                num=len/(len2*len3);
                total=total+num;
            }
        }
        
    
        return num;
    }
};

int main()
{
    Solution x;
    //int output;
    //int output=x.climbStairs(35);
    int output=x.mux(35);
    cout<<output<<endl;
}