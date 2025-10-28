euler <- function(deriv, x0, y0, h, n) {

  x <- numeric(n + 1) # 這邊是建立為 0 的 vector
  y <- numeric(n + 1)

  x[1] <- x0
  y[1] <- y0

  for (i in 1:n) {
    y[i + 1] <- y[i] + h * deriv(x[i], y[i])
    x[i + 1] <- x[i] + h
    if(i==n){
      print(y[n])
    }
  }
  plot(x, y, type = "p", col = "black", lwd = 1,
       main = "Solution curve",
       xlab = "x", ylab = "f(x)")
}
euler(function(x,y) {y}, x0 = 0, y0 = 1, h = 0.00001, n = 100000)


# n_r<-function(f,f1,x0){
#   x<-x0
#   k_max<-100
#   tolerance<-1e-8
#   k<-0
#   fx<-f(x)

#   if(abs(fx)<=tolerance){
#     return("Your start guess was on the money")
#   }

#   while(k<=k_max){
#     fpx<-f1(x)
#     if(fpx==0){
#       return("Derivative is zero-can't continue")
#     }
#     x<-x-fx/fpx
#     fx<-f(x)
#     k<-k+1
#     if(abs(fx)<=tolerance){
#       return(list(solution=x,nr_steps=k))
#     }
#     if(k==k_max){
#       print("Max nr of steps has been reached without finding a solution.")
#     }
#   }
# }

# n_r(function(x) x^2-2,function(x) 2*x,1)