//
//  3SumClosest.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/22.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <cstdlib>
using namespace std;
class Solutuion
{
public:
    int threeSumClosest(vector<int> &num, int target)
{//给出target，找到三个数的和与target
    int output=0;
    sort(num.begin(), num.end());
    auto len=num.size();
    if (len<3)
    {
        return 0;
    }
    //从第一个数遍历到倒数第三个数
    output=num[0]+num[1]+num[2];
    for (int i=0;i<len-2; ++i)
    {
        int j=i+1;
        int k=len-1;
        while (j<k)
        {
            int sum=num[i]+num[j]+num[k];
            //比较output与sum和target之间的距离
            if(abs(target-sum)<abs(target-output))
            {
                output=sum;
            }
            if (output==target)
                return target;
            (target>sum)?++j:--k;
        }
    }
    return output;
}
};