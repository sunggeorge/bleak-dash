import asyncio
import random
from dash.robot import DashRobot, discover_and_connect

class Chatbot:
    _robot = None  # Class property holding the current chatbot instance
    _address = None

    def __init__(self, address):
        self._address = address

    async def _connect(self):
        # robot = await discover_and_connect()
        
        self._robot = DashRobot(self._address)
        await self._robot.connect()    
        if not self._robot:
            print("No compatible robot found.")
            return

        try:
            if isinstance(self._robot, DashRobot):
                print("Dash detected.")
                # await test_dash_movements(robot)
            else:
                print("Dot detected.")

            # await test_dash_say(robot)
            # await test_basic_interactions(robot)

        finally:            
            print("Completed connection process.")

            # await self._robot.say("hi")  # Play a sound
            await asyncio.sleep(1)            

    # @classmethod
    # def isConnected(self) -> bool:  
    #     return self._robot.client.is_connected
        
    
    async def connect(self):
        # chatbot = cls(identifier)
        await self._connect()
        # cls.instance = chatbot
        # return chatbot

    async def say(self, message):
        print(f"Chatbot says: {message}")
        await asyncio.sleep(0.5)

    async def send_message(self, message):
        print(f"Sending message: {message}")
        await asyncio.sleep(0.5)

    # Main function to discover and test Dash or Dot
    async def disconnect(self):
        print("Disconnecting... ")        
        if self._robot:
            # Ensuring graceful disconnect            
            print("Saying goodbye...")
            await self._robot.say("bye")  # Play a sound
            # await asyncio.sleep(1) 
            print("Resetting...")
            await self._robot.reset(4)  # Soft reset as a gentle cleanup
            print("Disconnecting gracefully.")
            await self._robot.disconnect()
            print("Disconnected gracefully.")

    # Function for basic interactions that both Dot and Dash can perform
    async def say_action(self):
        print("Doing say function...")

        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFFFFF', '#FFA500', '#FF1493', '#8A2BE2', '#00CED1', '#32CD32', '#FFD700', '#FF4500']
        neck_color = random.choice(colors)
        ear_color = random.choice(colors)
        eye_pattern = random.randint(1, 4095)  # Random pattern for eye LEDs
        tail_brightness = random.randint(150, 255)  # Random brightness for tail light

        # Set random colors and patterns for each light
        if hasattr(self._robot, 'neck_color'):
            await self._robot.neck_color(neck_color)
        if hasattr(self._robot, 'left_ear_color') and hasattr(self._robot, 'right_ear_color'):
            await self._robot.left_ear_color(ear_color)
            await self._robot.right_ear_color(ear_color)
        if hasattr(self._robot, 'eye'):
            await self._robot.eye(eye_pattern)
        if hasattr(self._robot, 'tail_brightness'):
            await self._robot.tail_brightness(tail_brightness)

        # await robot.move(100, 100)  # Move 100mm at 100mm/s

        # Randomly move the head back and forth (head nodding) synchronized with the lights
        # await asyncio.sleep(0.5)  # Delay for synchronized movement
        # await robot.head_yaw(30)  # Turn head to one side
        # await asyncio.sleep(0.5)  # Delay for synchronized movement
        # await robot.head_yaw(-30)  # Turn head to the other side
        # await asyncio.sleep(0.5)  # Delay for synchronized movement
        # await robot.head_yaw(0)  # Return head to center position



        # await self.robot.spin(50)  # Gentle spin right
        # await asyncio.sleep(2)

        # print("Spinning left...")
        # await self.robot.spin(-50)  # Gentle spin left
        # await asyncio.sleep(2)

        # # await robot_instance.say("hi")  # Play a sound
        # await self.robot.say("bragging")  # Play a sound
        # # await robot_instance.say("
        # # ayayay")  # Play a sound
        # await asyncio.sleep(1)
        
        

        # print("Say function test completed.")


# if __name__ == "__main__":
#     asyncio.run(Chatbot.connect())