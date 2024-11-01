import subprocess
from keep_alive import keep_alive
import os

def run_script_in_background(script_name):
    print(f"Running {script_name} in the background...")
    try:
        # Command to run the script in the background
        command = f'nohup python {script_name} &'
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Failed to run {script_name} in the background: {e}")

if __name__ == "__main__":
    # Start keep_alive function to keep the script running
    keep_alive()
    
    script1 = '3ontg018lvph.py'
    script2 = '3tjdy009wzmv.py'
    script3 = '4edae071snnb.py'
    script4 = '4ffsa427ycxe.py'
    script5 = '4jtez107vnrx.py'
    script6 = '4knrb128hioy.py'
    script7 = '4kqlx753cjiq.py'
    script8 = '4mqta532ehjk.py'
    script9 = '4nnyi939oolb.py'
    script10 = '4rcoz527gyfl.py'
   
    

run_script_in_background(script1)
run_script_in_background(script2)
run_script_in_background(script3)
run_script_in_background(script4)
run_script_in_background(script5)
run_script_in_background(script6)
run_script_in_background(script7)
run_script_in_background(script8)
run_script_in_background(script9)
run_script_in_background(script10)