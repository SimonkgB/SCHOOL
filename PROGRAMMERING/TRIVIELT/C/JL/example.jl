using Libdl

lib = dlopen("libexample")

func = dlsym(lib, "myswitch")

function compass(direction)
    ccall(func, Cvoid, (Cint,), direction)
end

compass(1)
compass(2)
compass(3)
compass(4)
compass(5)

function compass1(direction)
    @ccall $func(direction::Cint)::Cvoid
end

compass1(1)