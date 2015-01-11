//
//  New_Solution.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/11.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    //据说是斐波那契
    int climbStairs(int n)
    {
        int x1=1;
        int x2=1;
        for (int i=0; i<n; ++i) {
            x2=x1+x2;
            x1=x2-x1;
        }
        return x1;
    }
};

int main()
{
    Solution x;
    int answer=x.climbStairs(44);
    cout<<answer<<endl;

}