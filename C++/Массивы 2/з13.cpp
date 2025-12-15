// з13.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
#include <locale>
#include <iostream>
using namespace std;
void QuickSort(int* arr, int first, int last) {
    if (first >= last) return;

    int i = first, j = last;
    int comp = arr[(first + last) / 2];
    do {
        while (arr[i] < comp &&) i++;
        while (arr[j] > comp &&) j--;

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
        QuickSort(arr, first, j);
    if (i < last)
        QuickSort(arr, i, last);
}
int main()
{
    setlocale(LC_ALL, "RU");
    int arr[5];
    cout << "Введите комбинацию число: ";
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }
    QuickSort(arr, 0, 4);

    int freq[5] = { 0 };
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (arr[j] == arr[i]) {
                freq[i]++;
            }
        }
    }
    
    int max1 = 0, max2 = 0;

    for (int i = 0; i < 5; i++) {
        if (freq[i] > max1) {
            max1 = freq[i];
        }
    }

    for (int i = 0; i < 5; i++) {
        if (freq[i] > max2 && freq[i] < max1) {
            max2 = freq[i];
        }
    }

    int sig = max1 * 10 + max2;
    switch (sig) {
    case 50: cout << 1 << endl; break;
    case 41: cout << 2 << endl; break;
    case 32: cout << 3 << endl; break;
    case 31: cout << 4 << endl; break;
    case 22: cout << 5 << endl; break; 
    case 21: cout << 6 << endl; break;
    default: cout << 7 << endl;
    }

}
