//수 정렬하기

#include <iostream>
using namespace std;

int main() {
    int input;
    cin >> input;
    int list[input];
    for (int i = 0; i < input; i++) {
        cin >> list[i];   
    }

    for (int j = 1; j < input; j++) {
        int key = list[j];
        int i = j - 1;
        while (i >= 0 && list[i] > key) {
            list[i + 1] = list[i];
            i--;
        }
        list[i + 1] = key;
    }

    for (int i = 0; i < input; i++) {
        cout << list[i] << endl;
    }
}
