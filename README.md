# 🛍️ AI Shopping Agent

This project is an AI-powered shopping assistant that interacts with users through natural language and fetches real-time product data from a live API. The assistant is designed to understand user prompts and respond intelligently by retrieving relevant product details such as name, price, category, and availability.


## Project Overview

The **AI Shopping Agent** understands user prompts like:

- “Find me electronics under 5000”
- “Display all available products”
- “Show me products in the clothing category”

It then calls a product API, parses the response, and displays the relevant information clearly and accurately.



##  API Used

**[Fake Store API](https://lnkd.in/e992pEid)**  
This API provides real-time product data including:

- Product Name  
- Price  
- Category  
- Stock Level



## Technologies & Tools

- **Python**
- **OpenAI SDK** (`@function_tool`)
- **Requests** library for API calls
- **JSON** for data parsing
- **Custom prompt handling & logic**
- **Robust error handling** and fallback responses



## Key Features

- Understands both **specific** and **general** product-related queries
- Smart parsing of natural language prompts
- Real-time data fetching from external API
- Clean and formatted response for user readability
- Handles errors gracefully and gives meaningful fallback replies



##  Notable Issue Faced

Initially, the agent failed to respond to broad prompts like:

> "Display all available products"

It returned:

> _"I’m sorry, I cannot fulfill this request. I need a category to search for products..."_

This was due to prompt logic not correctly triggering the function for general queries.  
 **Resolved** by improving the prompt analysis logic to handle broader use-cases.




## Final Outcome:

A **fully functional AI shopping assistant** capable of:

- Processing user input in natural language
- Integrating with real-world APIs
- Presenting data in a clean and user-friendly format



## What I Learned

- Prompt engineering for AI agents  
- API integration and debugging  
- Data parsing & formatting  
- Real-time error handling in user queries  
- How to structure AI responses effectively




