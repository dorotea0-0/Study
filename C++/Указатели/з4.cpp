// з4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <locale>
using namespace std;

bool staples(char* s) {
    char st[80];
    char* stk = st - 1;
    char* p = s;

    while (*p != '\0') {
        char c = *p;

        if (c == '(' || c == '{' || c == '[') {
            if (stk - st + 1 >= 80) return false;
            *(++stk) = c;
        }
        else if (c == ')' || c == '}' || c == ']') {
            if (stk < st) return false;

            char last = *(stk--);

            if ((c == ')' && last != '(') ||
                (c == '}' && last != '{') ||
                (c == ']' && last != '[')) {
                return false;
            }
        }
        ++p;
    }
    return (stk < st);
}

int main()
{
    setlocale(LC_ALL, "RU");
    char input[81];

    cout << "Введите  строку: ";
    cin.getline(input, 81);

    if (staples(input)) {
        cout << "Скобки расставлены корректно.";
    }
    else {
        cout << "Скобки расставлены некорректно." << endl;
    }
}