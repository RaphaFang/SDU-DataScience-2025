var(iris$Sepal.Length)  # 變異數（標準差的square）
sd(iris$Sepal.Length)   # 標準差

# -------------------------------------------------------
iris %>%
  summarise(
    across(
      .cols = where(is.numeric),
      list(
        mean = ~mean(.x, na.rm = TRUE),
        sd = ~sd(.x, na.rm = TRUE),
        var = ~var(.x, na.rm = TRUE)
      ),
      .names = "{fn}_{col}"
    )
  )
#   mean_Sepal.Length sd_Sepal.Length var_Sepal.Length
# 1          5.843333       0.8280661        0.6856935
# 確實是平方倍


# -------------------------------------------------------
# 2.1
var(iris$Petal.Width)
sd(iris$Petal.Width)

# 2.2
iris %>%
    summarise(
        across(
            .cols = where(is.numeric),
            .fns = ~sd(.x, na.rm=TRUE),
            .names = "sd_{col}"
        )
    )

# 2.3
# 這就是我上面的變形

# 2.4
iris %>% group_by(Species) %>%
    summarise(
        across(
            .cols = where(is.numeric),
            .fns = ~sd(.x, na.rm=TRUE)
        )
    )

# 2.5
iris %>% group_by(Species) %>%
    summarise(
        across(
            .cols = where(is.numeric),
            list(
                mean = ~mean(.x, na.rm = TRUE),
                sd = ~sd(.x, na.rm = TRUE)
                # var = ~var(.x, na.rm = TRUE)
            ),
            .names = "{fn}_{col}"
        )
    )