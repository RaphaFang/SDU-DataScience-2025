p <- ggplot(mtcars, aes(x = mpg, fill = factor(cyl))) +
  geom_density(alpha = 0.5)

ggsave("statistic/w2_data_manipulate/my_density.png", plot = p)
ggsave("statistic/w2_data_manipulate/my_density_plot.pdf", plot = p, width = 8, height = 5, dpi = 300)

getwd()
# 他會提供目前專案路徑
# "/Users/fangsiyu/Desktop/preview-SDU-2025"

# ------------------------------------------------------------------
filename <- paste0("statistic/w2_data_manipulate/mpg_density_", Sys.Date(), ".png")
ggsave(filename, plot = p)
# mpg_density_2025-06-26.png

# | 函數             | 說明                              |
# | --------------- | --------------------------------  |
# | `paste()`       | 合併字串（預設有空白間隔）            |
# | `paste0()`      | 合併字串（**無間隔**，常用）         |
# | `str_c()`       | **stringr 套件**的合併函數（更穩定） |
# | `str_sub()`     | 擷取字串的一部分（等同 `substring`） |
# | `str_replace()` | 替換字串中的內容                    |


# ------------------------------------------------------------------
# 使用 ggplot() 建立一張密度圖（mtcars$hp）
p <- ggplot(mtcars,aes(x = hp)) + 
    geom_density()

# 將圖儲存為 plots/hp_density.pdf，圖寬為 6 吋，高 4 吋，解析度為 300 dpi
ggsave('statistic/w2_data_manipulate/hp_density.pdf', plot = p, width = 6, height = 4, dpi = 300)
# 再將同張圖儲存為 PNG 檔，名稱中包含今日日期

file_name <- paste0('statistic/w2_data_manipulate/hp_density_', Sys.Date(), ".png")
ggsave(file_name, plot = p, width = 6, height = 4, dpi = 300)

# 額外挑戰：試著建立子資料夾（若不存在）後再儲存
dir.create('statistic/w2_data_manipulate/testing')
dir.create("statistic/w2_data_manipulate/testing", showWarnings = FALSE, recursive = TRUE)
# recursive = TRUE
# 如果上層資料不在，一併建立，