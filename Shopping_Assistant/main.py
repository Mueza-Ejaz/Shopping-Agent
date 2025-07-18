import os, asyncio, requests
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def get_productsdata() -> str:
    """Fetch product list from online store"""
    try:
        response = requests.get("https://next-ecommerce-template-4.vercel.app/api/product") # it's a API 
        response.raise_for_status()
        data = response.json()
        products = data.get("products", [])

        if not products:
            return "No products found."
        
        # N/A = not available

        formatted_products = "\n".join([
            f"""
            
                    **{p.get('name', 'N/A')}**  
                     Price: {p.get('price', 'N/A')}
                     Category: {p.get('category', 'N/A')}
                     Stock: {p.get('stockLevel', 'N/A')}"""
            for p in products
        ])

        return f"""***Welcome to your Smart Shopping Assistant!***\n
                    **Here are all the available products:**\n{formatted_products}"""

    except Exception as e:
        return f" Error: {str(e)}"



shopping_agent = Agent(
    name="Shopping Agent",
    instructions="""
    You are a helpful shopping assistant.
    Always call the `get_productsdata` tool when user asks anything about products.
    Just return the readable result from the tool.
    Do not ask follow-up questions.
    """,
    tools=[get_productsdata]
)

async def main():

    print("\n ***Welcome to your smart Shopping Assistant!***\n")

    user_input = input("What would you like to know? (e.g., Find me electronics under 5000, show me grocery items, etc.): ")
    result = await Runner.run(shopping_agent, user_input, run_config=config)

    print("\n Final Output:\n")
    print(result.final_output)

asyncio.run(main())

# **This is a sample query to test the agent**:

# 1- Do you have any sofas in stock?
# 2- Show me all chairs under 1000.
# 3- Can you show me the available products?
# 4-  Show me all kitchen products.
# 5- List all products that are out of stock.
# 6- Display all categories available.
# 7- Find me the cheapest product available.
# 8- I want to see a list of all sofa products sorted by price.
# 9- Are there any products for exactly 1000 rupees?
# 10- Give me a summary of all products with their stock level.





