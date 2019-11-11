var hippo = {
    name : "Micheal",
    _age : 20,
    get age(){
        return this._age;
    } ,
    set age(i){
        _age = i;
    },
    speak: function(){
        return `${this.name} is hungry`;
    }
};

Object.defineProperty(hippo, '_surname', {
    value: 80,
    configurable: true,
    writable: true
});

Object.defineProperty(hippo, 'surname', {
    get: function() {return this._surname; },
    set: function(i) { this._surname = i;}
});

Object.defineProperty(hippo, 'say', {
    value: function(){
        return "I'm hippo";
    }
});

hippo._surname = 20;
console.log(hippo._surname);
hippo.surname = "Janus"
console.log(hippo.surname)
console.log(hippo._surname)