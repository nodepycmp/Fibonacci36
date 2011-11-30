function fib(n,cur,next){
    if(n==0){
        return cur;
    } else
        return fib(n-1,next,cur+next);
}
console.log(fib(process.argv[2],0,1));
