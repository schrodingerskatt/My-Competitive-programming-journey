// Problem Link : https://codeforces.com/problemset/problem/266/B

#include<bits/stdc++.h>
using namespace std;

int main(){
int n;
int t;
cin>>n>>t;
string s; 
cin>>s;
while(t--){
for(int i = 0; i < n-1;){
if(s[i] == 'B'&& s[i+1]=='G'){
swap(s[i],s[i+1]);
i+=2;
}else{
i++;
}
}
}
cout<<s<<"\n";
return 0;
}