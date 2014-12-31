//
//  Balanced_Binary_Tree.cpp
//  Longest Substring
//
//  Created by Bowie Hsu  on 14/12/29.
//  Copyright (c) 2014年 Bowie Hsu . All rights reserved.
//

#include <stdio.h>
#include <iostream>

//  Definition for binary tree
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };

using namespace std;
class Solution {
public:
    //递归返回树的高度
    //因为result结果是要传回到isBanlanced函数中，所以是引用
    int judge(TreeNode *root,bool &result)
    {
        if (!root)return 0;
        int leftheight=judge(root->left, result);
        int rightheight=judge(root->right, result);
        if (abs(leftheight-rightheight)>1)
            result=false;
        return max(leftheight,rightheight)+1;
    }
    
    bool isBalanced(TreeNode *root)
    {
        bool result=true;
        int height=judge(root, result);
        return result;
    }
  
};