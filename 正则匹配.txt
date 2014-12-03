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
    bool isMatch(const char *s, const char *p)
    {   //用下标来对s和P进行操作
       
    
        if (*(p+1)!='*')
        {
            if(*s==*p||*p=='.')
            {
                return isMatch(s+1,p+1);
            }
            else if(*s!=*p && *p!='.')
            {
                return isMatch(s,p+1);
            }
        }
        
        else
        {
            if(*s!=*p && *p!='.')
            {
                return isMatch(s,p+2);
            }
            else if(*s==*p||*p=='.')
            {
                return isMatch(s+1,p+1);
            }
        
        }
    }
};

int main()
{
    char a='a';
    char b='*';
    const char *x=&a;
    const char *y=&b;
    bool ans;
    Solution absolute;
    ans=absolute.isMatch(x,y);
    cout<<ans<<endl;
   // cout<<"what the fuck?";
}

