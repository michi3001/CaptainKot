#include "parser.hpp"
#include <fstream>
#include <regex>
#include <iostream>

using namespace std;

Interface parseCapnpFile(const string &filename) {
    Interface parsedInterface;
    ifstream file(filename);
    string line;
    regex interfaceRegex(R"(interface\s+(\w+))");
    regex methodRegex(R"((\w+)\s+@\d+\s*\(([^)]*)\)\s*->\s*\(([^)]*)\))");
    smatch match;

    if (!file.is_open()) {
        cerr << "Fehler: Konnte die Datei " << filename << " nicht öffnen." << endl;
        return {};  // Return empty interface
    } else {
        cout << "Datei " << filename << " erfolgreich geöffnet." << endl;
    }

    while (getline(file, line)) {
        // Search for the interface definition
        if (regex_search(line, match, interfaceRegex)) {
            parsedInterface.name = match[1];
        }
        // Search for method definitions
        else if (regex_search(line, match, methodRegex)) {
            Method method;
            method.name = match[1];
            method.parameters = match[2];
            method.returnType = match[3];
            parsedInterface.methods.push_back(method);
        }
    }

    return parsedInterface;
}