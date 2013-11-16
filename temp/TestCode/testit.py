try{
    var x = badVarName;
} catch (err){
    console.log(err.name + ': "' + err.message +  '" occurred when assigning x.');
}

{
    "name": "my_module",
    "version": "0.1.0",
    "description": "a simple zero-configuration command-line http server",
    "dependencies" : {
        "express"   :  "latest"
    }
}
{