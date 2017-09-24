# findSubDomains
A tool finding sub domains for penetesters

## Preface
这个脚本源自lijiejie/subDomainsBrute， 用来探测子域名，我删除了很多代码，也添加了不少注释，使得代码变得更简练和清晰。

你可以在这看到找到这个项目： https://github.com/lijiejie/subDomainsBrute

## Dependencies

    pip install dnspython gevent

## Usage

    python findSubDomains.py [your target domain]

## Example
    
    ➜  subDomainsBrute git:(master) ✗ python findSubDomains.py baidu.com
    [*] Validate DNS servers ...
    [+] Check DNS Server 223.6.6.6        < OK >   Found 4                                                                                                                
    [*] Found 4 available DNS Servers in total
    [+] Load sub names ...                                                                                                                                                
    [+] Load sub names ...                                                                                                                                                
    [*] Exploiting sub domains of  baidu.com
    [+] There are 15372 subs waiting for trying ...
    --------------------------------------
    [*] Initializing 100 threads
    123.baidu.com   115.239.210.27, 115.239.211.112
    0.baidu.com     180.149.144.203
    1.baidu.com     61.135.186.115
    11.baidu.com    220.181.57.55
    12.baidu.com    220.181.57.166
    100.baidu.com   180.149.131.33
    1111.baidu.com  180.97.93.38
    2013.baidu.com  180.149.131.33
    2014.baidu.com  115.239.210.174, 180.97.33.136
    365.baidu.com   180.149.131.33
    3g.baidu.com    115.239.217.67, 115.239.217.68
    7.baidu.com     61.135.185.212

    
    
