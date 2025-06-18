install.packages("ggplot2")  # 第一次執行才需要
library(ggplot2)
x <- c(72,75,79,83,91)
z_scores <- as.vector(scale(x))
t_scores <- 50 + z_scores * 10
df <- data.frame(original = x, z = z_scores, t = t_scores)
print(df)
#   original          z        t
# 1       55 -1.1766968 38.23303
# 2       60 -0.7844645 42.15535
# 3       70  0.0000000 50.00000
# 4       80  0.7844645 57.84465
# 5       85  1.1766968 61.76697

# ----------------------------------------------------------------
write.csv(df, "statistic/t_score/scores.csv", row.names = FALSE) # row.names = FALSE 代表不要加上 row index（1,2,3,4,...）

# install.packages("arrow")
library(arrow)
write_parquet(df, "statistic/t_score/scores.parquet")

# "original","z","t"
# 55,-1.1766968108291,38.233031891709
# 60,-0.784464540552736,42.1553545944726
# 70,0,50
# 80,0.784464540552736,57.8446454055274
# 85,1.1766968108291,61.766968108291

# ----------------------------------------------------------------
library(ggplot2)
p <- ggplot(df, aes(x = z, y = t)) +
  geom_point(size = 3, color = "steelblue") +
  ggtitle("T Score pionter") +
  xlab("z-scores") +
  ylab("t-scores") +
  geom_smooth(method = "lm", se = FALSE, color = "grey")

ggsave("statistic/t_score/plot.png", plot = p, width = 6, height = 4)

# dev.off() 他不用加上這個，會自動關閉


# ----------------------------------------------------------------
# install.packages("DBI")
# install.packages("RMySQL")

library(DBI)
library(RMySQL)

con <- dbConnect(RMySQL::MySQL(),
                 dbname = "your_db",
                 host = "localhost",
                 user = "root",
                 password = "your_password")

dbWriteTable(con, "score_table", df, overwrite = TRUE)
dbDisconnect(con)
