module.exports = {mult};

let app1 = require('./app1.js');

function mult(a ,b){
    if(a === b){
        return app1.power(a,2);
    }
    else{
        return a * b;
   }
}