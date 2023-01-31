#include <iostream>

using namespace std;

int main()
{
    int n, x, y;
    char a=65;
    cout << "Enter number of rows: ";
    cin >> n;
    for (x=1; x<=n; x++)
    {
        for (y=1; y<=x; y++) {
            cout << (char)(a+y-1);
        }
        cout << "\n";
    }
    return 0;
}
