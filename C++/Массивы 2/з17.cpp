// з17.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
void quicksort(int* arr, int first, int last) {
    if (first >= last) return;

    int i = first, j = last;
    int comp = arr[(first + last) / 2];
    do {
        while (arr[i] < comp) i++;
        while (arr[j] > comp) j--;

        if (i <= j) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            i++;
            j--;
        }
    } while (i <= j);
    if (first < j)
        quicksort(arr, first, j);
    if (i < last)
        quicksort(arr, i, last);
}
int main()
{
    setlocale(LC_ALL, "RU");
    int n, m;
    cout << "Введите размеры 2 массивов: ";
    cin >> n >> m;

    cout << "Введите массив а: ";
    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cout << "Введите массив b: ";
    int* b = new int[m];
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    int* c = new int[n + m];
    for (int i = 0; i < n + m; i++) {
        c[i] = a[i];
    }
    for (int i = 0; i < n + m; i++) {
        c[n+i] = b[i];
    }

    cout << "Массив с: ";
    quicksort(c, 0, n + m - 1);
    for (int i = 0; i < n + m; i++) {
        cout << c[i]<<" ";
    }

    delete[] a;
    delete[] b;
    delete[] c;
    return 0;
}
