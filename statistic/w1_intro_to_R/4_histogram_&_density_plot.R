library(ggplot2)

# -------------------------------------------------------
# geom_histogram()
# 這是控制住狀圖

# geom_density()
# 這是控制線條圖

# -------------------------------------------------------
ggplot(iris, aes(x = Petal.Length)) +
  geom_histogram(aes(y = after_stat(density)), fill = "lightblue", bins = 30, color = "black") +
  geom_density(color = "red", linewidth = 1.2) +
  labs(title = "Petal Length Distribution", x = "Petal Length", y = "Density")

# 使用 binwidth 指定每箱寬度（建議與實際單位有意義的資料使用）
ggplot(iris, aes(x = Sepal.Width, fill = Species)) +
  geom_histogram(binwidth = 0.025, fill = "lightblue", color = "black") +
  labs(title = "Histogram of Sepal Width", x = "Sepal Width", y = "Count")


# -------------------------------------------------------
# 這是同一張圖片，曲線圖疊圖
# ! 注意。fill 要在aes() 的誇號裡面  fill = Species
# facet_wrap 也是操作在特定的欄位資訊 facet_wrap(~Species)

ggplot(iris, aes(x = Petal.Length, fill = Species)) + 
  geom_density(alpha = 0.5, linewidth = 0.5) +
  labs(
    title = "Density Plot of Petal Length by Species",
    x = "Petal Length",
    y = "Density"
  )
# 這可以做出柱狀圖的版本
ggplot(iris, aes(x = Petal.Length, fill = Species)) +
  geom_histogram(binwidth = 0.2, color = "white") +
#   facet_wrap(~Species) +
  labs(title = "Sepal Width by Species")


# -------------------------------------------------------
# 每種花一張圖
ggplot(iris, aes(x = Petal.Length)) +
  geom_histogram(binwidth = 0.2, fill = "steelblue", color = "white") +
  facet_wrap(~Species) +
  labs(title = "Sepal Width by Species")


# -------------------------------------------------------
# binwidth 是你想得到的箱子「寬度」
# bin 是你想要切出「幾個」箱子
# ! 注意 binwidth / bin 只能一次寫一個

# 4.1
ggplot(iris, aes(x = Sepal.Width)) +
    geom_histogram(bins = 20, color = "white")

# 4.2
# 使用 binwidth = 0.3 畫出 Petal.Length 的直方圖，觀察是否能更清楚看出集中區域。
ggplot(iris, aes(x = Petal.Length)) + 
    geom_histogram(binwidth = 0.3, color = "white", fill = "lightblue")

# 4.3
ggplot(iris, aes(x = Sepal.Width)) + 
    geom_histogram(aes(y = after_stat(density)),binwidth = 0.3,bins = 2, color = "white") + 
    geom_density(color = 'red', linewidth = 1.2)

# 4.4
ggplot(iris, aes(x = Sepal.Length)) + 
    geom_histogram(aes(y = after_stat(density)),binwidth = 0.3,bins = 2, color = "white") + 
    geom_density(color = 'red', linewidth = 1.2) 
    facet_wrap(~Species) 

ggplot(iris, aes(x = Sepal.Length, fill = Species)) + 
  geom_density(alpha = 0.4) +
  facet_wrap(~Species)

# 4.5 geom_density() 是預設 position = "identity"
ggplot(iris, aes(x = Sepal.Length, fill = Species)) + 
    geom_density(position = "identity",alpha = 0.5, linewidth = 0.5, color = 'white')

# 4.6 geom_histogram() 是預設 position = "stack"
ggplot(iris, aes(x = Sepal.Length, fill = Species)) + 
  geom_histogram(position = "identity", alpha = 0.5, bins = 20, color = "white")
