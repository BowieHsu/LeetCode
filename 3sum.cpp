class Solution{
public:
    vector<vector<int>> threeSum(vector<int> &num)//容器无法赋值，采用引用初始化
    {
        //利用STL对容器排序
        sort(num.begin(),num.end());
        vector<vector<int>> output;
        vector <int> buffer(3);
        int len=num.size();
        if (len<3)
        {
            return output;
        }
        int j=0,k=0;
        bool iden=false;
        
        for(int i=0;i<len-2;++i)
        {
            
            if(i > 0 && num[i] == num[i-1]) continue;
            for(k=i+1;k<len-1;++k)
            {
                int low=k+1;
                int high=len-1;
                while(low<=high)
                {
                    j=(low+high)/2;
                    if(num[j]+num[k]+num[i]==0)
                    {
                        buffer[0]=num[i];
                        buffer[1]=num[k];
                        buffer[2]=num[j];
                        output.push_back(buffer);
                        break;
                    }
                    else if(num[j]+num[k]+num[i]>0)
                        high=j-1;
                    else if(num[j]+num[k]+num[i]<0)
                        low=j+1;
                }
            }
        }
        //解决{0，0，0，0}这样的输入，将输出容器排序然后删除重复元素
        sort(output.begin(),output.end());
        output.erase(unique(output.begin(),output.end()),output.end());
        return output;
    }
};
