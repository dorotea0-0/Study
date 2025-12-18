// з2.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");
    char in[80 + 1];
    char out[80 + 1];

    cout << "Введите строку (до 80): ";

    char* start = in;
    char* end = in+80;
    char ch;

    while (start < end && (ch = cin.get()) != '\n') {
        *start = ch;
        start++;
    }
    *start = '\0';
    
    char* inp = in;
    char* outp = out;

    while (*inp == ' ') {
        inp++;
    }

    int k = 0;
    while (*inp != '\0') {
        if (*inp == ' ') {
            if (!k) {
                *outp = ' ';
                outp++;
                k = 1;
            }
        }
        else {
            *outp = *inp;
            outp++;
            k = 0;
        }
        inp++;
    }
    if (outp > out && *(outp - 1) == ' ') {
        outp--;
    }
    *outp = '\0';

    cout << "Новая строка: " << out;
}
