//
//  Remove Nth Node From End of List.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/8.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include "stdio.h"
#include "ctype.h"

using namespace std;
//定义链表结构
struct ListNode {
         int val;
         ListNode *next;
         ListNode(int x) : val(x), next(NULL) {}
     };

//实现对一个链表的反向删除，双指针，l1先走n步进行定位，l2进行节点删除
class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        if (head==NULL) {
            return 0;
        }
        ListNode *l1=head;
        
        ListNode output(0);
        output.next=head;
        ListNode *l2=&output;
        while (--n) {
            l1=l1->next;
        }
        
        while (l1->next)
        {
            l1=l1->next;
            l2=l2->next;
            
        }
        //可能出现删除最后一个节点的情况，需要考虑
        l2->next=l2->next->next;
        //如何删除该节点
        
        return output.next;
    }

};

int main()
{
    vector<string> str={"aab","aad","aae"};
    string ans;
    Solution absolute;
    ans=absolute.removeNthFromEnd(<#int *head#>, <#int n#>);
    cout<<ans<<endl;
    // cout<<"what the fuck?";
}
