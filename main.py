import argparse
from screenshot import Screenshot

def main():
    parser = argparse.ArgumentParser(description="Voice-Activated Screenshot Tool")
    parser.add_argument("--mode", choices=["screen", "region"], default="screen", help="Capture mode: screen or region")
    args = parser.parse_args()

    screenshot_taker = Screenshot()

    if args.mode == "screen":
        filepath = screenshot_taker.capture_screen()
        print(f"Screenshot saved to: {filepath}")
    elif args.mode == "region":
        print("Enter region coordinates (x, y, width, height): ")
        x, y, width, height = map(int, input().split())
        filepath = screenshot_taker.capture_region(x, y, width, height)
        print(f"Screenshot saved to: {filepath}")

if __name__ == "__main__":
    main()
