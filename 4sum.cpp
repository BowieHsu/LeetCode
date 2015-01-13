//
//  4sum.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/17.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//
#include<vector>
#include<map>
//#include <unordered_set>
#include <unordered_map>
#include<set>
#include <utility>
using namespace std;
class Solution
{
public:
    vector<vector<int> > fourSum(vector<int> &num, int target)
    {
        vector<vector<int>> output;
        vector<int> buffer=*new vector<int> (4);
        auto len=num.size();
        if (len<4)
        return output;
        //对输入序列进行排序
        sort(num.begin(),num.end());
        //建立一张图，用来存储计算结果
        unordered_multimap<int,pair<int,int>> mapresult;
        for (int i=0; i<len; ++i)
        {
            for (int j=i+1; j<len; ++j)
            {
                int sum=num[i]+num[j];
                mapresult.insert(make_pair(sum,make_pair(i, j)));
                
            }
        }
        for (auto i=mapresult.begin(); i!=mapresult.end(); ++i) {
            //求两个pair的和与traget的匹配关系
            int x=target-i->first;
            //利用equal_range来寻找x的值，返回两个迭代器,在两个迭代器的范围内查找x
            auto range=mapresult.equal_range(x);
            for (auto j=range.first; j!=range.second;++j )
            {
                auto a=i->second.first;
                auto b=i->second.second;
                auto c=j->second.first;
                auto d=j->second.second;
                buffer[0]=num[a];
                buffer[1]=num[b];
                buffer[2]=num[c];
                buffer[3]=num[d];
                if (a!=c&&a!=d&&b!=c&&b!=d)
                {
                    sort(buffer.begin(), buffer.end());
                    output.push_back(buffer);
                }
               
            }
            
           
        }
        sort(output.begin(),output.end());
        output.erase(unique(output.begin(), output.end()),output.end());
        return output;
    }
};

