#include<string>
#include<vector>
using namespace std;

//参考了各种解题思路之后的一种比较偷懒的方法，建一张表，将可能的情况都存进去，直接照着读
struct node
{
    int para;
    string key;
    node(int k,string s):para(k),key(s){}
};
class Solution {
public:
    string intToRoman(int num) 
   {
       //划分所有可能性
       string res;
       vector<node> buffer;
       buffer.push_back(node(1000,"M"));
       buffer.push_back(node(900,"CM"));
       buffer.push_back(node(500,"D"));
       buffer.push_back(node(400,"CD"));
       buffer.push_back(node(100,"C"));
       buffer.push_back(node(90,"XC"));
       buffer.push_back(node(50,"L"));
       buffer.push_back(node(40,"XL"));
       buffer.push_back(node(10,"X"));
       buffer.push_back(node(9,"IX"));
       buffer.push_back(node(5,"V"));
       buffer.push_back(node(4,"IV"));
       buffer.push_back(node(1,"I"));
       
       int i=0;
       if (num==1) {
           res.append("I");
       }
       while(num>0)
       {
       if(num/buffer[i].para==0)
       { ++i;continue;}
           
           for (int j=0; j<num/buffer[i].para; ++j)
               res.append(buffer[i].key);
               num%=buffer[i].para;
       }
       return res;
    }
};
