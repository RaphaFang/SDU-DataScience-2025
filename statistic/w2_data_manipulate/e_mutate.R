# mutate, transmute
mtcars %>% mutate(kmpl = mpg * 0.425)
mtcars %>% transmute(kmpl = mpg * 0.425) # 這是只產出一行的，並且會先作 mutate

# ------------------------------------------------------------------
mtcars %>% 
  mutate(
    kmpl = mpg * 0.425,
    hp_per_wt = hp / wt
  )

mtcars %>% 
      mutate(kmpl = mpg * 0.425) %>% 
      select(kmpl)

# ------------------------------------------------------------------
# if_else
mtcars %>% mutate(fuel_efficiency = if_else(mpg > 20, "高", "低"))

# ------------------------------------------------------------------
mtcars %>% mutate(
  power_class = case_when(
    hp < 100 ~ "低",
    hp < 150 ~ "中",
    TRUE ~ "高"
  )
)

# ------------------------------------------------------------------
# 使用 mutate() 新增欄位 kmpl，將 mpg 轉換為 km/L（乘以 0.425）。
mtcars %>% mutate(kmpl = mpg * 0.425)

# 新增欄位 hp_per_wt，代表馬力與車重的比值。
mtcars %>% mutate(hp_per_wt = hp/wt)

# 使用 if_else() 建立新欄位 fuel_efficiency，mpg > 20 則為 "高"，否則為 "低"。
mtcars %>% mutate(fuel_efficiency = if_else(mpg > 20, "高", "低"))

# 使用 case_when() 根據 hp 將車子分為 "低"（<100）、"中"（100–150）、"高"（>150）三類，存入 power_class。
mtcars  %>% mutate(
    power_class = case_when(
        hp < 100 ~ "低",
        hp < 150 ~ "中",
        TRUE ~ "高"
))

# 建立欄位 is_sports_car，當 hp > 150 且 wt < 3 時為 "Yes"，否則為 "No"。
mtcars  %>% mutate(is_sports_car = if_else((hp > 150) & (wt < 3), "Yes", "No"))

# 建立欄位 mpg_z，將 mpg 做 Z 分數標準化（提示：用 scale()）。
mtcars  %>% mutate(mpg_z = scale(mpg))

# 建立欄位 hp_log，存入 hp 的對數值（提示：log() 函數）。
mtcars  %>% mutate(hp_log = log(hp))
