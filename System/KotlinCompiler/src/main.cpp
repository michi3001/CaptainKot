#include "parser.hpp"
#include "generator.hpp"
#include <iostream>
#include <fstream>
#include <sstream>
#include <filesystem>

using namespace std;

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cerr << "Verwendung: " << argv[0] << " <schema.capnp>" << endl;
        return 1;
    }

    string filename = argv[1];

    // Step 1: Analyze the .capnp file
    Interface parsedInterface = parseCapnpFile(filename);

    // Step 2: Generate Kotlin code
    string outputDir = "output";
    if (!filesystem::exists(outputDir)) {
        filesystem::create_directory(outputDir);
    }
    string outputFilename = outputDir + "/" + parsedInterface.name + ".kt";
    generateKotlinCode(parsedInterface, outputFilename);
    
    return 0;
}