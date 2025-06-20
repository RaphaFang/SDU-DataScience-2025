library(ggplot2)
library(tibble)

ggplot(iris, aes(x = Species, y = Petal.Length)) +
  geom_boxplot() + 
  geom_jitter(width = 0.02, alpha = 0.5, color = "blue")
ggsave('statistic/w1_intro_to_R/boxplot.png', width = 6, height = 4)

# width 是調整點的晃動，也可以設定為0，就會是一條線

# -------------------------------------------------------
summary(iris$Petal.Length)
#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#   1.000   1.600   4.350   3.758   5.100   6.900 

# -------------------------------------------------------
# 這是 base R的寫法
# 也可以轉換成tidyverse ，但很麻煩
# Tidy + Table, tibble()
summary_stats <- function(x) {
  tibble(
    min = min(x),
    q1 = quantile(x, 0.25),
    median = median(x),
    mean = mean(x),
    q3 = quantile(x, 0.75),
    max = max(x)
  )
}
iris %>% summarise(summary_stats(Petal.Length))

# tibble(
#   name = c("Rafaela", "Alex"),
#   score = c(95, 88)
# )

# -------------------------------------------------------
# 5.1

# 5.2

# 5.3

# 5.4

# 5.5