import os
import subprocess

if not os.path.exists('mip-instances'):
  os.mkdir('mip-instances')

subprocess.call('cd mip-instances && wget https://miplib.zib.de/downloads/benchmark.zip', shell=True)
subprocess.call('cd mip-instances && unzip benchmark.zip', shell=True)
os.unlink('mip-instances/benchmark.zip')

