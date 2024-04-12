import subprocess

def call_other_script():
    try:
        # Replace 'python3' with 'python' if you're on Windows
        subprocess.run(['python3', 'other_script.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    else:
        print("other_script.py executed successfully!")

if __name__ == "__main__":
    call_other_script()
