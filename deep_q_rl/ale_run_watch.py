""" This script runs a pre-trained network with the game
visualization turned on.

Usage:

ale_run_watch.py NETWORK_PKL_FILE [ ROM ]
"""
import subprocess
import sys

def run_watch():
    if sys.argv[1] == 'nips':
        script = './run_nips.py'
    elif sys.argv[1] == 'nature':
        script = './run_nature.py'
    else:
        print 'Usage: python ale_run_watch.py NETWORK_THAT_YOU_TRAINED(nips/nature) NETWORK_PKL_FILE [ ROM ]'
        exit(0)  

    command = [script, '--steps-per-epoch', '0',
               '--test-length', '10000', '--nn-file', sys.argv[2],
               '--display-screen']

    if len(sys.argv) > 3:
        command.extend(['--rom', sys.argv[3]])

    p1 = subprocess.Popen(command)
    
    p1.wait()

if __name__ == "__main__":
    run_watch()
