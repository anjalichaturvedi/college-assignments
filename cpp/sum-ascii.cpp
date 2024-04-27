#include <iostream>

using namespace std;

int main(){
    string str;
    int sum, i;
    cout << "Enter string: ";
    cin >> str;
    for (i = 0; str[i] != '\0'; i++) //also while
        sum = sum + str[i];
    cout << "Sum of ASCII value : " << sum;
    return 0;
}
