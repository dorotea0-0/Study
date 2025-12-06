#include <iostream>
#include <clocale>

using namespace std;

int main()
{
    const int m = 10;
    int arr[m];
    int max_len = 0;

    for (int i = 0; i < m; i++)
        cin >> arr[i];

    for (int i = 1; i < m; i++)
    {
        if (arr[i] - arr[i - 1] == 1)
            max_len++;
    }
    cout << max_len;
    return 0;
}