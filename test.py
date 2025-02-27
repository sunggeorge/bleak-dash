from dash.chatbot import Chatbot
import asyncio


async def main():
    try:
        mybot = Chatbot("CE:51:B9:38:E1:D4")
        print("Initializing Chatbot...")
        await mybot.connect()
    except Exception as e:
        print(f"❌ Error initializing Chatbot: {e}")
        return

    print("Connected to Dash.")
    # asyncio.sleep(2)
    # asyncio.run(mybot.say_action())
    
    await mybot.disconnect()




if __name__ == "__main__":
    asyncio.run(main())