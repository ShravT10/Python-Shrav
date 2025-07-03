#include<iostream>
using namespace std;
class point
{
    public:
    int x,y;
    
    point(){ x = 0; y = 0; }
    point(int i , int j){ x = i; y = j; }
    void get_xy( int &i , int &j){ i = x; j = y;}
    point operator-();
};
point point::operator-()
{
    x=-x;
    y=-y;
    return *this;
}

int main()
{
    point obj(10,10);
    int x,y;
    obj.get_xy(x,y);
    obj=-obj;
    obj.get_xy(x,y);
    cout<<"USE OF UNARY OP IS"<<endl;   
    cout<<"X : "<<x<<y;
    return 0;

}