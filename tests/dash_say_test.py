import asyncio
import random
from dash.robot import DashRobot, discover_and_connect

# Function to test Dash-specific movements and interactions
async def test_dash_movements(dash_robot):
    print("Testing Dash-specific movements...")

    # Movement tests
    print("Moving forward slightly...")
    await dash_robot.drive(100)  # Gentle forward movement
    await asyncio.sleep(2)  # Wait for movement to complete

    print("Spinning right...")
    await dash_robot.spin(100)  # Gentle spin right
    await asyncio.sleep(2)

    print("Spinning left...")
    await dash_robot.spin(-100)  # Gentle spin left
    await asyncio.sleep(2)

    print("Moving backward slightly...")
    await dash_robot.drive(-100)  # Gentle backward movement
    await asyncio.sleep(2)

    # Additional Dash capabilities
    print("Adjusting head yaw and pitch...")
    await dash_robot.head_yaw(15)  # Slight turn right
    await asyncio.sleep(1)
    await dash_robot.head_yaw(-15)  # Slight turn left
    await asyncio.sleep(1)
    await dash_robot.head_pitch(5)  # Slight look up
    await asyncio.sleep(1)
    await dash_robot.head_pitch(-5)  # Slight look down
    await asyncio.sleep(1)

    print("Dash-specific movements test completed.")

# Function for basic interactions that both Dot and Dash can perform
async def test_basic_interactions(robot_instance):
    print("Testing basic interactions...")

    # LED and sound interactions
    print("Changing colors...")
    await robot_instance.neck_color("#FF00FF")  # Example color
    await asyncio.sleep(1)
    await robot_instance.left_ear_color("#00FF00")  # Example color
    await asyncio.sleep(1)
    await robot_instance.right_ear_color("#0000FF")  # Example color
    await asyncio.sleep(1)

    print("Playing a sound...")
    await robot_instance.say("hi")  # Play a sound
    await asyncio.sleep(1)

    print("Basic interactions test completed.")

# Function for basic interactions that both Dot and Dash can perform
async def test_dash_say(robot):
    print("Testing say function...")

    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFFFFF', '#FFA500', '#FF1493', '#8A2BE2', '#00CED1', '#32CD32', '#FFD700', '#FF4500']
    neck_color = random.choice(colors)
    ear_color = random.choice(colors)
    eye_pattern = random.randint(1, 4095)  # Random pattern for eye LEDs
    tail_brightness = random.randint(150, 255)  # Random brightness for tail light

    # Set random colors and patterns for each light
    if hasattr(robot, 'neck_color'):
        await robot.neck_color(neck_color)
    if hasattr(robot, 'left_ear_color') and hasattr(robot, 'right_ear_color'):
        await robot.left_ear_color(ear_color)
        await robot.right_ear_color(ear_color)
    if hasattr(robot, 'eye'):
        await robot.eye(eye_pattern)
    if hasattr(robot, 'tail_brightness'):
        await robot.tail_brightness(tail_brightness)

    # await robot.move(100, 100)  # Move 100mm at 100mm/s

    # Randomly move the head back and forth (head nodding) synchronized with the lights
    # await asyncio.sleep(0.5)  # Delay for synchronized movement
    # await robot.head_yaw(30)  # Turn head to one side
    # await asyncio.sleep(0.5)  # Delay for synchronized movement
    # await robot.head_yaw(-30)  # Turn head to the other side
    # await asyncio.sleep(0.5)  # Delay for synchronized movement
    # await robot.head_yaw(0)  # Return head to center position

    await robot.spin(50)  # Gentle spin right
    await asyncio.sleep(2)

    print("Spinning left...")
    await robot.spin(-50)  # Gentle spin left
    await asyncio.sleep(2)

    # await robot_instance.say("hi")  # Play a sound
    await robot.say("bragging")  # Play a sound
    # await robot_instance.say("
    # ayayay")  # Play a sound
    await asyncio.sleep(1)

    print("Say function test completed.")

# Main function to discover and test Dash or Dot
async def main():
    # robot = await discover_and_connect()
    known_address = "CE:51:B9:38:E1:D4"
    robot = DashRobot(known_address)
    await robot.connect()    
    if not robot:
        print("No compatible robot found.")
        return

    try:
        if isinstance(robot, DashRobot):
            print("Dash detected.")
            # await test_dash_movements(robot)
        else:
            print("Dot detected.")

        await test_dash_say(robot)
        # await test_basic_interactions(robot)

    finally:
        # Ensuring graceful disconnect
        print("Cleaning up and disconnecting...")
        await robot.reset(4)  # Soft reset as a gentle cleanup
        await robot.disconnect()
        print("Disconnected gracefully.")

if __name__ == "__main__":
    asyncio.run(main())
