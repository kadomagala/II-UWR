var Tree = function(left, right, value) {
    this.left = left;
    this.right = right;
    this.value = value;
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



function traverse(tree){ //inorder
    if(tree === null){
        return "";
    }else{
        return traverse(tree.left) + " " + tree.value + " " + traverse(tree.right);
    }
}

console.log(traverse(tr))