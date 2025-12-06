#include <iostream>
using namespace std;

int main(void)
{
    int n = 10000;
    for (int i = 999; i < n; i++) {
        int num[4];
        num[0] = i / 1000;
        num[1] = (i / 100) % 10;
        num[2] = (i / 10) % 10;
        num[3] = i % 10;

        bool n = true;

        for (int j = 0; j < 4; j++) {
            for (int k = j + 1; k < 4; k++) {
                if (num[j] == num[k]) {
                    n = false;
                    break;
                }
            }
        }
        if (n == true)
            cout << i << endl;
    }
    return 0;
}