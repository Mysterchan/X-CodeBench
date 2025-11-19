#include <iostream>
#include <string>

int main() {
    std::string S;
    std::cin >> S; // Read the entire string input

    std::string result; // Prepare to collect the '2's
    for (char c : S) { // Iterate through each character in the string
        if (c == '2') { // Check if the character is '2'
            result += c; // Concatenate '2' to the result string
        }
    }

    std::cout << result << std::endl; // Output the final result
    return 0;
}