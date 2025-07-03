#include<iostream>
using namespace std;
int x=10;
class w
{
    public:
    int x=5;
    void print(){
    cout<<x;
    cout<<::x;
    }
};


int main()
{
    
    w s;
    s.print();
}