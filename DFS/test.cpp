#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <stack>
#include <iomanip>

using namespace std;

map<char, vector<char>> graph;

void readData() {
    ifstream inputFile("D:\\Nam3Ky2\\AI\\NHOM_08\\input.txt");
    if (!inputFile.is_open()) {
        cerr << "Error opening input.txt. Make sure the file exists and you have the necessary permissions." << endl;
        return;
    }

    string line;
    while (getline(inputFile, line)) {
        char node = line[0];
        if (graph.find(node) == graph.end())
            graph[node] = vector<char>();

        for (size_t i = 2; i < line.size(); i += 2)
            graph[node].push_back(line[i]);
    }

    inputFile.close();
}

void DFS(char s, char f) {
    ofstream outputFile("output.txt");
    if (!outputFile.is_open()) {
        cerr << "Error opening output file." << endl;
        return;
    }

    outputFile << left << setw(10) << "PTTT" << " | " << setw(15) << "Trang thai Ke" << " | " << setw(25) << "Danh sach Q" << " | " << setw(25) << "Danh sach L" << endl;
    outputFile << string(85, '-') << endl;

    stack<pair<char, vector<char>>> st;
    st.push(make_pair(s, vector<char>{s}));
    map<char, int> d;
    d[s] = 0;

    while (!st.empty()) {
        char x;
        vector<char> v;
        tie(x, v) = st.top();
        st.pop();

        if (x == f) {
            string res;
            for (const char &c : v)
                res += "->" + string(1, c);
            outputFile << left << setw(10) << string(1, x) << " | " << setw(15) << "TTKT-Dung" << " | " << setw(25) << "" << " | " << setw(25) << "" << endl;
            outputFile << d[x] << ": " << res.substr(2) << endl;
            break;
        }

        if (graph.find(x) != graph.end()) {
            string tt, Q, L;
            for (const char &c : graph[x]) {
                tt += ", " + string(1, c);
                if (d.find(c) == d.end()) {
                    st.push(make_pair(c, v));
                    st.top().second.push_back(c);
                    d[c] = d[x] + 1;
                }
            }

            for (const auto &entry : d)
                Q += ", " + string(1, entry.first);

            stack<pair<char, vector<char>>> st_copy = st; // Create a copy of the stack to iterate over its elements
            while (!st_copy.empty()) {
                L += ", " + string(1, st_copy.top().first);
                st_copy.pop();
            }

            outputFile << left << setw(10) << string(1, x) << " | " << setw(15) << tt.substr(2) << " | " << setw(25) << Q.substr(2) << " | " << setw(25) << L.substr(2) << endl;
        }
    }

    outputFile.close();
}

int main() {
    readData();
    DFS('A', 'G');
    return 0;
}