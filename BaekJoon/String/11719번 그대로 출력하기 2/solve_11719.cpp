#include <iostream>

using namespace std;

int main(){
    string str;
    while(true){
        getline(cin, str);
        if(cin.eof())
            break;
        cout << str << endl;
    }
}