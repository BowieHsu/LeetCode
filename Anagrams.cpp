//
//  Anagrams.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/29.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;
class Solution{
public:
    vector<string>anagrams(vector<string> &strs)
    {
        string r;
        map<string, int> remap;
        vector<string> output;
        for (auto i=0; i<strs.size(); ++i)
        { r=strs[i];
          sort(r.begin(), r.end());
            if (remap.find(r)==remap.end())
            {
                remap[r]=i;
            }
            //如果remap中已经存储有相同的r，则将该r的位置remap[r]输出，然后清理掉
            else
            {
             if(remap[r]>=0)
             {
                 output.push_back(strs[remap[r]]);
                 remap[r]=-1;
             }
                //在清理掉第一次存储的r后，以后每次发现相同的r，就将该r的位置输出
                output.push_back(strs[i]);
            }
        }
        return output;
    }
};

int main()
{
    Solution x;
    vector<string> pri;
    vector<string> input(3,"abc");
    pri=x.anagrams(input);
    for (auto i=pri.begin();i!=pri.end(); ++i)
    {
        cout<<*i<<endl;
    }

}