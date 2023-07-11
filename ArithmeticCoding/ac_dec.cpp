#include <bits/stdc++.h>
#define pdd pair<long double,long double>
using namespace std;

int width = 14;
map<string,pdd> Range;

string doDecode(long double code){

    long double low, high, range;
    string ans , s;

    for(int i = 0 ; i < width ; i++){
       for(auto &itr: Range){
            if(itr.second.first <= code && code < itr.second.second){
                s = itr.first;
                low = itr.second.first;
                high = itr.second.second;
                range = high - low;
                code = (code - low) / range;
                break;
            }
       }
        if(s == "$")
            break;
        
        if(s == "-")
            ans += '\n';
        else
            ans += s;
    }

    return ans;

}
int main(){
    ifstream in("./enc.txt");
    ofstream out("./dec.txt");

    cout<<fixed<<setprecision(20);

    char ch;
    string str, tmp;
    bool codeSection = false;
    vector < string > separator;

    while(getline(in,str)){
        if(!codeSection){
            separator.clear();

            stringstream ss(str);
            while(ss >> tmp)
                separator.push_back(tmp);
            
            if(separator.size() == 2)
                separator.insert(separator.begin()," ");
            
            Range[separator[0]] = {stold(separator[1]),stold(separator[2])};
            
            if(str[0] == '$')
                codeSection = true;
        }
        else{
            long double code = stold(str);
            out<<doDecode(code);
        }

    }

    in.close();
    out.close();

    return 0;
}