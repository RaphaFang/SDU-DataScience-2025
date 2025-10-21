collatz <- function(x){
    counter = 0
    while (x > 1) {
        if (x%%2 == 0){
            x = x/2
        }else{
            x = x*3 + 1
        }
        counter = counter + 1
        cat(x)}
    cat("steps we take:", counter, "\n")
}
collatz(1)

# ------------------------------------------
# have to keep the number of gap in even, means the "n" in func must be even
simpson <- function(f, a, b, n){
    stopifnot(n %% 2 == 0)
    d_x <- (b-a)/n
    holder <- f(a) + f(b)
    for (i in 1:n-1){
        input <- a + i*d_x
        if (i%%2 == 0){
            holder <- holder + 2*f(input)
        }else{
            holder = holder + 4*f(input)
        }
    }
    return(holder * (d_x/3))
}

simpson(sin, 0, 10, 1000)
# [1] 1.839072
integrate(sin, 0, pi)
# 2 with absolute error < 2.2e-14

# ------------------------------------------
# sum of the squares of the first one hundred natural numbers
holder <- 0
for (i in 1:100){
    holder = holder + i**2
}
cat(holder)
# 338350

# the square of the sum
(101*50)**2
# 25502500

holder_2 <- 0
for (i in 1:1000){
    if(i%%3==0 | i%%5==0){
        holder_2 = holder_2 + i
    }
}
cat(holder_2)
# 234168