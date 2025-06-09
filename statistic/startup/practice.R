# 查看內建資料
data(cars)

# 統計摘要
summary(cars)

# 繪圖
plot(cars)

# 線性回歸
model <- lm(dist ~ speed, data = cars)
summary(model)
abline(model, col="red")

