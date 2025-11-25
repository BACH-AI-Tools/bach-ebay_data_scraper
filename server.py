"""
Ebay Data Scraper MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "ebay_data_scraper/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Ebay Data Scraper\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: augsmachado/ebay-data-scraper\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://ebay-data-scraper.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/products\": {\n      \"get\": {\n        \"summary\": \"Search products\",\n        \"description\": \"This endpoint can be used to search a products based in the name.  The USA subdomain not need to be selected, because it is the mais domain.  **Allowed *country* params** - australia - austria - canada - france - germany - hong kong - ireland - italy - malaysia - netherlands - philippines - poland - singapore - spain - switzerland - united kingdom\",\n        \"operationId\": \"search_products\",\n        \"parameters\": [\n          {\n            \"name\": \"product_name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: paper ink\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"country\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: canada\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"buy_now\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: true\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/products/{id}\": {\n      \"get\": {\n        \"summary\": \"Get product details\",\n        \"description\": \"This endpoint request a specific product infos. You must provider in each request only one parameter: product_id  The USA subdomain not need to be selected, because it is the mais domain.  **Allowed *country* params** - australia - austria - canada - france - germany - hong kong - ireland - italy - malaysia - netherlands - philippines - poland - singapore - spain - switzerland - united kingdom\",\n        \"operationId\": \"get_product_details\",\n        \"parameters\": [\n          {\n            \"name\": \"country\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: australia\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: 326150465337\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/deals\": {\n      \"get\": {\n        \"summary\": \"Request the daily global featured deals\",\n        \"description\": \"Request the daily global featured deals\",\n        \"operationId\": \"request_the_daily_global_featured_deals\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/deals/fashion\": {\n      \"get\": {\n        \"summary\": \"Request the daily global fashion deals\",\n        \"description\": \"Request the daily global fashion deals\",\n        \"operationId\": \"request_the_daily_global_fashion_deals\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/deals/home\": {\n      \"get\": {\n        \"summary\": \"Request the daily global home deals\",\n        \"description\": \"Request the daily global home deals\",\n        \"operationId\": \"request_the_daily_global_home_deals\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/status/api\": {\n      \"get\": {\n        \"summary\": \"Request API status\",\n        \"description\": \"Request API status\",\n        \"operationId\": \"request_api_status\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/seller\": {\n      \"get\": {\n        \"summary\": \"Get products by seller name\",\n        \"description\": \"This endpoint get all products sold by seller where each page shows 240 new products.\",\n        \"operationId\": \"get_products_by_seller_name\",\n        \"parameters\": [\n          {\n            \"name\": \"seller_name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: Geekstationparts\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page_number\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 2\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/deals/tech\": {\n      \"get\": {\n        \"summary\": \"Request the daily global tech deals\",\n        \"description\": \"Request the daily global tech deals\",\n        \"operationId\": \"request_the_daily_global_tech_deals\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/status/server\": {\n      \"get\": {\n        \"summary\": \"Request server status\",\n        \"description\": \"Without params\",\n        \"operationId\": \"request_server_status\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "ebay-data-scraper.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://ebay-data-scraper.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="ebay_data_scraper",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "ebay-data-scraper.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Ebay Data Scraper MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()