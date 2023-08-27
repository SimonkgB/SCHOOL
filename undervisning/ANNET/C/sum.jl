using Libdl

lib = dlopen("libsum_vektor1")

func = dlsym(lib, "sum")

x = y = 0

function sum(x ,y)
    ccall(func, Cint,(Cint,Cint),x,y)
end

sum(1,3)

# use: gcc -fpic -shared sum_vektor.c -o libsum_vektor.dll to convert to dll