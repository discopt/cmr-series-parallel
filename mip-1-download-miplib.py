import os

if not os.path.exists('mip-instances'):
  os.mkdir('mip-instances')

os.system('cd mip-instances && wget https://miplib.zib.de/downloads/benchmark.zip')
os.system('cd mip-instances && unzip benchmark.zip')
os.unlink('mip-instances/benchmark.zip')

