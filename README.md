# Ebay Data Scraper MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-ebay_data_scraper`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Ebay Data Scraper API。

- **PyPI 包名**: `bach-ebay_data_scraper`
- **版本**: 2.0.0
- **传输协议**: stdio


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

### API 认证

此 API 需要认证。请设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | API 密钥 | 是 |
| `PORT` | 不适用 | 否 |
| `HOST` | 不适用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "ebay_data_scraper": {
      "command": "uvx",
      "args": ["--from", "bach-ebay_data_scraper", "bach_ebay_data_scraper"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 请将 `E:\path\to\ebay_data_scraper\server.py` 替换为实际的服务器文件路径。


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

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自动生成。

版本: 2.0.0
