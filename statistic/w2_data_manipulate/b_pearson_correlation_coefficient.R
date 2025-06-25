# 範圍：−1≤r≤1
# r>0：正相關，變數一起上升
# r<0：負相關，一個上升、一個下降
# r=0：無線性關係（但可能有非線性）

cor(mtcars$wt, mtcars$mpg)
# -0.8676594

# ------------------------------------------------------------------
r <- cor(mtcars$wt, mtcars$mpg)

ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 5, y = 30, label = paste0("r = ", round(r, 2)), size = 15, color = "darkblue") +
  theme_minimal()

# annotate 可以提供註解

# ------------------------------------------------------------------
mtcars %>% group_by(cyl) %>%
  summarise(
    cor_wt_mpg = cor(wt, mpg)
    )

# ------------------------------------------------------------------
# 使用 cor() 計算 wt 與 mpg 的皮爾森相關係數。
# 加上 annotate() 把 r 值加在前一題散佈圖中（建議四捨五入到小數第 2 位）。
# 改畫 hp 與 mpg，同樣加上趨勢線與相關係數。
# 使用 group_by(cyl) 分別計算不同汽缸數下的 wt ~ mpg 的相關性。

p1 <- mtcars %>% summarise(p = cor(wt, mpg)) %>% pull(p)
# -0.8676594

ggplot(mtcars, aes(x = wt, y = mpg)) +
    geom_point() + 
    annotate('text', x = 5, y = 40, label = paste0('r = ', round(p1, 2)), size = 15, color = "darkblue")

p2 <- mtcars %>% summarise(p = cor(hp, mpg)) %>% pull(p)
# 會建議這邊加上 pull()
ggplot(mtcars, aes(x = hp, y = mpg)) + 
    geom_point() + 
    geom_smooth(method = 'lm', se = FALSE, color = 'red') +
    annotate('text', x = 5, y = 40, label = paste0('r = ', round(p2, 2)), size = 15, color = "darkblue")

p3 <- mtcars %>% group_by(cyl) %>%
    summarise(
        correlation = cor(wt, mpg)
    )
print(p3)
# # A tibble: 3 × 2
#     cyl correlation
#   <dbl>       <dbl>
# 1     4      -0.713
# 2     6      -0.682
# 3     8      -0.650


head(mtcars)
