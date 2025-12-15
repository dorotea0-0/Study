#include <locale>
#include <iostream>
using namespace std;
void QuickSort(int* arr, int first, int last, int k) {
    if (first >= last) return;

    int i = first, j = last;
    int comp = arr[(first + last) / 2];
    do {
        while (arr[i] < comp && i < last) i++;
        while (arr[j] > comp && j > first) j--;

        if (i <= j) {
            if (arr[i] != arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            i++;
            j--;
        }
    } while (i <= j);

    if (k <= j) {
        QuickSort(arr, first, j, k);
    }
    else if (i >= k)
        QuickSort(arr, i, last, k);
}
int main()
{
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите n: ";
    cin >> n;
    cout << "Введите комбинациюне не повторяющихся чисел в количестве равном 2n+1: ";
    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int k = n / 2;
    QuickSort(arr, 0, n - 1, k);

    cout << "Медиана: " << arr[n / 2];
}