import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🇮🇳 Stylish Indian Flag Animation 🇮🇳")
screen.setup(width=1200, height=800)
screen.tracer(0)  # Turn off animation for faster drawing

# Create turtles for different parts
flag_turtle = turtle.Turtle()
chakra_turtle = turtle.Turtle()
text_turtle = turtle.Turtle()
effect_turtle = turtle.Turtle()

# Hide all turtles
for t in [flag_turtle, chakra_turtle, text_turtle, effect_turtle]:
    t.hideturtle()
    t.speed(0)

# Indian flag colors
SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
GREEN = "#138808" 
NAVY_BLUE = "#000080"
GOLD = "#FFD700"
SILVER = "#C0C0C0"

def draw_waving_flag():
    """Draw a waving Indian flag effect"""
    flag_turtle.clear()
    
    # Flag dimensions
    width = 450
    height = 300
    waves = 6
    
    # Draw saffron band with wave effect
    flag_turtle.color(SAFFRON)
    flag_turtle.begin_fill()
    flag_turtle.penup()
    flag_turtle.goto(-width//2, height//3)
    flag_turtle.pendown()
    
    # Top wavy line
    for i in range(50):
        x = -width//2 + (i * width/49)
        y = height//3 + 15 * math.sin(i * 0.3 + time.time() * 3)
        flag_turtle.goto(x, y)
    
    # Straight right edge
    flag_turtle.goto(width//2, height//3)
    flag_turtle.goto(width//2, 0)
    
    # Bottom wavy line
    for i in range(50, 0, -1):
        x = -width//2 + (i * width/49)
        y = 10 * math.sin(i * 0.3 + time.time() * 3)
        flag_turtle.goto(x, y)
    
    flag_turtle.goto(-width//2, height//3)
    flag_turtle.end_fill()
    
    # Draw white band
    flag_turtle.color(WHITE)
    flag_turtle.begin_fill()
    flag_turtle.penup()
    flag_turtle.goto(-width//2, 0)
    flag_turtle.pendown()
    
    for i in range(50):
        x = -width//2 + (i * width/49)
        y = 10 * math.sin(i * 0.3 + time.time() * 3)
        flag_turtle.goto(x, y)
    
    flag_turtle.goto(width//2, 0)
    flag_turtle.goto(width//2, -height//3)
    
    for i in range(50, 0, -1):
        x = -width//2 + (i * width/49)
        y = -height//3 + 10 * math.sin(i * 0.3 + time.time() * 3)
        flag_turtle.goto(x, y)
    
    flag_turtle.goto(-width//2, 0)
    flag_turtle.end_fill()
    
    # Draw green band
    flag_turtle.color(GREEN)
    flag_turtle.begin_fill()
    flag_turtle.penup()
    flag_turtle.goto(-width//2, -height//3)
    flag_turtle.pendown()
    
    for i in range(50):
        x = -width//2 + (i * width/49)
        y = -height//3 + 10 * math.sin(i * 0.3 + time.time() * 3)
        flag_turtle.goto(x, y)
    
    flag_turtle.goto(width//2, -height//3)
    flag_turtle.goto(width//2, -height//2 - 50)
    
    for i in range(50, 0, -1):
        x = -width//2 + (i * width/49)
        y = -height//2 - 50 + 15 * math.sin(i * 0.3 + time.time() * 3)
        flag_turtle.goto(x, y)
    
    flag_turtle.goto(-width//2, -height//3)
    flag_turtle.end_fill()

def draw_rotating_chakra():
    """Draw animated Ashoka Chakra"""
    chakra_turtle.clear()
    chakra_turtle.color(NAVY_BLUE)
    chakra_turtle.pensize(3)
    
    # Center position
    cx, cy = 0, -50
    radius = 45
    
    # Outer circle
    chakra_turtle.penup()
    chakra_turtle.goto(cx, cy - radius)
    chakra_turtle.pendown()
    chakra_turtle.circle(radius)
    
    # Inner circle
    chakra_turtle.penup()
    chakra_turtle.goto(cx, cy - 15)
    chakra_turtle.pendown()
    chakra_turtle.circle(15)
    
    # 24 rotating spokes
    rotation = time.time() * 50  # Rotation speed
    
    for i in range(24):
        angle = (i * 15 + rotation) % 360
        
        # Outer point
        outer_x = cx + (radius - 8) * math.cos(math.radians(angle))
        outer_y = cy + (radius - 8) * math.sin(math.radians(angle))
        
        # Inner point
        inner_x = cx + 18 * math.cos(math.radians(angle))
        inner_y = cy + 18 * math.sin(math.radians(angle))
        
        # Draw spoke
        chakra_turtle.penup()
        chakra_turtle.goto(inner_x, inner_y)
        chakra_turtle.pendown()
        chakra_turtle.goto(outer_x, outer_y)
        
        # Draw small circle at end of spoke
        chakra_turtle.penup()
        chakra_turtle.goto(outer_x, outer_y)
        chakra_turtle.pendown()
        chakra_turtle.dot(6, NAVY_BLUE)

def draw_flag_pole():
    """Draw decorative flag pole"""
    effect_turtle.color("#8B4513")
    effect_turtle.pensize(12)
    effect_turtle.penup()
    effect_turtle.goto(-240, 200)
    effect_turtle.pendown()
    effect_turtle.goto(-240, -300)
    
    # Pole decorations
    effect_turtle.color(GOLD)
    effect_turtle.penup()
    effect_turtle.goto(-240, 200)
    effect_turtle.pendown()
    effect_turtle.dot(20)
    
    # Flag attachment
    effect_turtle.color(SILVER)
    effect_turtle.pensize(4)
    effect_turtle.penup()
    effect_turtle.goto(-240, 150)
    effect_turtle.pendown()
    effect_turtle.goto(-225, 150)

def draw_background_effects():
    """Draw background decorative effects"""
    effect_turtle.color("#1a1a2e")
    
    # Draw gradient circles
    for i in range(8):
        effect_turtle.penup()
        effect_turtle.goto(0, -50)
        effect_turtle.pendown()
        effect_turtle.circle(100 + i * 30)

def draw_floating_particles():
    """Draw floating particles around flag"""
    import random
    
    effect_turtle.color(GOLD)
    
    # Create floating golden particles
    for _ in range(15):
        x = random.randint(-500, 500)
        y = random.randint(-300, 300)
        
        # Animate particle position
        offset_x = 20 * math.sin(time.time() * 2 + x * 0.01)
        offset_y = 15 * math.cos(time.time() * 1.5 + y * 0.01)
        
        effect_turtle.penup()
        effect_turtle.goto(x + offset_x, y + offset_y)
        effect_turtle.pendown()
        effect_turtle.dot(4)

def draw_stylish_text():
    """Draw animated text"""
    text_turtle.clear()
    
    # Main title with glow effect
    text_turtle.color(GOLD)
    text_turtle.penup()
    text_turtle.goto(0, 280)
    text_turtle.pendown()
    
    # Create glow effect
    text_turtle.write("भारत माता ", font=("Arial",20, "bold"), align="center")
    
    # Subtitle
    text_turtle.color(WHITE)
    text_turtle.penup()
    text_turtle.goto(0, 240)
    text_turtle.pendown()
    text_turtle.write("INCREDIBLE INDIA", font=("Courier", 18, "bold"), align="center")
    
    # Animated bottom text
    pulse = abs(math.sin(time.time() * 2))
    text_color = (int(255 * pulse), int(255 * pulse), int(255))
    
    text_turtle.color(WHITE)
    text_turtle.penup()
    text_turtle.goto(0, -320)
    text_turtle.pendown()
    text_turtle.write("Unity in Diversity", font=("Times", 16, "italic"), align="center")

def draw_tricolour_border():
    """Draw animated tricolor border"""
    border_turtle = turtle.Turtle()
    border_turtle.hideturtle()
    border_turtle.speed(0)
    
    colors = [SAFFRON, WHITE, GREEN]
    
    for i, color in enumerate(colors):
        border_turtle.color(color)
        border_turtle.pensize(8)
        border_turtle.penup()
        border_turtle.goto(-580 + i*5, 380 - i*5)
        border_turtle.pendown()
        
        # Draw border rectangle with offset
        for _ in range(2):
            border_turtle.forward(1160 - i*10)
            border_turtle.right(90)
            border_turtle.forward(760 - i*10)
            border_turtle.right(90)

# Animation loop
def animate():
    """Main animation function"""
    # Clear previous frame
    screen.clear()
    screen.bgcolor("black")
    
    # Draw all elements
    draw_background_effects()
    draw_tricolour_border()
    draw_floating_particles()
    draw_flag_pole()
    draw_waving_flag()
    draw_rotating_chakra()
    draw_stylish_text()
    
    # Update screen
    screen.update()
    
    
# Start animation
animate()

# Add click to exit
text_turtle.color(WHITE)
text_turtle.penup()
text_turtle.goto(0, -360)
text_turtle.pendown()
text_turtle.write("🇮🇳 Click anywhere to exit 🇮🇳", font=("Arial", 12, "normal"), align="center")

screen.exitonclick()
turtle.done()
