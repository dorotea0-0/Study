// з24.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <cmath>
#include <locale>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");

    int m, n, k, cen;
    cout << "Введите введите размеры матрицы: ";
    cin >> n >> m;
    cout << "Введите координаты центра: ";
    cin >> k >> cen;
    int** a = new int* [n];
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
    }

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            int dr = abs(row - k);           
            int dc = abs(col - cen);   
            int dist = (dr > dc) ? dr : dc;  
            a[row][col] = dist + 1;          
        }
    }

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            cout << a[row][col] << " ";
        }
        cout << "\n";
    }

    for (int i = 0; i < n; i++) {
        delete[] a[i];
    }
    delete[] a;
    return 0;
}