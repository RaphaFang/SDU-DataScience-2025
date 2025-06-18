# normal distribution, 鐘形對稱：平均值、中位數、眾數全部相同
# 約68% 落在 𝜇 ± 1 𝜎 ，95% 落在 𝜇 ± 2 𝜎 

# | 功能          | 說明            | R 寫法                                |
# | ------------ | --------------- | ------------------------------------ |
# | 計算 Z-score  | 對變數標準化      | `scale(x)`                           |
# | 理論常態密度   | 計算機率密度      | `dnorm(x, mean, sd)`                 |
# | 累積分布函數   | $P(X \leq x)$   | `pnorm(x, mean, sd)`                 |
# | 繪圖密度曲線   | 觀察分布狀況      | `geom_density()`, `geom_histogram()` |

library(ggplot2)
# ! aes() 代表「美學映射 (aesthetics)」：把資料欄位映射到圖形屬性（x、y、color、fill、size...）

ggplot(iris, aes(x = Petal.Length)) +
  geom_histogram(aes(y = after_stat(density)), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red", linewidth = 1.2) +
  labs(title = "Distribution of Petal Length", x = "Petal Length", y = "Density")


# 可以只輸出特定己行 c[]
iris$Petal.Length.z <- scale(iris$Petal.Length)
head(iris[c("Petal.Length", "Petal.Length.z")])
head(iris)

# -------------------------------------------------------
# dnorm vs pnorm
# dnorm, density of the normal distribution	
# 理論上的分布，圖會是鐘型
# pnorm, probability of the normal distribution
# 累積的分布，圖最後會到1(100%)

# -------------------------------------------------------
mu <- iris %>% summarise(m = mean(Sepal.Length)) %>% pull(m)
s  <- iris %>% summarise(s = sd(Sepal.Length))   %>% pull(s)

df <- tibble(x = seq(min(iris$Sepal.Length) - 0.5,
                     max(iris$Sepal.Length) + 0.5, by = 0.01)) %>%
  mutate(
    density = dnorm(x, mean = mu, sd = s),
    cdf     = pnorm(x, mean = mu, sd = s)
  )
# head(df)
ggplot(df, aes(x = x)) +
  geom_line(aes(y = density), color = "steelblue", size = 1.2) +
  geom_line(aes(y = cdf), color = "darkorange", size = 1.2) +
  labs(
    title = "dnorm() vs pnorm() for iris$Sepal.Length",
    subtitle = paste0("mean = ", round(mu, 2), ", sd = ", round(s, 2)),
    caption = "blue line's dnorm(), orange line's pnorm()"
  )

# -------------------------------------------------------
# 3.1
iris$Sepal.Length.z <- scale(iris$Sepal.Length)
head(iris)

# 3.2
ggplot(iris, aes(x = Sepal.Length)) +
    geom_histogram(aes(y = after_stat(density)),bins=100, fill = "skyblue", color = "black") +
    geom_density(color = "red", linewidth = 1.2) + 
    labs(title = "Distribution of Sepal Length", x = "Sepal Length", y = "Density")

# 3.3
ggplot(iris, aes(x = Sepal.Length.z)) + 
    geom_histogram(aes(y = after_stat(density)),bins=100, fill = "skyblue", color = "black") +
    geom_density(color = "red", linewidth = 1.2) + 
    geom_vline(xintercept = 0, linetype = "dashed", color = "darkred") + 
    labs(title = "Distribution of Sepal.Length.z", x = "Sepal Length", y = "Density")

# 3.4 小於的機率
# pnorm() 是回傳小於 x 數值的比例
pnorm(iris$Petal.Length, mean(iris$Petal.Length), sd(iris$Petal.Length))
# 這是傳回所有的數值，可以設定要傳回的
pnorm(4, mean = mean(iris$Petal.Length), sd = sd(iris$Petal.Length))
# 0.33382 是33.3%


# 3.5
dnorm(mean(iris$Petal.Length), mean(iris$Petal.Length), sd(iris$Petal.Length))
# 0.2259914
# 這是得出，在全部數據中，x 等同於中位數的機率

# 3.6
p <- ggplot(iris, aes(x = Petal.Length, fill = Species)) + 
  geom_density(alpha = 0.5, size = 0.5) +
  labs(
    title = "Density Plot of Petal Length by Species",
    x = "Petal Length",
    y = "Density"
  )
ggsave("statistic/w1_intro_to_R/line_plot.png", plot = p, width = 6, height = 4)

# alpha = 0.5 這是控直圖案的顏色深淺
