library(ggplot2)
library(tibble)

p <- ggplot(iris, aes(x = Species, y = Petal.Length)) +
  geom_boxplot() + 
  geom_jitter(width = 0.02, alpha = 0.5, color = "blue")
ggsave('statistic/w1_intro_to_R/boxplot.png',plot = p, width = 6, height = 4)

# 沒有geom_jitter() 之前，(因為會把原先黑點擋住)
# ! 黑色點，會是離群數值

# width 是調整點的晃動，也可以設定為0，就會是一條線

# -------------------------------------------------------
summary(iris$Petal.Length)
#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#   1.000   1.600   4.350   3.758   5.100   6.900 

# -------------------------------------------------------
# 這是 base R的寫法
# 也可以轉換成tidyverse ，但很麻煩
# Tidy + Table, tibble()
# ! 建立函數都用 tibble() 作
# 因為可以讓出來的資料符合繼續在管道流動的格式
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
iris %>% group_by(Species) %>%
    summarise(
        summary_stats(Petal.Length)
        )

#   Species      min    q1 median  mean    q3   max
#   <fct>      <dbl> <dbl>  <dbl> <dbl> <dbl> <dbl>
# 1 setosa       1     1.4   1.5   1.46  1.58   1.9
# 2 versicolor   3     4     4.35  4.26  4.6    5.1
# 3 virginica    4.5   5.1   5.55  5.55  5.88   6.9


# -------------------------------------------------------
# 5.1
ggplot(iris, aes(y = Petal.Length)) +
  geom_boxplot()
#   geom_jitter(width = 0.02, alpha = 0.5, color = "blue")
# 5.2
ggplot(iris, aes(x = Species, y = Petal.Length)) + 
    geom_boxplot()

# 5.3
ggplot(iris, aes(x = Species, y = Petal.Length)) + 
    geom_boxplot() + 
    geom_jitter(width = 0.025, color = '#1d9cc6')
# 5.4
# base R (他沒辦法分組)
summary(iris$Petal.Length)
# tidyverse
iris %>% group_by(Species) %>%
    summarise(
        summary_stats(Petal.Length)
        )

# 5.5
ggplot(iris, aes(x = Species, y = Petal.Length)) + 
    geom_boxplot() + 
    geom_jitter(width = 0.025, color = '#1d9cc6') + 
    coord_flip() + 
    theme(aspect.ratio = 0.5)

# 5.6 可以看到離群值
ggplot(iris, aes(x=Species, y=Sepal.Width)) + 
    geom_boxplot()


# -------------------------------------------------------
# 這是可以作 summary_stats 的函數
install.packages("skimr")
library(skimr)
