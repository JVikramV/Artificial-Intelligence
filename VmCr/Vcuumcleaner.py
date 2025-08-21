import random

# Environment setup for 4 rooms in a 2x2 grid
# 'D' = Dirty, 'C' = Clean
rooms = [['D', 'C'],  # Room 1 (Dirty), Room 2 (Clean)
         ['D', 'D']]  # Room 3 (Dirty), Room 4 (Dirty)

# Vacuum Cleaner Agent
class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Agent starts at the top-left corner (Room 1)
    
    # Method to print the environment (rooms status)
    def print_environment(self):
        print(f"Room 1: {self.environment[0][0]} | Room 2: {self.environment[0][1]}")
        print(f"Room 3: {self.environment[1][0]} | Room 4: {self.environment[1][1]}")
        print()

    # Method to check if all rooms are clean
    def all_clean(self):
        for row in self.environment:
            if 'D' in row:
                return False
        return True

    # Method to clean the current room
    def clean(self):
        x, y = self.position
        if self.environment[x][y] == 'D':
            print(f"Cleaning room at position {self.position}...")
            self.environment[x][y] = 'C'  # Clean the room

    # Method to move the agent to another room
    def move(self, direction):
        x, y = self.position
        if direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < 1:
            self.position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'right' and y < 1:
            self.position = (x, y + 1)
        else:
            print(f"Move {direction} not possible from position {self.position}.")

    # Method to execute the agent's actions until all rooms are clean
    def run(self):
        steps = 0
        while not self.all_clean():
            steps += 1
            print(f"Step {steps}:")
            self.print_environment()

            x, y = self.position
            if self.environment[x][y] == 'D':
                self.clean()
            else:
                print(f"Room at {self.position} is already clean.")

            # Move to another room (choose a random move for simplicity)
            direction = random.choice(['up', 'down', 'left', 'right'])
            self.move(direction)

            print(f"Moved to position {self.position}")
        
        print("All rooms are clean!")
        self.print_environment()

# Run the Vacuum Cleaner Agent in the environment
agent = VacuumCleanerAgent(rooms)
agent.run()
