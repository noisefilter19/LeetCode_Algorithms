//https://leetcode.com/problems/text-justification/
#define ff first
#define ss second
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int n=words.size();
        if(n==1)
        {
            vector<string> ans(1);
            ans[0]+=words[0];
            while(ans[0].length()!=maxWidth)
                ans[0]+=" ";
            return ans;
        }
        vector<pair<int,int>> len(n);
        len[0].first=words[0].length();
        len[0].second=len[0].first;
        int i;
        for(i=1;i<n;i++)
        {
            len[i].first=words[i].length();
            len[i].second=len[i-1].second+len[i].first;
        }
        if(len[i-1].ss+i-1<=maxWidth)
        {
            vector<string> ans(1);
            ans[0]+=words[0];
            for(int i=1;i<n;i++)
                ans[0]+=" "+words[i];
            while(ans[0].length()!=maxWidth)
                ans[0]+=" ";
            return ans;
        }
        vector<pair<int,int>> help(1);
        int check=0;
        help[0].ff=0;
        int j=0;
        for(i=0;i<words.size();i++)
        {
            if(check+len[i].first<=maxWidth)
            {
                check+=len[i].first;
                check++;
            }
            else
            {
                help[j].ss=i-1;
                j++;
                help.push_back(make_pair(i,0));
                check=len[i].first;
                check++;
            }
        }
        help[j].ss=i-1;
        j++;
        vector<string> ans(j,"");
        int sum=len[help[0].ss].ss;
        int space=help[0].ss;
        i=0;
        while(i!=help[0].ss)
        {
            ans[0]+=words[i];
            i++;
            int xx=maxWidth-sum;
            int j;
            for(j=0;j<ceil((double)xx/(double)space);j++)
            {
                ans[0]+=" ";
            }
            space--;
            sum+=(j);
        }
        ans[0]+=words[i];
         while(ans[0].length()!=maxWidth)
            ans[0]+=" ";
        int ii;
        for(ii=1;ii<j-1;ii++)
        {
            i=help[ii].ff;
            sum=len[help[ii].ss].ss-len[help[ii].ff-1].ss;
            space=help[ii].ss-help[ii].ff;
            while(i!=help[ii].ss)
            {
                ans[ii]+=words[i];
                i++;
                int xx=maxWidth-sum;
                int j;
                for(j=0;j<ceil((double)xx/(double)space);j++)
                {
                    ans[ii]+=" ";
                }
                space--;
                sum+=(j);
            }
            ans[ii]+=words[i];
             while(ans[ii].length()!=maxWidth)
            ans[ii]+=" ";
        }
        ans[ii]+=words[help[ii].ff];
        for(int i=help[ii].ff+1;i<n;i++)
        {
            ans[ii]+=" "+words[i];
        }
        while(ans[ii].length()!=maxWidth)
            ans[ii]+=" ";
        return ans;
    }
};