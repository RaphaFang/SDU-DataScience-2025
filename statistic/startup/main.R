# 檢查 R session 的基本環境資訊
cat("✅ 測試開始：檢查 R 環境...\n\n")

# 1. 測試是否載入成功 languageserver
if (!requireNamespace("languageserver", quietly = TRUE)) {
  stop("❌ languageserver 套件未安裝，請先執行 install.packages(\"languageserver\")")
} else {
  cat("✔ languageserver 套件已正確安裝 ✅\n")
}

# 2. 顯示 R 版本與工作目錄
cat("🔧 R 版本：", R.version.string, "\n")
cat("📁 當前工作目錄：", getwd(), "\n\n")

# 3. 建立簡單資料，測試語法提示功能（打 data$ 可補全）
data <- data.frame(name = c("A", "B"), value = c(1, 2))
print(data)

# 4. 測試補全功能（打 lm 回車時會有提示）
m <- lm(value ~ name, data = data)
summary(m)

cat("\n✅ 測試完成！你已成功設定 VS Code + R 開發環境。\n")



# ------------------------------------------------
# 要進入築行運行模式，要先cmd+shift+P
# 輸入 >R: Create R Terminal
# 接著每一行單獨按下 cmd+Enter

# ✅ 幾個類似 radian 的 SQL 終端工具
# | 工具名稱                                | 適用資料庫           | 功能亮點           | 安裝方式                  | 備註                |
# | ----------------------------------- | --------------- | -------------- | --------------------- | ----------------- |
# | **[pgcli](https://www.pgcli.com/)** | PostgreSQL      | 自動補全、語法高亮、多行編輯 | `pip install pgcli`   | 最受歡迎的 SQL CLI 替代品 |
# | **[mycli](https://www.mycli.net/)** | MySQL / MariaDB | 自動補全、語法高亮、多行輸入 | `pip install mycli`   | 與 pgcli 是姊妹工具     |
# | **litecli**                         | SQLite          | 類似上面，支援補全 / 顏色 | `pip install litecli` | 適合開發者日常本地 SQLite  |
