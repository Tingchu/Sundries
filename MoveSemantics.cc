#include <iostream>
#include <cstring>

using namespace std;

class MyString
{
public:
    char *data;
    MyString(const char* _data)
    {
        cout << "  Constructor called." << endl;
        int size = strlen(_data) + 1;
        data = new char[size];
        memcpy(data, _data, size);
    }

    ~MyString()
    {
        cout << "  Destructor called" << endl;
        delete [] data;
    }

    // Copy constructor
    MyString(const MyString& other)
    {
        cout << "  Copy constructor called." << endl;
        int size = strlen(other.data) + 1;
        data = new char[size];
        memcpy(data, other.data, size);
    }

    // Move constructor
    // To get this called, disable compiler's RVO
    // "-fno-elide-constructors"
    // Reference: https://medium.com/@pumbaawithmask/%E4%B8%80%E4%BA%9B%E7%AD%86%E8%A8%98-c-move-semantics-c1c174357f7d
    MyString(MyString&& other)
    {
        cout << "  Move constructor called." << endl;
        data = other.data;
        other.data = nullptr;
    }

    // Operator + overloading
    MyString operator+(const MyString &rhs)
    {
        cout << "  operator+ called." << endl;
        char* result = new char[100];
        strcpy(result, data);
        strcat(result, rhs.data);
        MyString newString(result);
        return newString;
    }
};

int main()
{
    // Constructor
    cout << "Construting x" << endl;
    MyString x("Hello");

    // Constructor
    cout << "Construting y" << endl;
    MyString y("World");

    // Copy constructor (src is lvalue --> copy constructor)
    cout << "Construting a" << endl;
    MyString a(x);

    // Operator+
    // (Constructor in operator+)
    // Move constructor (src is rvalue --> move constructor)
    cout << "Construting b" << endl;
    MyString b(x + y);

    return 0;
}
