//수 정렬하기 2

#include <iostream>
using namespace std;

void merge(int list[], int p, int q, int r) {
    int n1 = q - p + 1;
    int n2 = r - q;
    int list1[n1 + 1];
    int list2[n2 + 1];
    for (int i = 0; i < n1; i++) {
        list1[i] = list[p + i];
    }
    for (int j = 0; j < n2; j++) {
        list2[j] = list[q + 1 + j];
    }
    int tmax = ~(1 << 31);
    list1[n1] = tmax;
    list2[n2] = tmax;

    int i = 0;
    int j = 0;
    for (int k = p; k < r + 1; k++) {
        if (list1[i] <= list2[j]) {
            list[k] = list1[i];
            i++;
        } else {
            list[k] = list2[j];
            j++;
        }
    }
}

void mergeSort(int list[], int p, int r) {
    if (p < r) {
        int q = (p + r) / 2;
        mergeSort(list, p, q);
        mergeSort(list, q + 1, r);
        merge(list, p, q, r);
    }
}

int main() {
    int input;
    cin >> input;
    int list[input];
    for (int i = 0; i < input; i++) {
        cin >> list[i];
    }

    mergeSort(list, 0, input - 1);

    for (int j = 0; j < input; j++) {
        cout << list[j] << endl;
    }
}
