//
//  ValidParenthness.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/9.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

//Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

//The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#include "ValidParenthness.h"
#include "string"
#include "stack"
#include "iostream"
using namespace std;

class Solution {
public:
    bool isValid(string s)
    {
        bool output=true;
        //使用堆栈，遇到符号就入栈，匹配就出栈
        stack<char> input;
        input.push(s[0]);
        //找到brackets，判断其关系
        for (int i=1; i<s.length(); i++)
        {
            if ((!input.empty())&&ismatch(input.top(),s[i]))
            {
                input.pop();
            }
            else
            {
                input.push(s[i]);
            
            }
        }
        if (input.empty())
        {
            output=true;
        }
        else
            output=false;
            return output;
        }
   

bool ismatch(char s1,char s2)
{
    if ((s1=='('&&s2==')')||(s1=='{'&&s2=='}')||(s1=='['&&s2==']'))
    {
        return true;
    }
    else
        return false;
}
};


int main()
{
    string s1="[]";
    bool output=false;
    Solution x;
    output=x.isValid(s1);
    cout<<output<<endl;

}