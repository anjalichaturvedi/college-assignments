#include <iostream>

using namespace std;

int main()
{
    int arr[10];
    int pos, i, num;
    cout << "Enter number of elements in an array: ";
    cin >> num;
    cout << "Enter elements: ";
    for (i=0; i<num; i++) {
        cin >> arr[i];
    }
    cout << "Enter the position: ";
    cin >> pos;
    for (i=pos-1; i<num-1; i++) {
        arr[i]=arr[i+1];
    }
    num--;
    cout << "Array after deletion: " << endl;
    for (i=0; i<num; i++) {
        cout << arr[i] <<endl;
    }
    return 0;
}
