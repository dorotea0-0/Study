// з16.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");

    int n, m;
    cout << "Введите число строк и колонок: ";
    cin >> n>> m;

    int** arr = new int* [n];
    for (int i = 0; i < n; i++) {
        arr[i] = new int[m];
    }

    cout << "Заполните массив: \n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    int found = 0;
    for (int j = 0; j < m; j++) {
        int cand = arr[0][j];
        int all = 1;

        for (int i = 1; i < n; i++) {
            int row = 0;
            for (int k = 0; k < m; k++) {
                if (arr[i][k] == cand) {
                    row = 1;
                    break;
                }
            }
            if (row == 0) {
                all = 0;
                break;
            }
        }

        if (all == 1) {
            cout << cand << endl;
            found = 1;
            break;
        }
    }

    if (found == 0) {
        cout << "НЕТ" << endl;
    }

    for (int i = 0; i < n; i++) {
        delete[] arr[i];
    }
    delete[] arr;

    return 0;
}
