var Foo = function(name){
    this.name = name;

}

Foo.prototype = (function(){
    var Qux = function(){
        console.log("Private method call");
    };

    return {
        Bar:function(){
            Qux();
        }
    };
})();

/*
Foo.prototype.Asd = function (){
    Qux();
};
*/


var x = new Foo("test");

x.Bar();
//x.Asd(); //error