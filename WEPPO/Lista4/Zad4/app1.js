
module.exports = {power};
let app2 = require('./app2.js');
function power(a, b){
     l = 1;
     if(b==2)
     return a * a;
    for ( i = 1; i <= b; i++){
        l = app2.mult(a, l);
    }
    return l;
}