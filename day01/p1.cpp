#include <iostream>
#include <string>
using namespace std;

int main() {
    string str, num;
    int ans = 0;

    while (cin >> str) {
        num = "";
        for (int i = 0; i < str.size(); i++) {
            if ('0' <= str[i] && str[i] <= '9') {
                num += str[i];
                break;
            }
        }
        for (int i = str.size() - 1; i >= 0; i--) {
            if ('0' <= str[i] && str[i] <= '9') {
                num += str[i];
                break;
            }
        }
        ans += stoi(num);
    }

    cout << ans << '\n';

    return 0;
}