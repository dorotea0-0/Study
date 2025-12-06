#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");

    int n;
    cout << "Введите размер массива: ";
    cin >> n;
    int* arr = new int[n];

    cout << "Введите ряд чисел(через пробел): ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int now=0, max=0;
    for (int i=0; i<n; i++){
        if (arr[i] == 0) {
            ++now;
            if (now>max){
                max = now;
            }
        }
        else {
            now = 0;
        }
    }
    cout << max;
    delete[] arr;
}
