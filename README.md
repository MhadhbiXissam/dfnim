# dfnim
Nim Naitive Extension for defold

# Creedits : 
***this work is based on the nice project [nimLua](https://github.com/jangko/nimLUA)***
## Install 
### game.project -> project -> dependecies -> add this url 
```txt
https://github.com/MhadhbiXissam/dfnim/archive/refs/tags/v1.0.1.zip
```
# Get starts : 
1-  Edit file `MyExtension.nim`
```txt
Nim
├── BuildExt.py     <-- this to build the nim code 
├── LICENSE
├── Lua.nim         <-- this is Lua binding for nim 
├── MyExtension.nim <-- edit this file 
├── nim.manifest
└── README.md
```
>   Note : do not change the name of the file cause it is point in build python file by the name , if you want so , change it in python file also with same name .

```nim
include Lua


# write you nim function 
proc add*( a : int , b:int ): int  = 
    return a + b*100


# create binding 
proc Luabinding_add(L : PState) :  cint {.cdecl,exportc,dynlib.} =
    let a = checkinteger(L , 1 )
    let b = checkinteger(L, 2)
    var y = add(a,b) + 1  - 1000
    pushinteger(L,y)
    return 1 


# this function is exposed to defld game engine , to register the module 
proc LuaInit*(L : PState) {.cdecl,exportc,dynlib.} = 
    var regs = [
        # here add the function and its name 
        luaL_Reg(name: "add", `func`: Luabinding_add),
        luaL_Reg(name: nil, `func`: nil)
    ]
    L.register("ext",regs)
    L.pop(1)
```
2-  Build the nim code : 
to build the nim code to be used in defld run : 
```bash
python BuildExt.py 
```

3- Use you function from  any where in your lua defold scipts : 
```lua
    --- ....
	local result = nim.add(10,12)
	print(result) 
    --- ....
end
```