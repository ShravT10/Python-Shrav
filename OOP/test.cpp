#include <iostream>
#include <fstream>
using namespace std;
char ans;
class bag
{
    public:
    string color;
    int a;
    string item;
    fstream file;
    file.open("bag.txt");

    void open(){
        a = 1;
        cout<<"you opened the bag!\n";
        cout<<"what item do you want to add?\n";
        cin>>item;
        file<<item;
        cout<<"Your bag now contains the following items: \n";
        
        
    }

    void close(){
        switch(a)
        {
            case 1:
            cout<<"You closed the bag and now youre ready !\n"<<"you have kept "<<item<<" in your bag\n";
            break;
            default:
            cout<<"open the bag bro :)\n";
            break;
        }
    }

};

int main(){ 
    int choice;   
    char ans = 'y';
    bag shrav;
    cout<<"What you wanna do mate ?\n"<<"1.open bag\n"<<"2.close bag\n";
    cin>>choice;
    while(ans== 'y' || ans=='Y'){
    switch(choice)
    {
      case 1:
       shrav.open();
       break;
       case 2:
       shrav.close();
       break;
       default:
       cout<<"choose valid opt\n";
       break;
    }
    cout<<"\n"<<"Do you want to continue?\n";
    cin>>ans;
}

return 0;
}