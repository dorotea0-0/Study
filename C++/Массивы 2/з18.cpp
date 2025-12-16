// з18.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");

    int n, m, k=0;
    cout << "Введите размер массив(Минимум 2 на 2): ";
    cin >> n >> m;

    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
    }

    cout << "Введите массив(0, 1, 5 или 11): "<<"\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m - 1; j++) {
            if (a[i + 1][j] + a[i][j + 1] + a[i][j] + a[i + 1][j + 1] == 17) {
                k++;
            }
        }
    }

    cout << k;

    for (int i = 0; i < n; i++) {
        delete[] a[i];
    }
    delete[] a;
}

