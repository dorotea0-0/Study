#include <iostream>
#include<locale>
using namespace std;

int main(void)
{
    setlocale(LC_ALL, "RU");

    int n;
    cout << "Введите количество битов" << endl;
    cin >> n;

    int a[100], a1[100];

    cout << "Введите биты числа" << endl;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        a1[i] = a[n - 1 - i];
    }
    int plus = 1;

    for (int i = 0; i < n; i++) {
        int sum = a1[i] + plus;
        a1[i] = sum % 2;
        plus = sum / 2;
    }
    if (plus == 1) {
        a1[n] = 1;
        n++;
    }
    cout << "Результат сложения: ";
    for (int i = n - 1; i >= 0; i--)
        cout << a1[i];

    return 0;
}