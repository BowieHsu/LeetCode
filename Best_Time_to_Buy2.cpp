//
//  Best_Time_to_Buy2.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/2.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <unordered_map>

using namespace std;
class Solution
{
public:
    //用关联容器存储手机按键和其代表的字母
    map<char, string> map_result;
    //构造函数对map_result进行初始化
    Solution(){
    map_result.insert({'2',"abc"});
    map_result.insert({'3',"def"});
    map_result.insert({'4',"ghi"});
    map_result.insert({'5',"jkl"});
    map_result.insert({'6',"mno"});
    map_result.insert({'7',"pqr"});
    map_result.insert({'8',"tuv"});
    map_result.insert({'9',"wxyz"});
    }
    //递归输出所有的数字
    vector<string> letterCombinations(string digits)
    {
        //空字符返回空
        vector<string> output;
        if (digits=="")
        {
            output.push_back("");
            return output;
        }
        //递归
        vector<string>buffer=letterCombinations(digits.substr(1));
        //在map_result中查找有关的结果
        string map_buffer=map_result[digits[0]];
        //利用递归，每次将在map中找到的字母排在目前有的string后，生成不同的排列组合
        for (auto i=0;i!=map_buffer.size(); ++i)
        {
            for (auto j=0; j!=buffer.size(); ++j)
            {
                output.push_back(map_buffer[i]+buffer[j]);
            }
            
        }
        return output;
    }

};

int main()
{
    Solution x;
    vector<string>answer=x.letterCombinations("23");
    for (auto i=answer.begin();i!=answer.end();++i)
    {
          cout<<*i<<endl;
    }
    
}