import os
import subprocess

if not os.path.exists('mip_instances'):
  os.mkdir('mip_instances')

subprocess.call('cd mip_instances && wget https://miplib.zib.de/downloads/benchmark.zip', shell=True)
subprocess.call('cd mip_instances && unzip benchmark.zip', shell=True)
os.unlink('mip_instances/benchmark.zip')

