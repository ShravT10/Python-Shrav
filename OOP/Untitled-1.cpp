#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    char a;
    ofstream file;
    file.open("MyFile");
    file<<"M";
    file.close();

    ifstream file1;
    file1.open("MyFile");
    
    file1>>a;
    cout<<a;

}