quadrant <- function(x,y){
    if(!is.numeric(x) | !is.numeric(y)){
        return(cat("Either x or y is not numeric."))
    }
    if(x==0 | y==0){
        return(cat("dude, one of the input is on the axis"))
    }
    if(x>=0){
        if(y>=0){
            return("I")
        }else{
            return("IV")
        }
    }else{
        if(y>=0){
            return("II")
        }else{
            return("III")
        }
    }
}
quadrant(-1,0)

# ------------------------------------
BMI <- function(weight, height){
    bmi <- weight / (height/100)^2
    # cat(bmi)
    if(bmi>=40){
        cat('MO')
    }else if (bmi>=35) {
       cat('SO')
    }else if (bmi>=30) {
       cat('O')
    }else if (bmi>=25) {
       cat('overWeight')
    }else if (bmi>=18.5) {
       cat('HW')
    }else{
        cat('underWeight')
    }
}
BMI(120, 180)

# ------------------------------------
facto <- function(x){
    holder <- 1
    while(x>0) {
        holder <- holder*x
        x <- x-1
    }
    return(holder)
}
facto(5)

# ------------------------------------
add_up <- function(x){
    holder <- 0
    while(x>0){
        holder <- holder + x
        x <- x-1
    }
    return(holder)
}
add_up(4)
