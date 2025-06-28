scale(mtcars$mpg)

log(mtcars$hp)

sqrt(mtcars$hp)

mtcars %>%
  mutate(across(c(mpg, hp), scale, .names = 'z_{col}'))
# 如果沒有 .name 就會在原先欄位上操作，原地改變

# ------------------------------------------------------------------
# 用 mutate() 為 mtcars 增加一個欄位 mpg_z，是 mpg 的 Z 分數標準化。
mtcars %>% mutate(mpg_z = scale(mpg))

# 用 mutate() 新增一欄 log_hp，表示 hp 的對數轉換。

mtcars %>% mutate(log_hp = log(hp))

# across() 同時對 mpg, hp, wt 做 Z 分數轉換，並命名為 z_{col}。
mtcars %>%
    mutate(across(c(mpg, hp, wt), scale, .names = 'z_{col}'))

# 畫出 mtcars$hp 與 log(hp) 的密度圖，並放在同一張圖中（兩條線）
ggplot() +
  geom_density(data = mtcars, aes(x = hp), fill = "#1f78b4", alpha = 0.4) +
  geom_density(data = mtcars, aes(x = mpg), fill = "#e31a1c", alpha = 0.4)
# 如果在ggplot() 內部預設資料，會沒辦法疊起來

mtcars_long <- mtcars %>%
  transmute(hp = hp, log_hp = mpg, tt = disp) %>%  # transmute() 這邊可以加入多個欄位
  pivot_longer(cols = everything(), 
               names_to = "variable", 
               values_to = "value")
ggplot(mtcars_long, aes(x = value, fill = variable)) +
  geom_density(alpha = 0.5)
# ! pivot_longer() 做的很特別，將欄位化約成兩cols
# | variable | value |
# | -------- | ----- |
# | hp       | 110   |
# | hp       | 120   |
# | ...      | ...   |
# | log\_hp  | 4.7   |
# | log\_hp  | 4.78  |
# | ...      | ...   |


# 畫出 wt 和 z_wt 的密度圖，用 geom_density() + pivot_longer() + fill 上色來比較變化
# 整理成長格式：兩欄變成一欄
long <- mtcars %>%
    transmute(a= wt, b=scale(wt)) %>%
    pivot_longer(cols = everything(),
                names_to = 'variable',
                values_to = 'value')
ggplot(long, aes(x=value, fill=variable)) + 
    geom_density(alpha=0.5)


# e_mutate.R
# 這裡有初步的使用到 mutate 以及 transmute