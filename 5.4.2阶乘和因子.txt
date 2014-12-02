//
//  main.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 29/11/21.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//
// what the fuck?
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include "stdio.h"
#include "ctype.h"
using namespace std;

int is_prime(int x)
{
    for (int i=2; i*i<=x; ++i)
    {
        if(x%i==0)
        return 0;
        
    }
   return 1;
}

int main()
{
    int num=1;
    int input=10;
    int count=0;
    int max=0;
    //int a,b,c,d;
    int p[100];
    int list[100];
    //建立素数表
    for (int i=2; i<input+1; ++i)
    {
        if(is_prime(i))
        p[count++]=i;
        num=num*i;
    }
    //判断素数因子的个数
   for (int i=0; i<input; ++i)
    {
        while(p[i]!=0 && num%p[i]==0)
        {
            num=num/p[i];
            ++list[i];
            //设置下标最大值
            if (i>max)
            max=i;
            
        }
    
    }
    for(int i=0;i<max+1;++i)
    {
        cout<<list[i];
    }
}