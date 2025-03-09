import asyncio
import os

async def start_server():
    from uvicorn import Config, Server
    config = Config("app:app", port=8000, host="0.0.0.0", reload=True)
    server = Server(config)
    await server.serve()
    
async def start_bot():
    pass

async def main():
    os.environ.clear()
    if __name__ == "__main__":
        asyncio.run(main())