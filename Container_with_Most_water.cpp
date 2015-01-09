//
//  Container_with_Most_water.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 15/1/9.
//  Copyright (c) 2015年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    //pair<int,int> pailie;
    //map<int,pair<int,int>> map_result;
    
    int maxArea(vector<int> &height)
    {
        //遍历所有的高度
        //线性时间复杂度的算法
        int i=1;
        int j=height.size()+1;
        int output=0;
        while(i<j)
        {
            
            output=max(output,(j-i)*min(height[i-1],height[j-1]));
            if (height[i-1]<=height[j-1])
                i++;
            else if(height[i-1]>height[j-1])
                j--;
        }
        
        return output;
        
    }
};

int main()
{
    Solution x;
    vector<int>input={1,2,3,4,5,10,11};
    int answer=x.maxArea(input);
    cout<<answer<<endl;
}