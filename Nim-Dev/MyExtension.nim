include Lua



proc add*( a : int , b:int ): int {.cdecl,exportc,dynlib.} = 
    return a + b*100


proc bind_add(L : PState) :  cint {.cdecl,exportc,dynlib.} =
    let a = checkinteger(L , 1 )
    let b = checkinteger(L, 2)
    var y = add(a,b) 
    pushinteger(L,y)
    return 1 


proc LuaInit*(L : PState) {.cdecl,exportc,dynlib.} = 
    echo "ok..."
    var regs = [
        luaL_Reg(name: "add", `func`: bind_add),
        luaL_Reg(name: nil, `func`: nil)
    ]
    L.register("nim",regs)
    L.pop(1)
