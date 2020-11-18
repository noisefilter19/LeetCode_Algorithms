/* Trie or Prefix Tree is a data structure with
which you can make fast dictionary of words and 
search which word is in it or isn't 
Time complexity:
Insert: O(n)
Check: O(n)
Remove: O(n)
Where n is the length of given string
*/

#include <bits/stdc++.h>

using namespace std;

struct Trie
{
    int childrenC;
    Trie* children[30];
    bool endOfWord;
    Trie()
    {
        this->childrenC=0;
        this->endOfWord=false;
        for(int i=0;i<30;i++)
        {
            this->children[i]=NULL;
        }
    }
};
void Insert(Trie *&root, string word)
{
    Trie* tmp = root;
    for(int i=0;i<word.size();i++)
    {
        if(tmp->children[word[i]-'a']==NULL)
        {
           tmp->childrenC++;
           tmp->children[word[i]-'a']=new Trie(); 
        }
        tmp=tmp->children[word[i]-'a'];
        if(i==word.size()-1)
        {
             tmp->endOfWord=true;
        }
    }
}
bool Check(Trie *root, string word)
{
    bool result=true;
    for(int i=0;i<word.size();i++)
    {
        if(root->children[word[i]-'a']==NULL)
        {
            result=false;
            break;
        } 
        root = root->children[word[i]-'a'];
        if(i==word.size()-1)
        {
            result = root->endOfWord;
        }
    }
    return result;
}
bool RemoveAPI(Trie* &cur,string word,int idx)
{
    if(cur==NULL)return false;
    if(idx==word.size())
    {
        cur->endOfWord=false;
    }
    else
    {
        bool result = RemoveAPI(cur->children[word[idx]-'a'],word,idx+1);
        if(result)
        {
            cur->childrenC--;
            delete cur->children[word[idx]-'a'];
        }
    }
    return cur->childrenC==0;
}
void Remove(Trie* &root,string word)
{
    RemoveAPI(root,word,0);
}
int main()
{
    //Driver code.
    Trie* root = new Trie();
    Insert(root,"test");
    Insert(root,"testa");
    cout<<Check(root,"test")<<endl;
    cout<<Check(root,"tes")<<endl;
    Remove(root,"testa");
    cout<<Check(root,"testa")<<endl;
    cout<<Check(root,"test")<<endl;
}