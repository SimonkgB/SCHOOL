filename = "Hello.cxx"

lib = "libHello"

func = :hello

using CxxCall
eval(cxxsetup())

eval(cxxnewfile(filename,
    """
    #include <iostream>
    using namespace std;
    """

))

@cxx lib function $func(s::Cstring)::Cvoid
    """
    cout << "hello, " << s << "!" << endl;
    """
end

Cxx_write_code!()