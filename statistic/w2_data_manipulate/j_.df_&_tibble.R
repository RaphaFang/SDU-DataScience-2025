# dplyr 是 tidyverse 裡面的一個成員
# 它是專門負責「資料處理」的套件，最常用的幾個動作就是：

# select()    # 選欄位
# filter()    # 篩選列
# mutate()    # 新增或修改欄位
# summarise() # 彙總
# group_by()  # 分組處理
# arrange()   # 排序

# -------------------------------------------------------
# ! 檢查資料
str(iris)
str(mtcars)

glimpse(iris)
glimpse(mtcars)

# -------------------------------------------------------
# ! 檢查缺值
colSums(is.na(mtcars))
#  mpg  cyl disp   hp drat   wt qsec   vs   am gear carb 
#    0    0    0    0    0    0    0    0    0    0    0 
anyNA(mtcars)  # TRUE or FALSE
# [1] FALSE

na_test <- mtcars %>% 
  bind_rows(rep(NA, ncol(mtcars)) %>% setNames(names(mtcars)))

colSums(is.na(na_test))
#  mpg  cyl disp   hp drat   wt qsec   vs   am gear carb 
#    1    1    1    1    1    1    1    1    1    1    1 
anyNA(na_test)
# [1] TRUE

# -------------------------------------------------------
# ! 檢查 data type
class(mtcars)
# [1] "data.frame"

tibble_mt <- as_tibble(mtcars)
class(tibble_mt)
# [1] "tbl_df"     "tbl"        "data.frame"

# -------------------------------------------------------
# ! build tibble 
tibble(
    name = c("Toyota", "Honda", "Ford"),
    mpg = c(10,10,10),
    hp = c(10,10,10)
)


# -------------------------------------------------------
# 將 mtcars 轉為 tibble 並使用 glimpse 觀察
mtcars_tb <- as_tibble(mtcars)
glimpse(mtcars_tb)
glimpse(mtcars)

# 使用 tribble() 建立你喜歡的三個車名與 mpg