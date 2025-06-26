# | 函數                   | 功能                        |
# | -------------------- | ---------------------------- |
# | `arrange()`          | 排序（預設為升序）              |
# | `arrange(desc(...))` | 降序排序                      |
# | `slice_max()`        | 挑出**最大前 N 筆**            |
# | `slice_min()`        | 挑出**最小前 N 筆**            |
# | `top_n()`            | 過去的函數，現在推薦用 `slice_max()` |

# ------------------------------------------------------------------
mtcars %>% arrange(desc(hp))
mtcars %>% arrange(cyl, desc(mpg))

mtcars %>% slice_max(hp, n=3)
mtcars %>% slice_min(hp, n=3)


mtcars %>% 
    rownames_to_column("model") %>% 
    select(model, hp) %>%
    slice_max(hp, n = 10)
# rownames 理論是資料的id。只是這份資料沒有這id而是這個車名

# ------------------------------------------------------------------
# 挑出每種汽缸數 (cyl) 中，馬力 (hp) 最高的車款
mtcars %>% group_by(cyl) %>%
    slice_max(hp)

# 找出每種汽缸數 (cyl) 中，油耗 (mpg) 最低的 2 台車
mtcars %>% group_by(cyl) %>%
    slice_min(mpg, n =2)


# 先計算每台車的「每公斤馬力比」（hp_per_wt），找出前 5 強性能怪獸
mtcars %>%
  mutate(hp_per_wt = hp / wt) %>%
  slice_max(hp_per_wt, n = 5)
# ! 可以直接 pipe
    # data = mtcars %>% mutate(hp_per_wt = hp/wt)
    # data %>% slice_max(hp_per_wt, n=5)


# 對所有車依照「馬力／油耗比」(hp/mpg) 降序排序，觀察是否符合直覺
mtcars %>% arrange(desc(hp/mpg))

# 計算每種變速 (am) 下，馬力前 3 高的車款名稱與馬力
mtcars %>% group_by(am) %>%
    slice_max(hp, n=3)

# 取出車重 (wt) 最重的前 3 輛車，並只顯示車名、wt、mpg
mtcars %>% 
    rownames_to_column("model") %>%
    select(model, wt, mpg) %>%
    slice_max(wt, n=3)

# 找出油耗 (mpg) 最佳但車重 (wt) 也高於平均的車（前 5 名）
mtcars %>%
  filter(wt > mean(wt)) %>%
  slice_max(mpg, n = 5)
# ! 直接在內部 mean() 就好
    # m_wt <- mtcars %>% summarise(m_wt = mean(wt)) %>% pull(m_wt)
    # mtcars %>% filter(wt > m_wt) %>%
    #     slice_max(mpg, n=5)

