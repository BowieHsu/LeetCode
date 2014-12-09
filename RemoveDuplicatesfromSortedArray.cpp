//
//  RemoveDuplicatesfromSortedArray.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/9.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

#include "RemoveDuplicatesfromSortedArray.h"
#include "string"
#include <iostream>
using namespace std;
//Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

//Do not allocate extra space for another array, you must do this in place with constant memory.
class Solution {
public:
    int removeDuplicates(int A[], int n)
    {
        //去掉重复的元素
        int num=1;
        if(n==0)
            return NULL;
        for (int i=0; i<n-1; ++i)
        {
            if (A[i]!=A[i+1])
            A[num++]=A[i+1];
        }
        //返回不相同数字的个数
        return num;
    }
};

int main()
{
    Solution x;
    int n=2;
    int s[]={1,1};
    int ans;
    ans=x.removeDuplicates(s,n);
    cout<<ans<<endl;
}