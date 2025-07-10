#!/usr/bin/env python3
import webbrowser
import keyboard
import sys
import time

def rickroll():
    """Open the classic Rick Roll video in the default browser"""
    rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("🎵 Never gonna give you up, never gonna let you down! 🎵")
    webbrowser.open(rickroll_url)
    print("You've been rickrolled! Press Ctrl+C to exit.")

def on_key_press(event):
    """Handle key press events"""
    if event.name == 'j':
        print("\nJ key detected! Initiating rickroll...")
        rickroll()

def main():
    print("🎯 Prank Program Active 🎯")
    print("Listening for the 'j' key...")
    print("Press Ctrl+C to exit")
    
    try:
        keyboard.on_press(on_key_press)
        keyboard.wait()
    except KeyboardInterrupt:
        print("\nPrank program stopped!")
        sys.exit(0)

if __name__ == "__main__":
    main()