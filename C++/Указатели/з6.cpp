// з6.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale> 
#include <time.h>
#include <random> 
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");

    int seed = time(NULL);
    srand(seed);

    int a[1000] = { 0 };
    int* in = a;
    int* end = a + 1000;

    int f = rand() % 1000;
    for (int* p=a; p<a+f; p++) {
        *p= 1+rand()%9;
    }

    while (in < end) {
        int* mid = in + (end - in) / 2;
        if (*mid != 0) {
            in = mid + 1;
        }
        else {
            end = mid;
        }
    }

    cout << "Количество ненулевых элементов: "<<in-a;
}

