x <- c(72,75,79,83,91)

# ----------------------------------------------------------------
mean_x <- mean(x) # 會得到平均數，80
print(mean_x) 

# ----------------------------------------------------------------
sd_score <- sd(x) # sample standard deviation
print(sd_score)
# 7.416198

# ----------------------------------------------------------------
# 手算 standard deviation
z_scores <- (x - mean(x)) / sd(x)
print(z_scores)
# -1.0787198 -0.6741999 -0.1348400  0.4045199  1.4832397

# ----------------------------------------------------------------
# sacle 就可以直接算standard deviation
z_scores <- scale(x)
print(z_scores)
#            [,1]
# [1,] -1.0787198
# [2,] -0.6741999
# [3,] -0.1348400
# [4,]  0.4045199
# [5,]  1.4832397
# attr(,"scaled:center")
# [1] 80
# attr(,"scaled:scale")
# [1] 7.416198

z_scores <- as.vector(scale(x))
print(z_scores)
# [1] -1.0787198 -0.6741999 -0.1348400  0.4045199  1.4832397

# ----------------------------------------------------------------
t_score <- 50 + 10 * z_scores
print(t_score)
# 39.2128 43.2580 48.6516 54.0452 64.8324


install.packages("ggplot2")  # 第一次執行才需要
library(ggplot2)
df <- data.frame(
  original = x,
  z = z_scores,
  t = t_scores
)

