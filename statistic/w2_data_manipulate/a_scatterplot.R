library(ggplot2)

# ------------------------------------------------------------------
# Scatterplot
ggplot(mtcars, aes(x = hp, y = mpg)) +
    geom_point() + 
    geom_smooth(method = "lm", se = TRUE, color = "red") +
    # lm 信賴區間， se 灰色
    labs(title = "MPG vs Horsepower", x = "馬力", y = "每加侖哩程") +
    theme_minimal() # 這會把背後的格現灰色變淡

# ------------------------------------------------------------------
# 用 ggplot() 畫出 mtcars 中 wt（車重）與 mpg 的散佈圖。
# 為上面圖加上線性趨勢線（紅色），並移除信賴區間。
# 觀察圖形後：你覺得車重與油耗有關聯嗎？關聯方向是正還是負？

ggplot(mtcars, aes(x = wt, y = mpg)) + 
    geom_point() + 
    geom_smooth(method = 'lm',se = FALSE, color = 'red') + 
    labs(title = 'MPG vs wt', x = 'wt', y = 'MPG') + 
    theme_minimal() 