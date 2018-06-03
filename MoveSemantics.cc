#include <iostream>
#include <cstring>

using namespace std;

class MyString
{
public:
    char *data;
    MyString(const char* _data)
    {
        int size = strlen(_data) + 1;
        data = new char[size];
        memcpy(data, _data, size);
    }

    ~MyString()
    {
        delete [] data;
    }

    // Copy constructor
    MyString(const MyString& other)
    {
        cout << "Copy constructor called." << endl;
        int size = strlen(other.data) + 1;
        data = new char[size];
        memcpy(data, other.data, size);
    }

    // Move constructor
    // To get this called, disable compiler's RVO
    // "-fno-elide-constructors"
    MyString(MyString&& other)
    {
        cout << "Move constructor called." << endl;
        data = other.data;
        other.data = nullptr;
    }

    // Operator + overloading
    MyString operator+(const MyString &rhs)
    {
        cout << "operator+ called." << endl;
        char* result = new char[100];
        strcpy(result, data);
        strcat(result, rhs.data);
        MyString newString(result);
        return newString;
    }
};

int main()
{
    MyString x("Hello");
    MyString y("World");
    MyString a(x);
    MyString b(x + y);
    return 0;
}
