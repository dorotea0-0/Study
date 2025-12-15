#include <iostream>
#include <locale>
using namespace std;

int main() {
    int n;
    cout << "Введите размер массивов: ";
    cin >> n;

    int* x = new int[n];
    int* y = new int[n];
    cout << "Введите массив X: ";
    for (int i = 0; i < n; i++)
        cin >> x[i];
    cout << "Введите массив Y: ";
    for (int i = 0; i < n; i++)
        cin >> y[i];

    int found = 0;

    for (int i = 0; i < n; i++) {
        for (int k = 1; k <= n - i; k++) {
            int match = 1;
            for (int j = 0; j < k; j++) {
                if (x[i + j] != y[j]) {
                    match = 0;
                    break;
                }
            }
            if (match) {
                found = 1;
                break;
            }
        }
        if (found) break;
    }

    if (found)
        cout << "ДА" << endl;
    else
        cout << "НЕТ" << endl;

    return 0;
}