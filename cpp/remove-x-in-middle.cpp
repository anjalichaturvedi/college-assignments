#include <iostream>
#include<algorithm>

using namespace std;

int main() {
   string str = "hxxjghji";
   string str1="";
   string str2="";
   int len=str.length();
   int i;
   cout << "Length of the string: " << len << endl;
   cout << "Initial string: " << str << endl;
   if (str[0]=='x' || str[len]=='x')
    {
        str.erase(remove(str.begin()+1, str.end()-1, 'x'), str.end()-1);
        str1=str;
    }
    else
    {
        str.erase(remove(str.begin(), str.end(), 'x'), str.end());
        str1=str;

    }
   cout << "Final string: " << str1;
   return 0;
}
