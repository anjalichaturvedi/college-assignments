#include <iostream>

using namespace std;

int main() {
  int i, n;
  cout << "Enter a number: ";
  cin >> n;
  switch(n%2)
    {
        case 0:
            printf("Number is even");
            break;
        case 1:
            printf("Number is odd");
            break;
    }

  return 0;
}
