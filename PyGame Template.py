import pygame as PG # You will need to install the PyGame module

PG.init()
PG.joystick.init()

# Constants
WIDTH, HEIGHT = 2560, 1440 # Adjust as needed for your screen resolution

FPS = 120 # Adjust as needed for your desired frame rate

BG_COLOR = (255, 255, 255) # Change to your desired background color

PLAYER_COLOR = (0, 0, 255) # Change to your desired player color

PLAYER_SIZE = 50 # Adjust as needed for your desired player size

PLAYER_SPEED = 5 # Adjust as needed for your desired player speed

# Set up the display
screen = PG.display.set_mode((WIDTH, HEIGHT))
PG.display.set_caption("PyGame Template")

# Set up the clock for controlling the frame rate
clock = PG.time.Clock()

# Initialize joystick
joystick = None
if PG.joystick.get_count() > 0:
    joystick = PG.joystick.Joystick(0)
    joystick.init()

# Sprite groups
all_sprites = PG.sprite.Group()

# set up players, enemies, and other game objects here
class Player(PG.sprite.Sprite):
    def __init__(self, x, y, width=PLAYER_SIZE, height=PLAYER_SIZE, color=PLAYER_COLOR):
        super().__init__()
        self.image = PG.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.width = width
        self.height = height

    def update(self, keys, joystick=None):
        """Handle input and update position"""
        # Controller movement (prioritized)
        if joystick:
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            if abs(x_axis) > 0.1 or abs(y_axis) > 0.1:
                self.rect.x += x_axis * PLAYER_SPEED
                self.rect.y += y_axis * PLAYER_SPEED
            else:
                # Keyboard movement
                if keys[PG.K_LEFT] or keys[PG.K_a]:
                    self.rect.x -= PLAYER_SPEED
                if keys[PG.K_RIGHT] or keys[PG.K_d]:
                    self.rect.x += PLAYER_SPEED
                if keys[PG.K_UP] or keys[PG.K_w]:
                    self.rect.y -= PLAYER_SPEED
                if keys[PG.K_DOWN] or keys[PG.K_s]:
                    self.rect.y += PLAYER_SPEED
        else:
            # Keyboard movement (if no joystick)
            if keys[PG.K_LEFT] or keys[PG.K_a]:
                self.rect.x -= PLAYER_SPEED
            if keys[PG.K_RIGHT] or keys[PG.K_d]:
                self.rect.x += PLAYER_SPEED
            if keys[PG.K_UP] or keys[PG.K_w]:   
                self.rect.y -= PLAYER_SPEED
            if keys[PG.K_DOWN] or keys[PG.K_s]:
                self.rect.y += PLAYER_SPEED
        
        # Keep player on screen
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.height))


# Create player instance
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)

# Main game loop
running = True

while running:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            running = False

    # Get input and update
    keys = PG.key.get_pressed()
    player.update(keys, joystick)

    # Fill the background
    screen.fill(BG_COLOR)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    PG.display.flip()
    clock.tick(FPS)