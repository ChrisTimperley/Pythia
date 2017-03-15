#!/usr/bin/python3
import os
import signal
from timeit import default_timer as timer
from subprocess import Popen, PIPE, TimeoutExpired

TIMEOUT = 5
cmd = "./loop.sh"

with Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, preexec_fn=os.setsid) as p:
    try:
        t_start = timer()
        stdout, stderr = p.communicate(timeout=TIMEOUT)
        t_end = timer()
        stdout = str(stdout)[2:-1]
        stderr = str(stderr)[2:-1]
        retcode = p.returncode
        print("Terminated okay!")
    except TimeoutExpired:
        print("Timed out")
        os.killpg(p.pid, signal.SIGINT)
        print("Tried to kill process group")
