
#include <iostream>
#include <locale>
#include <random>
using namespace std;
int main()
{
    int n,s,d;

    setlocale(LC_ALL, "RU");

    cout << "Введтие число N: ";
    cin >> n;
    cout << "Введите диапазон генерации чисел (от и до): ";
    cin >> s >> d;
    int m = n;

    int* rand=new int[n*n];
    int** arr = new int* [n];

    for (int i = 0; i < m; i++) {
        arr[i] = new int[m];
    }

    for (int i = 0; i < n * n; i++) {
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<int> dis(s, d);
        rand[i] = dis(gen);
    }

    for (int i = 0; i < n * n - 1; ++i) {
        for (int j = 0; j < n * n - 1 - i; ++j) {
            if (rand[j] > rand[j + 1]) {
                int temp = rand[j];
                rand[j] = rand[j + 1];
                rand[j + 1] = temp;
            }
        }
    }

    int index = 0;
    int top = 0, bottom = n - 1;
    int left = 0, right = n - 1;

    while (top <= bottom && left <= right) {
        for (int j = left; j <= right; ++j)
            arr[top][j] = rand[index++];
        top++;

        for (int i = top; i <= bottom; ++i)
            arr[i][right] = rand[index++];
        right--;

        if (top <= bottom) {
            for (int j = right; j >= left; --j)
                arr[bottom][j] = rand[index++];
            bottom--;
        }

        if (left <= right) {
            for (int i = bottom; i >= top; --i)
                arr[i][left] = rand[index++];
            left++;
        }
    }
    cout << "\nМатрица, заполненная по спирали:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout.width(5);
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }

    for (int i = 0; i < n; i++) {
        delete[] arr[i];
    }
    delete[] arr;
    delete[] rand;
}