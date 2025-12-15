// з15.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");
    int n;

    cout << "Введите размер массива: ";
    cin >> n;

    int* a = new int[n];
    cout << "Введите значения массива: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int max = 1;
    int result = a[0];

    for (int i = 0; i < n; i++) {
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (a[i] == a[j]) {
                count++;
            }
        }
        if (count > max) {
            max = count;
            result = a[i];
        }
    }

    cout << "Число, повторяющееся чаще всего: " << result << endl;


    delete[] a;
}
