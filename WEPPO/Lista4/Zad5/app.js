
console.log("Podaj nazwe użytkownika");
process.stdin.setEncoding('utf8');
process.stdin.on('readable', function(){
    var chunk = process.stdin.read();
    if(chunk !== null){
        process.stdout.write("Witaj "+ chunk);
    }
});

process.stdin.on('end', () => {
    process.stdout.write('end');
});