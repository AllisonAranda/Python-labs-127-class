//Name: Allison
//Email: allison.aranda48@myhunter.cuny.edu
//Date: May 10,2022
//This program prints 

#include <iostream>
using namespace std;

int main()
{
    int yearborn;
    cout<<"Enter your year born:";
    cin>>yearborn;
    
    while  (yearborn>2018)
    {
        cout<<"Please enter year born:";
        cin>>yearborn;
    }
    cout<<"You enter:"<<yearborn<<endl;
    return 0;
    
}
