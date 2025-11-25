# Ebay Data Scraper MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

## 🚀 Quick Start with EMCP Platform

**[EMCP](https://sit-emcp.kaleido.guru)** is a powerful MCP server management platform that allows you to quickly use various MCP servers without manual configuration!

### Quick Start:

1. 🌐 Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)**
2. 📝 Register and login
3. 🎯 Go to **MCP Marketplace** to browse all available MCP servers
4. 🔍 Search or find this server (`bach-ebay_data_scraper`)
5. 🎉 Click the **"Install MCP"** button
6. ✅ Done! You can now use it in your applications

### EMCP Platform Advantages:

- ✨ **Zero Configuration**: No need to manually edit config files
- 🎨 **Visual Management**: Easy-to-use GUI for managing all MCP servers
- 🔐 **Secure & Reliable**: Centralized API key and authentication management
- 🚀 **One-Click Install**: Rich selection of servers in MCP Marketplace
- 📊 **Usage Statistics**: Real-time service call monitoring

Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)** now to start your MCP journey!


---

## Introduction

This is an automatically generated MCP server using [FastMCP](https://fastmcp.wiki) for accessing the Ebay Data Scraper API.

- **PyPI Package**: `bach-ebay_data_scraper`
- **Version**: 1.0.0
- **Transport Protocol**: stdio


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

## Configuration

### API Authentication

This API requires authentication. Please set environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | API Key | Yes |
| `PORT` | N/A | No |
| `HOST` | N/A | No |



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

**Note**: Replace `E:\path\to\ebay_data_scraper\server.py` with the actual server file path.


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

This server is automatically generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 1.0.0
