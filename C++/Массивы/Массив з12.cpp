#include <iostream>
#include <locale>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите размер массива: ";
    cin >> n;
    int* A = new int[n];
    cout << "Введите ряд чисел(через пробел): ";
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int len = 1;

    for (int cen = 0; cen < n; ++cen) {
        int left = cen, right = cen;
        while (left >= 0 && right < n && A[left] == A[right]) {
            if (right - left + 1 >len) {
                len = right - left + 1;
            }
            --left;
            ++right;
        }

        left = cen;
        right = cen + 1;
        while (left >= 0 && right < n && A[left] == A[right]) {
            if (right - left + 1 > len) {
                len = right - left + 1;
            }
            --left;
            ++right;
        }
    }

    cout << len << endl;

    delete[] A;
    return 0;
}