library(ggplot2)

ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE)
  
# 這可以讓分組資料的 cor 都成現在圖上
# factor(), 沒有使用，會變成一條線，變成深淺

# ------------------------------------------------------------------
ggplot(mtcars, aes(x = mpg, fill = factor(cyl))) +
  geom_density(alpha = 0.5)

ggplot(iris, aes(x = Petal.Length, fill = Species)) +
  geom_density(alpha = 0.5)

# ! Species 是 factor（分類變數），ggplot2 能自動辨識為分類。
# 所以你在 aes(fill = Species) 中不需額外處理，它就會用離散色彩分組。
# ------------------------------------------------------------------
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  facet_wrap(~cyl)

# ------------------------------------------------------------------
ggplot(mtcars, aes(x = hp, y = mpg)) +
  geom_point() +
  facet_grid(gear ~ cyl)

# ------------------------------------------------------------------
# 使用 color = factor(cyl) 畫出 wt ~ mpg 的散佈圖與回歸線。
ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) + 
    geom_point() + 
    geom_smooth(method = 'lm', se = FALSE)

# 改成使用 facet_wrap(~cyl)，畫出每組汽缸一張圖。
ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) + 
    geom_point() + 
    geom_smooth(method = 'lm', se=FALSE) + 
    facet_wrap(~cyl)

# 對 mtcars$mpg 畫出密度圖，並使用 fill = factor(cyl)。
ggplot(mtcars, aes(x = mpg, fill = factor(cyl))) + 
    geom_density(alpha = 0.35)
# color, 會變成只有線條

# 使用 facet_grid(gear ~ cyl)，畫出 hp ~ mpg 的散佈圖與回歸線。
ggplot(mtcars, aes(x=hp, y = mpg)) + 
    geom_point() + 
    geom_smooth(method = 'lm', se = FALSE) + 
    facet_grid(gear ~ cyl)

head(mtcars, 20)

# 請觀察第 1 題與第 2 題的圖形差異：你覺得哪一種在分析時比較直觀？為什麼？
# 我自己覺得第一種不分圖比較好，能比較清楚一次看到全部資料，如果有區別顏色的話
