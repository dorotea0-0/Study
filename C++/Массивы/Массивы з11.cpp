#include <locale>
#include <iostream>
using namespace std;
int main()
{
    setlocale(LC_ALL, "RU");
    int a[3] = { 0,0,0 };
    int b[3] = { 144,12,1 };
    int n;
    cout << "Сколько пар: ";
    cin >> n;

    while (n > 0)
    {
        for (int i = 0; i < 3; i++)
        {
            while (n >= b[i])
            {
                a[i]++;
                n -= b[i];
            }
        }
    }
    cout << "Коробки: " << a[0] << endl;
    cout << "Связки: " << a[1] << endl;
    cout << "Пары: " << a[2] << endl;

    return 0;
}
