import subprocess
import sys

def main():
    print("Starting Javid Self Bot...")
    selfbot = subprocess.Popen([sys.executable, "self.py"], cwd="/app")
    try:
        selfbot.wait()
    except KeyboardInterrupt:
        selfbot.terminate()

if __name__ == "__main__":
    main()
