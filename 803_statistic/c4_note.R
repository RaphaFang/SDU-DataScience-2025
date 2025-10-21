# Pass QC (between 35.8 and 36.2 oz)
pnorm(36.2 ,36, 0.11) - pnorm(35.8 ,36, 0.11)
# 0.9309637

# What percent of bottles have less than 35.8 ounces of ketchup?
pnorm(35.8 ,36, 0.11)
# 0.03451817

# ------------------------------------------
qnorm(0.03, 98.2, 0.73)
# 96.82702

# if you like to get the 10% on the "right", you have to put 0.9 in the qnorm()
qnorm(0.9, 98.2, 0.73)

# this will tell you the z score, base on mean = 0, sd = 1
qnorm(0.5)

# ------------------------------------------
pnorm(1) - pnorm(-1)
# 0.6826895
pnorm(2) - pnorm(-2)
# 0.9544997
pnorm(3) - pnorm(-3)
# 0.9973002

# ------------------------------------------
