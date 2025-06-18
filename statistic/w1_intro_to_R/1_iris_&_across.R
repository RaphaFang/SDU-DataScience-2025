# install.packages("dplyr")
library(dplyr)

head(iris)

# -------------------------------------------------------
iris %>%
  summarise(
    across(
      .cols = where(is.numeric), # 這邊挑出只是數字的
      ~mean(.x, na.rm = TRUE), # x是placeholder, na.rm = TRUE這邊是說 na數值忽略
      .names = "mean_{.col}"
    )
  )


# -------------------------------------------------------
# exercise
# 1.1 
mean(iris$Petal.Width)

# 1.2
mean(iris$Sepal.Length, na.rm=TRUE)

# 1.3
mean(iris$Sepal.Width)
iris %>% summarise(mean_sepal = mean(Sepal.Width))

# 1.4
iris %>%
summarise(
    across(
        .cols = where(is.numeric),
        .fns = ~mean(.x, na.rm=TRUE)
    )
)

# 1.5
iris %>%
    summarise(
        across(
            .cols = where(is.numeric),
            list(
                mean = ~mean(.x, na.rm=TRUE),
                sd = ~sd(.x, na.rm=TRUE)
            ),
            .names = "{fn}_{col}" # {fn} 會被替換成 mean / sd
        )
    )

# -------------------------------------------------------
# 在 R 的函式呼叫中，逗號 後面必須要跟一個引數。
# 如果結尾留了一個逗號，parser 會視為「還有一個 Unnamed 引數，但是內容是空的」。
# 這個「空白引數」會被轉成物件 alist()，然後一路傳進 across()；
# across() 看到不明物件，會把它當成「另一個要套用的函式」，結果在做

# mean(alist(), na.rm = TRUE)
# 時就觸發
# unused argument (alist()) 錯誤訊息。
# -------------------------------------------------------

# 1.6
iris2 <- iris
iris2[1, "Petal.Length"] <- NA
head(iris2)
head(iris)
# 確實有一個數值是NA

# 1.7
iris %>% group_by(Species) %>%
    summarise(
        across(
            .cols = Petal.Width,
            .fns = ~mean(.x, na.rm=TRUE)
        )
    )

# 1.8
iris %>% group_by(Species) %>%
    summarise(
        across(
            .cols = where(is.numeric),
            .fns = ~mean(.x, na.rm=TRUE)
        )
    )

# 1.9
scores <- c(90, 80, 70)
weights <- c(0.5, 0.3, 0.2)
weighted.mean(scores, weights)
mean(scores)

# 1.10
head(diamonds)
diamonds %>%
  group_by(cut) %>%
  summarise(
    across(
      .cols = c(price, carat),
      .fns = ~mean(.x, na.rm = TRUE),
      .names = "mean_{col}"
    )
  )
