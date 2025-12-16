// з5.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
#include <iostream>
using namespace std;
int a[10][10];
bool used[10][10];

void sum(int i, int j) {
    if (i < 0 || i >= 10 || j < 0 || j >= 10 || a[i][j] == 0 || used[i][j]) return;
    used[i][j] = true;
    sum(i + 1, j);
    sum(i - 1, j);
    sum(i, j + 1);
    sum(i, j - 1);
}

int main() {
    cout << "Введите массив\n";
    for (int i = 0; i < 10; ++i)
        for (int j = 0; j < 10; ++j)
            cin >> a[i][j];

    int k = 0;
    for (int i = 0; i < 10; ++i)
        for (int j = 0; j < 10; ++j)
            if (a[i][j] == 1 && !used[i][j]) {
                sum(i, j);
                ++k;
            }

    cout << k << endl;
    return 0;
}