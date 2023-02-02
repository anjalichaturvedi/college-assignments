#include <iostream>

using namespace std;

int main()
{
    int i, maximum;
    int arr[5]={5,7,8,12,32};
    maximum=arr[0];
    for (i=1; i<5; i++) 
    {
        if (arr[i]>maximum) 
        {
            maximum=arr[i];
        }
    }
    cout << maximum;
    return 0;
}
