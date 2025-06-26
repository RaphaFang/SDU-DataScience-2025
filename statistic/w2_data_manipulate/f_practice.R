data <- mtcars %>% mutate(targets = (hp > 100) & (wt < 3))
ggplot(data, aes(x = mpg, fill = targets)) + 
    geom_density(alpha = 0.5)
    # 呈現這樣兩種圖形的重疊嗎？

# ------------------------------------------------------------------
data <- mtcars %>% mutate(
    hp_per_wt = hp / wt,
    target = (mpg > 20) & (hp_per_wt > 40))
ggplot(data, aes(x = wt, y = mpg)) + 
    geom_point() + 
    geom_smooth(method = 'lm', se = FALSE)

# ------------------------------------------------------------------
sport <- mtcars %>% mutate(
    is_sports_car = if_else((hp > 100) & (wt < 3), "Yes", "No"))
ggplot(sport, aes(x= mpg, fill = factor(is_sports_car))) + 
    geom_density(alpha = 0.5)

# ------------------------------------------------------------------
ggplot(sport, aes(x= mpg, fill = is_sports_car)) + 
    geom_density(alpha = 0.5) + 
    facet_wrap(~is_sports_car)