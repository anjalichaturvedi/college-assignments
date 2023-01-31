#include <iostream>

using namespace std;

int main(){
    int i,j;
    string temp;
    string name[2][2]=
    {
        {"Sachin", "Dixit"},
        {"Aman", "Srivastava"}   };
    name[0][1]="Srivastava";
    name[1][1]="Dixit";
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << name[i][j] << "\n";
    }
}
    return 0;
}
