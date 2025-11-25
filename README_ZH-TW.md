# Ebay Data Scraper MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-ebay_data_scraper`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個使用 [FastMCP](https://fastmcp.wiki) 自動生成的 MCP 伺服器，用於存取 Ebay Data Scraper API。

- **PyPI 套件名**: `bach-ebay_data_scraper`
- **版本**: 1.0.0
- **傳輸協定**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-ebay_data_scraper
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-ebay_data_scraper bach_ebay_data_scraper

# 或指定版本
uvx --from bach-ebay_data_scraper@latest bach_ebay_data_scraper
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-ebay_data_scraper

# 运行（命令名使用下划线）
bach_ebay_data_scraper
```

## 配置

### API 認證

此 API 需要認證。請設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | API 金鑰 | 是 |
| `PORT` | 不適用 | 否 |
| `HOST` | 不適用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "ebay_data_scraper": {
      "command": "python",
      "args": ["E:\path\to\ebay_data_scraper\server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 請將 `E:\path\to\ebay_data_scraper\server.py` 替換為實際的伺服器檔案路徑。


## 可用工具

此服务器提供以下工具:


### `search_products`

This endpoint can be used to search a products based in the name.  The USA subdomain not need to be selected, because it is the mais domain.  **Allowed *country* params** - australia - austria - canada - france - germany - hong kong - ireland - italy - malaysia - netherlands - philippines - poland - singapore - spain - switzerland - united kingdom

**端点**: `GET /products`


**参数**:

- `product_name` (string) *必需*: Example value: paper ink

- `country` (string): Example value: canada

- `buy_now` (string): Example value: true



---


### `get_product_details`

This endpoint request a specific product infos. You must provider in each request only one parameter: product_id  The USA subdomain not need to be selected, because it is the mais domain.  **Allowed *country* params** - australia - austria - canada - france - germany - hong kong - ireland - italy - malaysia - netherlands - philippines - poland - singapore - spain - switzerland - united kingdom

**端点**: `GET /products/{id}`


**参数**:

- `country` (string): Example value: australia

- `id` (string) *必需*: Example value: 326150465337



---


### `request_the_daily_global_featured_deals`

Request the daily global featured deals

**端点**: `GET /deals`



---


### `request_the_daily_global_fashion_deals`

Request the daily global fashion deals

**端点**: `GET /deals/fashion`



---


### `request_the_daily_global_home_deals`

Request the daily global home deals

**端点**: `GET /deals/home`



---


### `request_api_status`

Request API status

**端点**: `GET /status/api`



---


### `get_products_by_seller_name`

This endpoint get all products sold by seller where each page shows 240 new products.

**端点**: `GET /seller`


**参数**:

- `seller_name` (string) *必需*: Example value: Geekstationparts

- `page_number` (string): Example value: 2



---


### `request_the_daily_global_tech_deals`

Request the daily global tech deals

**端点**: `GET /deals/tech`



---


### `request_server_status`

Without params

**端点**: `GET /status/server`



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自動生成。

版本: 1.0.0
