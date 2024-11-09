local _M = {}

local function ends_with(str, ending)
    return ending == '' or str:sub(-#ending) == ending
end

local python_build_script = [[
BUILD_EXTENSION_CODE_BUILD_EXTENSION_CODE_BUILD_EXTENSION_CODE_BUILD_EXTENSION_CODE
]]

local MyExtension_lua_script = [[
MyExtensionMyExtensionMyExtensionMyExtensionMyExtensionMyExtensionMyExtensionMyExtension
]]

local Lua_binding_code = [[
Lua_binding_codeLua_binding_codeLua_binding_codeLua_binding_codeLua_binding_codeLua_binding_code
]]
function _M.get_commands()
    local commands = {}
    local Create_Nim_Ext = {
        label = 'Create Nim Extension',
        locations = {'Assets'},
        query = {
            selection = {type = 'resource', cardinality = 'one'}
        },
        run = function(opts)
            editor.execute("mkdir" ,  "Nim")
            local file = io.open("Nim/BuildExt.py", "w")
            file:write(python_build_script)
            file:close()
            local file = io.open("Nim/MyExtension.nim", "w")
            file:write(MyExtension_lua_script)
            file:close()
            local file = io.open("Nim/Lua.nim", "w")
            file:write(Lua_binding_code)
            file:close()
            local file = io.open("Nim/ext.manifest", "w")
            file:write('name : "nim"')
            file:close()
        end

    }
    local build_nim_extension = {
        label = 'Build Nim Extension',
        locations = {'Assets'},
        query = {
            selection = {type = 'resource', cardinality = 'one'}
        },
        active = function(opts)
            local path = editor.get(opts.selection, 'path')
            return ends_with(path, '.nim')
        end,
        run = function(opts)
            local path = editor.get(opts.selection, "path")
            editor.execute("python" ,  "Nim/BuildExt.py")
        end

    }
    local open_vscode = {
        label = 'Open vs-code',
        locations = {'Assets'},
        query = {
            selection = {type = 'resource', cardinality = 'one'}
        },
        active = function(opts)
            local path = editor.get(opts.selection, 'path')
            return true
        end,
        run = function(opts)
            local path = editor.get(opts.selection, "path")
            editor.execute("code" ,  ".")
        end

    }
    table.insert(commands, Create_Nim_Ext)
    table.insert(commands, build_nim_extension)

    return commands
end

return _M