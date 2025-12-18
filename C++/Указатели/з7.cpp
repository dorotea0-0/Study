// з7.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");
    int n;
    cout << "Введите количество элементов в массиве: ";
    cin >> n;

    char* arr = new char[n];
    char* in = arr;
    cout << "Введите элементы массива: ";
    for (int i = 0; i < n; i++, in++) {
        cin >> *in;
    }

    char* read = arr;
    char* write = arr;

    while (read < arr + n){
        if (read == arr || *read != *(read - 1)) {
            *write = *read;
            write++;
        }
        read++;
    }

    int r = write - arr;
    cout << "Массив на выходе: ";
    char* out = arr;
    for (int i = 0; i < r; i++, out++) {
        cout << *out << " ";
    }

    delete[] arr;
}

