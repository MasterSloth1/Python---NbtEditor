import subprocess
import sys

def run_script(script_name):
    subprocess.run([sys.executable, script_name])

def main():
    scripts = ["nbt2json.py", "searchjsonreplacestrings.py", "json2nbt.py", "deletejsonfiles.py"]
    for script in scripts:
        run_script(script)

    # Print "DONE" message
    print("\n" + "=" * 20 + " DONE " + "=" * 20)

if __name__ == "__main__":
    main()
