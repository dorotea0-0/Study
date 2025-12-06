
#include <iostream>
#include <locale>
using namespace std;

int main()
{
    setlocale(LC_ALL, "RU");
    int n, m, s=0, f;
    cout << "Введите размеры двумерного массива(через пробел): ";
    cin >> n >> m;

    int** arr = new int* [n];
    for (int i = 0; i < n; i++) {
        arr[i] = new int[m];
    }
    
    for (int i = 0; i < n; i++) {
        cout << "Строка " << i + 1 << ": ";
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    int* coord = new int[n + m]();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 0) {
                coord[i] = 1;
                coord[n + j] = j;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (coord[i] == 1 || coord[n + j] == 1) {
                arr[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
        
    for (int i = 0; i < n; i++) {
        delete[] arr[i];
    }

    delete[] coord;
    delete[] arr;

}
