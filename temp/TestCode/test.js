try{
    var x = badVarName;
} catch (err){
    console.log(err.name + ': "' + err.message +  '" occurred when assigning x.');
}


