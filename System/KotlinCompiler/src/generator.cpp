#include "generator.hpp"
#include <fstream>
#include <iostream>
#include <string>
#include <regex>
#include <map>

using namespace std;

map<string, string> typeMapping = {
    {"Int8", "Byte"},
    {"Int16", "Short"},
    {"Int32", "Int"},
    {"Int64", "Long"},
    {"UInt8", "UByte"},
    {"UInt16", "UShort"},
    {"UInt32", "UInt"},
    {"UInt64", "ULong"},
    {"Float32", "Float"},
    {"Float64", "Double"},
    {"Text", "String"},
    {"Bool", "Boolean"}
};


string replaceCapnpTypeWithKotlin(const string &text) {
    string result = text;
    for (const auto &pair : typeMapping) {
        regex typeRegex(R"(\b)" + pair.first + R"(\b)");
        result = regex_replace(result, typeRegex, pair.second);
    }
    return result;
}


string getReturnType(const string &returnValue) {
    size_t colonPos = returnValue.find(':');
    
    string type = (colonPos != string::npos) ? returnValue.substr(colonPos + 1) : returnValue;
    
    // Remove leading spaces
    type = regex_replace(type, regex(R"(^\s+)"), "");
    
    return replaceCapnpTypeWithKotlin(type);
}


void generateKotlinCode(const Interface &interfaceData, const string &outputFilename) {
    ofstream kotlinFile(outputFilename);
    if (!kotlinFile.is_open()) {
        cerr << "Fehler: Konnte die Datei " << outputFilename << " nicht \u00F6ffnen." << endl;
        return;
    }

    // Generate the Kotlin interface
    kotlinFile << "interface " << interfaceData.name << " {\n";
    for (const auto &method : interfaceData.methods) {

        string parameters = replaceCapnpTypeWithKotlin(method.parameters);
        string returnType = getReturnType(method.returnType);

        kotlinFile << "    fun " << method.name << "(" << parameters << "): " << returnType << "\n";
    }
    kotlinFile << "}\n";

    kotlinFile.close();
    cout << "Kotlin-Code erfolgreich generiert: " << outputFilename << endl;
}


