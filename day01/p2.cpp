#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str, num;
    int ans = 0;
    char digit;

    auto decode_digit = [&](string str, bool rev) -> char {
        if (!rev) {
            if (str == "one")
                return '1';
            else if (str == "two")
                return '2';
            else if (str == "three")
                return '3';
            else if (str == "four")
                return '4';
            else if (str == "five")
                return '5';
            else if (str == "six")
                return '6';
            else if (str == "seven")
                return '7';
            else if (str == "eight")
                return '8';
            else if (str == "nine")
                return '9';
        } else {
            if (str == "eno")
                return '1';
            else if (str == "owt")
                return '2';
            else if (str == "eerht")
                return '3';
            else if (str == "ruof")
                return '4';
            else if (str == "evif")
                return '5';
            else if (str == "xis")
                return '6';
            else if (str == "neves")
                return '7';
            else if (str == "thgie")
                return '8';
            else if (str == "enin")
                return '9';
        }

        return '0';
    };

    auto solve = [&](string str, bool rev) -> void {
        for (int i = 0; i < str.size(); i++) {
            if ('0' <= str[i] && str[i] <= '9') {
                num += str[i];
                break;
            }
            if (i + 3 <= str.size()) {
                if ((digit = decode_digit(str.substr(i, 3), rev)) > '0') {
                    num += digit;
                    break;
                }
            }
            if (i + 4 <= str.size()) {
                if ((digit = decode_digit(str.substr(i, 4), rev)) > '0') {
                    num += digit;
                    break;
                }
            }
            if (i + 5 <= str.size()) {
                if ((digit = decode_digit(str.substr(i, 5), rev)) > '0') {
                    num += digit;
                    break;
                }
            }
        }
    };

    while (cin >> str) {
        num = "";
        solve(str, false);
        reverse(str.begin(), str.end());
        solve(str, true);
        ans += stoi(num);
    }

    cout << ans << '\n';

    return 0;
}