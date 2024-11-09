import os , shutil , subprocess , urllib.request , glob
joinpath = os.path.join 

def BuildExt(cpp_code) : 
    ExtensionPath = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))
    here = os.path.abspath(os.path.dirname(__file__))
    nimfile = joinpath(here,'MyExtension.nim')
    nimcache = joinpath(here,'nimcache')
    cheader = "nim.h"
    # get currnet nim installation : 
    nimpath = shutil.which('nim')
    if nimpath is None : 
        exit("[Exit Error] nim is not installed or can not be found ")
    nim_version = subprocess.run([
        nimpath , "-v"
    ] , capture_output=True, text=True)
    if nim_version.returncode != 0 : 
        exit(f'[Exit Error] can not excute command : {nimpath} -v , due to {nim_version.stderr}' )
    # get nimbase.h content  
    nimversion = nim_version.stdout.split()[nim_version.stdout.split().index('Version') + 1 ]
    rtawgithub_nimbase_h = f'https://raw.githubusercontent.com/nim-lang/Nim/refs/tags/v{nimversion}/lib/nimbase.h'
    nimbase_h_content = None 
    try:
        with urllib.request.urlopen(rtawgithub_nimbase_h) as response:
            content = response.read().decode('utf-8')  # Decode if it's text content
            nimbase_h_content = content
    except urllib.error.URLError as e:
        exit(f"Failed to retrieve content: {e.reason}")
    ## clean old build 
    if os.path.exists(nimcache) : 
        shutil.rmtree(nimcache)
    # build nim file
    nim_compîle_command = [
        nimpath , "c" , "--exceptions:quirky" , "-d:release"  , "--genScript " , "--gc:refc" ,"-d:useMalloc" , "--noMain" , "--app:lib",
        f"--nimcache:{nimcache}"  , f"--header:{cheader}" , nimfile
    ]
    print(f" Build :\n\t {' '.join(nim_compîle_command)}")
    nim_compile = subprocess.run(
            nim_compîle_command  , capture_output=True, text=True
    )
    if nim_compile.returncode != 0 : 
        exit(f'[Error] compiling {nimfile} \n' + nim_compile.stderr)
    if not os.path.exists(os.path.join(nimcache,"nimbase.h")) : 
        print(nimbase_h_content , file = open(os.path.join(nimcache,"nimbase.h"),"w"))
    os.makedirs(ExtensionPath , exist_ok = True ) 
    # copy src files
    ExtensionPath_src = os.path.join(ExtensionPath,'src')
    os.makedirs(ExtensionPath_src , exist_ok = True )
    for file in glob.glob(os.path.join(nimcache , "*.c")) : 
        shutil.copy(file , os.path.join(ExtensionPath_src,os.path.basename(file)))
    # copy header files
    ExtensionPath_include = os.path.join(ExtensionPath,'include')
    os.makedirs(ExtensionPath_include , exist_ok = True )  
    for file in glob.glob(os.path.join(nimcache , "*.h")) : 
        shutil.copy(file , os.path.join(ExtensionPath_include,os.path.basename(file)))
    if not os.path.exists(os.path.join(ExtensionPath_src,"nim.cpp")) : 
        print(cpp_code , file = open(os.path.join(ExtensionPath_src,"nim.cpp"),"w"))
    # create manifest file
    if not os.path.exists(os.path.join(ExtensionPath,"ext.manifest")) : 
        print('name: "nim"\n' , file = open(os.path.join(ExtensionPath,"ext.manifest"),"w"))
    if os.path.exists(nimcache) : 
        shutil.rmtree(nimcache)


cpp_code  = '''
#define LIB_NAME "nim"
#define MODULE_NAME "nim"

// include the Defold SDK
#include <dmsdk/sdk.h>
extern "C" {
    #include "nim.h"
}


static dmExtension::Result AppInitializeMyExtension(dmExtension::AppParams* params)
{
    dmLogInfo("AppInitializeMyExtension");
    NimMain() ; 
    return dmExtension::RESULT_OK;
}

static dmExtension::Result InitializeMyExtension(dmExtension::Params* params)
{
    // Init Lua
    LuaInit(params->m_L);
    dmLogInfo("Registered %s Extension", MODULE_NAME);
    return dmExtension::RESULT_OK;
}

static dmExtension::Result AppFinalizeMyExtension(dmExtension::AppParams* params)
{
    dmLogInfo("AppFinalizeMyExtension");
    return dmExtension::RESULT_OK;
}

static dmExtension::Result FinalizeMyExtension(dmExtension::Params* params)
{
    dmLogInfo("FinalizeMyExtension");
    return dmExtension::RESULT_OK;
}

static dmExtension::Result OnUpdateMyExtension(dmExtension::Params* params)
{
    dmLogInfo("OnUpdateMyExtension");
    return dmExtension::RESULT_OK;
}

static void OnEventMyExtension(dmExtension::Params* params, const dmExtension::Event* event)
{
    switch(event->m_Event)
    {
        case dmExtension::EVENT_ID_ACTIVATEAPP:
            dmLogInfo("OnEventMyExtension - EVENT_ID_ACTIVATEAPP");
            break;
        case dmExtension::EVENT_ID_DEACTIVATEAPP:
            dmLogInfo("OnEventMyExtension - EVENT_ID_DEACTIVATEAPP");
            break;
        case dmExtension::EVENT_ID_ICONIFYAPP:
            dmLogInfo("OnEventMyExtension - EVENT_ID_ICONIFYAPP");
            break;
        case dmExtension::EVENT_ID_DEICONIFYAPP:
            dmLogInfo("OnEventMyExtension - EVENT_ID_DEICONIFYAPP");
            break;
        default:
            dmLogWarning("OnEventMyExtension - Unknown event id");
            break;
    }
}

// Defold SDK uses a macro for setting up extension entry points:
//
// DM_DECLARE_EXTENSION(symbol, name, app_init, app_final, init, update, on_event, final)

// MyExtension is the C++ symbol that holds all relevant extension data.
// It must match the name field in the `ext.manifest`
DM_DECLARE_EXTENSION(nim, LIB_NAME, AppInitializeMyExtension, AppFinalizeMyExtension, InitializeMyExtension, OnUpdateMyExtension, OnEventMyExtension, FinalizeMyExtension)
'''
BuildExt(cpp_code=cpp_code)