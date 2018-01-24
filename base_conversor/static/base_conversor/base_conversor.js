const error = $('#error');

$('input').keyup(function(){
    const actualBase = Number(this.id.split("base").pop()); 
    const regex = new RegExp("^"+this.pattern+"$");
    if(!regex.test(this.value)){
        error.html("The number base " + actualBase + " is not formatted correctly");
        error.show();
        return -1;
    }
    else{
        $('#error').hide();
    }
    const inputs = $(":input");
    const base10Value = actualBase!==10?baseOtherTo10(actualBase, this.value):Number(this.value);
    for(var i = 0; i < inputs.length; i++)
    {
        const base = Number(inputs[i].id.split("base").pop()); 
        if(base !== actualBase){
            switch(actualBase){
                case 10:
                    inputs[i].value=base10ToOther(base, this.value);
                default:
                    if(base==10){
                        inputs[i].value=base10Value;
                    }
                    else{
                        inputs[i].value=base10ToOther(base,base10Value);
                    }
            }

        }
    }
})


function base10ToOther(base, value){
    if(value===0)
        return "0";
    else
    {   
        return base10ToOther(base, Math.floor(value/base)) + String(numberToLetter(value%base));
    }
}

function baseOtherTo10(base, value){
    valueArray = String(value).split("").reverse();
    base10 = 0;
    for(var i = 0; i < valueArray.length; i++)
    {
        base10 += Math.pow(base,i)*Number(letterTonumber(valueArray[i]));
    }
    return base10;
}

function numberToLetter(val){
    if(val>9)
        return String.fromCharCode(val+55)
    else
        return val;
}

function letterTonumber(val){
    const ascii = val.toUpperCase().charCodeAt(0);
    return ascii>64?ascii-55:val;
}