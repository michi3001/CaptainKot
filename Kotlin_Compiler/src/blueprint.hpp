#pragma once
#include <string>
#include <vector>

using namespace std;

struct Method {
    string name;
    string parameters;
    string returnType;
};

struct Interface {
    string name;
    vector<Method> methods;
};