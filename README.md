# Messaging App
Temirlan Myrzakhmetov, Lablup Bootcamp, Task1

## Installation Instructions

- Install all the missing libraries by "pip install library_name" into your virtual environment.

### Redis Setup
- Run "brew install redis" to install Redis on your MacOS. 
- Run "brew services [--verbose] start redis" to start redis server. Otherwise, the app won't be able to connect to the Redis server and will throw an error.

Respective instructions for Windows can be found on the Internet.

### Server Start
- Run "python ./app.py" from the root folder. Note that it will occupy one of terminal windows.

### Connection to the Server as a Client
- Open your web-browser.
- Go to "localhost:8080" and the chat will work in case everything is fine with the server. If the server is running on someone-else's machine, then go to "server_machine_ip_address:8080" to connect to the chat.

## Versions of Libraries in the Virtual Environment (TODO: list all the used versions here
Package              Version   Location                                                               
-------------------- --------- -----------------------------------------------------------------------
aiodns               2.0.0     
aiohttp              3.5.4     
aiohttp-debugtoolbar 0.5.0     
aiohttp-jinja2       1.1.1     
aiohttp-session      2.7.0     
aioredis             1.2.0     
aioresponses         0.6.0     
async-timeout        3.0.1     
asynctest            0.13.0    
atomicwrites         1.3.0     
attrs                19.1.0    
backend.ai-client    19.6.0a1  /Users/temirlanmyrzakhmetov/metabackend.ai/backend.ai-dev/client-py/src
backend.ai-common    19.6.0a1  /Users/temirlanmyrzakhmetov/metabackend.ai/backend.ai-dev/common/src   
bleach               3.1.0     
cchardet             2.1.4     
certifi              2019.6.16 
cffi                 1.12.3    
chardet              3.0.4     
Click                7.0       
codecov              2.0.15    
coverage             4.5.3     
docutils             0.14      
entrypoints          0.3       
etcd3                0.8.1     
flake8               3.7.7     
grpcio               1.21.1    
hiredis              1.0.0     
humanize             0.5.1     
idna                 2.8       
importlib-metadata   0.18      
Jinja2               2.10.1    
MarkupSafe           1.1.1     
mccabe               0.6.1     
more-itertools       7.0.0     
msgpack              0.6.1     
multidict            4.5.2     
namedlist            1.7       
packaging            19.0      
pip                  19.1.1    
pkginfo              1.5.0.1   
pluggy               0.12.0    
protobuf             3.8.0     
py                   1.8.0     
pycares              3.0.0     
pycodestyle          2.5.0     
pycparser            2.19      
pyflakes             2.1.1     
Pygments             2.4.2     
pyparsing            2.4.0     
pytest               3.9.3     
pytest-asyncio       0.10.0    
pytest-cov           2.7.1     
pytest-mock          1.10.4    
pytest-sugar         0.9.2     
python-dateutil      2.8.0     
python-json-logger   0.1.11    
pyzmq                18.0.1    
readme-renderer      24.0      
requests             2.22.0    
requests-toolbelt    0.9.1     
setproctitle         1.1.10    
setuptools           41.0.1    
six                  1.12.0    
tabulate             0.8.3     
tenacity             5.0.4     
termcolor            1.1.0     
tqdm                 4.32.2    
trafaret             1.2.0     
twine                1.13.0    
urllib3              1.25.3    
wcwidth              0.1.7     
webencodings         0.5.1     
wheel                0.33.4    
yarl                 1.3.0     
zipp                 0.5.1 

