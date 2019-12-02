
var Tree = function(left, right, value) {
    this.left = left;
    this.right = right;
    this.value = value;
};


Tree.prototype[Symbol.iterator] = function*(){
    if(this === null) return;
    if(this.left)
        yield *this.left;
    yield this.value;
    if(this.right)
        yield *this.right;
}


/*
              7
         5        6
      3     4
    2    

*/
var tr = new Tree(
    new Tree(
        new Tree(
            new Tree(null, null, 2), 
            null, 
            3),
        new Tree(null, null, 4),
        5),
     new Tree(null, null, 6),
    7);




for(var e of tr){
    console.log(e);
}