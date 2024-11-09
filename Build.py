import os , sys , shutil , json 

here = os.path.dirname(__file__)
Nimdev = os.path.join(here,"Nim-Dev")

Luacode = open(os.path.join(Nimdev,"Lua.nim")).read()
MyExtension = open(os.path.join(Nimdev,"MyExtension.nim")).read()
Manifest = open(os.path.join(Nimdev,"ext.manifest")).read()
BuildExt = open(os.path.join(Nimdev,"BuildExt.py")).read()
NimExtension = os.path.join(here,"NimExtension")
Template_Editor_script = open(os.path.join(Nimdev,"Template.lua")).read()
if os.path.exists(NimExtension) : shutil.rmtree(NimExtension)
os.makedirs(NimExtension)


generated_code = Template_Editor_script.replace('BUILD_EXTENSION_CODE_BUILD_EXTENSION_CODE_BUILD_EXTENSION_CODE_BUILD_EXTENSION_CODE' , BuildExt)
generated_code = generated_code.replace('MyExtensionMyExtensionMyExtensionMyExtensionMyExtensionMyExtensionMyExtensionMyExtension' , MyExtension)
generated_code = generated_code.replace('Lua_binding_codeLua_binding_codeLua_binding_codeLua_binding_codeLua_binding_codeLua_binding_code' , Luacode)
print(generated_code,file = open(os.path.join(NimExtension ,"Nim.editor_script"),"w"))