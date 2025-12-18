// з3.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");
    int arr[80];
    cout << "Введите массив(до 80 чисел, завершите ввод Ctrl+Z или некорректным значением): ";
    for (int* p = arr; p < arr + 80; p++) {
        cin >> *p;
    }

    int max=0, k = 0, t=0;
    for (int* p = arr; p < arr + 80; p++) {
        for (int* j = arr; j < arr + 80; j++) {
            if (*p >= 0 && *p == *j && *p < 10) {
                k++;
            }
        }
        if (max < k) {
            max = k;
            t = *p;
        }
        k = 0;
    }
    if (max != 0) {
        cout << t;
    }
    else {
        cout << "В массиве нет цифр";
    }
}

