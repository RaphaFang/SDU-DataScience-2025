library(ggplot2)

filter()
select()
# ------------------------------------------------------------------
mtcars %>% filter(mpg > 20)

mtcars %>% filter(cyl %in% c(4, 6))
mtcars %>% filter(between(mpg, 15, 25))

iris %>% filter(Species == "setosa")
# ------------------------------------------------------------------
# 選出 mpg > 25 的車子。
mtcars %>% filter(mpg > 25)

# 選出 cyl 為 4 或 6 的車子。
mtcars %>% filter(cyl %in% c(4, 6))

# 選出 mpg > 20 且 hp < 100 的車子。
mtcars %>% filter(mpg > 20 & hp < 100)

# 選出 gear 不為 4 的車子。
mtcars %>% filter(gear != 4)

# 使用 %in% 選出 cyl 為 4、6 的車子。
mtcars %>% filter(cyl %in% c(4, 6))

# 使用 between() 篩出 mpg 介於 15 到 25 的車子。
mtcars %>% filter(15<mpg & mpg<25)
mtcars %>% filter(between(mpg, 15, 25))


mtcars %>% filter(mpg > 25) %>% select(mpg, cyl, hp)
