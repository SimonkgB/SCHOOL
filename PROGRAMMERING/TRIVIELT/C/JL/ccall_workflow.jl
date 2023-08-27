####################
# 2 methods to use c in julia
#########################
#option 1:
#=
using Libdl

lib = dlopen("libworkflow")

func = dlsym(lib, "myadd")

x = y = 0

function myadd(x, y)    # function can have any name this is randomly teh same as in the ccode and dll
    ccall(func, Cint, (Cint, Cint), x,y)    # Cint er data typen til C fila (Cflaot, Cint etc..)
end                                             # (Cint, Cint) er variablene fra C funksjonen

#we can now use the C code in julia

myadd(2,3)
myadd(-7, 4)
myadd(0.1, 0.2) # doesnt work since C has teh variables int x and int y
=#

#option 2:

using Libdl

lib = dlopen("libworkflow")

func = dlsym(lib, "myadd")

x = y = 0

function myadd(x, y)    # function can have any name this is randomly teh same as in the ccode and dll
    @ccall $func(x::Cint, y::Cint)::Cint    # Cint er data typen til C fila (Cflaot, Cint etc..)
end                                             # (Cint, Cint) er variablene fra C funksjonen

#we can now use the C code in julia

myadd(2,3)
myadd(-7, 4)
myadd(0.1, 0.2) # doesnt work since C has teh variables int x and int y