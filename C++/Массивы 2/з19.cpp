// з19.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");

    int n, sum=0;

    cout << "Введите размер массива n*n: ";
    cin >> n;

    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[n];
    }

    cout << "Введите массив:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] < 1 || a[i][j] > n) {
                cout << "Не является";
                return 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            for (int j = k+1; j < n; j++) {
                if (a[i][k] == a[i][j]) {
                    cout << "Дубликат в строке " << i << ": a[" << i << "][" << k << "] = a[" << i << "][" << j << "] = " << a[i][k] << endl;
                    cout << "Не является";
                    return 0;
                }
            }
        }
    }

    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            for (int i = k + 1; i < n; i++) {
                if (a[k][j] == a[i][j]) {
                    cout << "Не является";
                    return 0;
                }
            }
        }
    }

    cout << "Является";

    for (int i = 0; i < n; i++) {
        delete[] a[i];
    }
    delete[] a;
}
