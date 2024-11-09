python -c "import os , shutil , subprocess , urllib.request , glob , sys \njoinpath = os.path.join \n\ndef BuildExt(cpp_code) : \nExtensionPath = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))\nhere = os.path.abspath(os.path.dirname(__file__))\nnimfile = joinpath(here,'MyExtension.nim')\nnimcache = joinpath(here,'nimcache')\ncheader = \"nim.h\"\n# get currnet nim installation : \nnimpath = shutil.which('nim')\nif nimpath is None : \nmay_exisits = os.path.join(os.environ['HOME'] , '.nimble/bin/nim')\nif os.path.exists(may_exisits) : \nnimpath = may_exisits\nelse : \nexit(\"[Defold Nim Naitive Extension] Erro: nim is not installed or can not be found \")\nnim_version = subprocess.run([\nnimpath , \"-v\"\n] , capture_output=True, text=True)\nif nim_version.returncode != 0 : \nexit(f'[Exit Error] can not excute command : {nimpath} -v , due to {nim_version.stderr}' )\n# get nimbase.h content  \nnimversion = nim_version.stdout.split()[nim_version.stdout.split().index('Version') + 1 ]\nprint(f\"[Defold Nim Naitive Extension]: Nim version: {nimversion}\")\nrtawgithub_nimbase_h = f'https://raw.githubusercontent.com/nim-lang/Nim/refs/tags/v{nimversion}/lib/nimbase.h'\nnimbase_h_content = None \ntry:\nwith urllib.request.urlopen(rtawgithub_nimbase_h) as response:\ncontent = response.read().decode('utf-8')  # Decode if it's text content\nnimbase_h_content = content\nexcept urllib.error.URLError as e:\nexit(f\"[Defold Nim Naitive Extension] Error: Failed to retrieve content: {e.reason}\")\n## clean old build \nif os.path.exists(nimcache) : \nshutil.rmtree(nimcache)\n# build nim file\nnim_comp\u00eele_command = [\nnimpath , \"c\" , \"--exceptions:quirky\" , \"-d:release\"  , \"--genScript \" , \"--gc:refc\" ,\"-d:useMalloc\" , \"--noMain\" , \"--app:lib\",\nf\"--nimcache:{nimcache}\"  , f\"--header:{cheader}\" , nimfile\n]\nprint(f\"[Defold Nim Naitive Extension] Executing :\\n{' '.join(nim_comp\u00eele_command)}\")\nnim_compile = subprocess.run(\nnim_comp\u00eele_command  , capture_output=True, text=True\n)\nif nim_compile.returncode != 0 : \nexit(f'[Defold Nim Naitive Extension] Error: compiling {nimfile} \\n' + nim_compile.stderr)\nif not os.path.exists(os.path.join(nimcache,\"nimbase.h\")) : \nprint(nimbase_h_content , file = open(os.path.join(nimcache,\"nimbase.h\"),\"w\"))\nos.makedirs(ExtensionPath , exist_ok = True ) \n# copy src files\nExtensionPath_src = os.path.join(ExtensionPath,'src')\nif os.path.exists(ExtensionPath_src) : shutil.rmtree(ExtensionPath_src)\nos.makedirs(ExtensionPath_src , exist_ok = True )\nfor file in glob.glob(os.path.join(nimcache , \"*.c\")) : \nshutil.copy(file , os.path.join(ExtensionPath_src,os.path.basename(file)))\n# copy header files\nExtensionPath_include = os.path.join(ExtensionPath,'include')\nif os.path.exists(ExtensionPath_include) : shutil.rmtree(ExtensionPath_include)\nos.makedirs(ExtensionPath_include , exist_ok = True )  \nfor file in glob.glob(os.path.join(nimcache , \"*.h\")) : \nshutil.copy(file , os.path.join(ExtensionPath_include,os.path.basename(file)))\nif not os.path.exists(os.path.join(ExtensionPath_src,\"nim.cpp\")) : \nprint(cpp_code , file = open(os.path.join(ExtensionPath_src,\"nim.cpp\"),\"w\"))\n# create manifest file\nif not os.path.exists(os.path.join(ExtensionPath,\"ext.manifest\")) : \nprint('name: \"nim\"\\n' , file = open(os.path.join(ExtensionPath,\"ext.manifest\"),\"w\"))\nif os.path.exists(nimcache) : \nshutil.rmtree(nimcache)\nprint(\"[Defold Nim Naitive Extension] Extension ready !!\")\n\n\ncpp_code  = '''\n#define LIB_NAME \"nim\"\n#define MODULE_NAME \"nim\"\n\n// include the Defold SDK\n#include <dmsdk/sdk.h>\nextern \"C\" {\n#include \"nim.h\"\n}\n\n\nstatic dmExtension::Result AppInitializeMyExtension(dmExtension::AppParams* params)\n{\ndmLogInfo(\"AppInitializeMyExtension\");\nNimMain() ; \nreturn dmExtension::RESULT_OK;\n}\n\nstatic dmExtension::Result InitializeMyExtension(dmExtension::Params* params)\n{\n// Init Lua\nLuaInit(params->m_L);\ndmLogInfo(\"Registered %s Extension\", MODULE_NAME);\nreturn dmExtension::RESULT_OK;\n}\n\nstatic dmExtension::Result AppFinalizeMyExtension(dmExtension::AppParams* params)\n{\ndmLogInfo(\"AppFinalizeMyExtension\");\nreturn dmExtension::RESULT_OK;\n}\n\nstatic dmExtension::Result FinalizeMyExtension(dmExtension::Params* params)\n{\ndmLogInfo(\"FinalizeMyExtension\");\nreturn dmExtension::RESULT_OK;\n}\n\nstatic dmExtension::Result OnUpdateMyExtension(dmExtension::Params* params)\n{\ndmLogInfo(\"OnUpdateMyExtension\");\nreturn dmExtension::RESULT_OK;\n}\n\nstatic void OnEventMyExtension(dmExtension::Params* params, const dmExtension::Event* event)\n{\nswitch(event->m_Event)\n{\n    case dmExtension::EVENT_ID_ACTIVATEAPP:\n    dmLogInfo(\"OnEventMyExtension - EVENT_ID_ACTIVATEAPP\");\n    break;\n    case dmExtension::EVENT_ID_DEACTIVATEAPP:\n    dmLogInfo(\"OnEventMyExtension - EVENT_ID_DEACTIVATEAPP\");\n    break;\n    case dmExtension::EVENT_ID_ICONIFYAPP:\n    dmLogInfo(\"OnEventMyExtension - EVENT_ID_ICONIFYAPP\");\n    break;\n    case dmExtension::EVENT_ID_DEICONIFYAPP:\n    dmLogInfo(\"OnEventMyExtension - EVENT_ID_DEICONIFYAPP\");\n    break;\n    default:\n    dmLogWarning(\"OnEventMyExtension - Unknown event id\");\n    break;\n}\n}\n\n// Defold SDK uses a macro for setting up extension entry points:\n//\n// DM_DECLARE_EXTENSION(symbol, name, app_init, app_final, init, update, on_event, final)\n\n// MyExtension is the C++ symbol that holds all relevant extension data.\n// It must match the name field in the `ext.manifest`\nDM_DECLARE_EXTENSION(nim, LIB_NAME, AppInitializeMyExtension, AppFinalizeMyExtension, InitializeMyExtension, OnUpdateMyExtension, OnEventMyExtension, FinalizeMyExtension)\n'''\n\n\n\nBuildExt(cpp_code=cpp_code)"