//Tran, Thang
//1001-233-804
//2018-03-10

#include <iostream>
#include <fstream>
#include <regex>
using namespace std;

void processToken(string token) {
    regex isID("^[a-mN-Z_][n-zA-M0-9_]*$");
    regex isInt("^(0d|0D)[0-9]+$");
    regex isnotEFP("^[0-9]+$");
    regex isHexInt("^(0x|0X)[0-9a-fA-F]+$");
    regex isFP("^[0-9]+[\\.][0-9]+$");
    regex isEFP("(([0-9]+\\.)|(\\.[0-9]+)|([0-9]+\\.[0-9]+)|([0-9]+))([eE][-+]?[0-9]+)?$");

    if(regex_match(token,isID)) {
        cout << ">" << token << "< matches ID.\n";
    }else if (regex_match(token,isInt)) {
        cout << ">" << token << "< matches INT.\n";
    }else if (regex_match(token,isnotEFP)) {
        cout << ">" << token << "< does not match.\n";
    }else if (regex_match(token,isHexInt)) {
        cout << ">" << token << "< matches HEXINT.\n";
    }else if (regex_match(token,isFP)) {
        cout << ">" << token << "< matches FP.\n";
    }else if (regex_match(token,isEFP)) {
        cout << ">" << token << "< matches EXP.\n";
    }else {
        cout << ">" << token << "< does not match.\n";
    }    
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        cout << "processing tokens from " << argv[ 1 ] << " ...\n";
        ifstream inputFile;
        string token;

        inputFile.open(argv[ 1 ]);

        if (inputFile.is_open()) {
            for (inputFile >> token; !inputFile.eof(); inputFile >> token) {
                processToken(token);
            }
            inputFile.close();
        } else {
            cout << "unable to open " << argv[ 1 ] << "?\n";
        }
    } else {
        cout << "No input file specified.\n";
    }
}
