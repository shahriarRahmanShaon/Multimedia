#include <bits/stdc++.h>
#define pdd pair<long double,long double>
using namespace std;

int width = 14;
map<char,pdd> Range;

long double generateCodeword(long double low, long double high){
    long double x = 0.5 , code = 0.0;

    while(code < low){
        if(code + x <= high)
            code = code + x;
        x /= 2.0;
    }

    return code;
}

long double doEncode(string str){

    long double low = 0.0 , high = 1.0 , range = 1.0;

    for(int i = 0 ; i < width ; i++){
        high = low + range * Range[str[i]].second;
        low = low + range * Range[str[i]].first;
        range = high - low;

        if(str[i] == '$')
            break;
    }

    long double codeword = generateCodeword(low,high);
    return codeword;

}
int main(){
    ifstream in("./input.txt");
    ofstream out("./enc.txt");

    out<<fixed<<setprecision(20);

    char ch;
    string str, tmp;
    map<char,int>freq;
    long double low = 0.0;

    while(in.get(ch)){
        if(ch == '\n')
            ch = '-';
        str += ch , freq[ch]++;
    }
    
    for(int i = 0 ; i < str.size() ; i++){
        long double p = (long double)freq[str[i]] / (long double)str.size();
        if(freq[str[i]] != 0){
            Range[str[i]] = {low,low+p};
            out<<str[i]<<' '<<low<<' '<<low+p<<endl;
            low = low + p;
            freq[str[i]] = 0;
        }
    }

    for(int i = 0 ; i < str.size() ; i += width){
        tmp = "";
        for(int j = 0 ; j < width && i + j < str.size() ; j++){
            tmp += str[i+j];
        }
        long double codeword= doEncode(tmp);
        out<<codeword<<endl;
    }

    in.close();
    out.close();

    return 0;
}