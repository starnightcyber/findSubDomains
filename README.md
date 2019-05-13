# findSubDomains
A tool finding sub-domains of a target site for us penetesters.

Switch to python3 for simplication @2019.5.13.

## Preface
这个脚本源自lijiejie/subDomainsBrute， 用来探测子域名，我删除了很多代码，也添加了不少注释，使得代码变得更简练和清晰。

你可以在这看到找到这个项目： https://github.com/lijiejie/subDomainsBrute

## Dependencies

    pip3 install dnspython gevent

## Usage

    python3 findSubDomains.py [your target domain]

## Example
    
    starnight:findSubDomains starnight$ python3 findSubDomains.py qq.com
	[*] Validate DNS servers ...
	[+] Check DNS Server 119.29.29.29     < OK >   Found 4                                                                                                                                                                                                                                                                                                      
	[*] Found 4 available DNS Servers in total
	[+] Load sub names ...                                                                                                                                                                                                                                                                                                                                      
	[+] Load sub names ...                                                                                                                                                                                                                                                                                                                                      
	[*] Exploiting sub domains of  qq.com
	[+] There are 15372 subs waiting for trying ...
	--------------------------------------
	[*] Initializing 100 threads
	007.qq.com       61.129.7.119
	108.qq.com       180.153.105.147, 180.153.105.153, 180.153.105.161, 180.153.105.162, 180.153.105.173, 180.153.105.195
	114.qq.com       183.61.51.35
	2010.qq.com      61.129.7.47
	2011.qq.com      61.129.7.47
	2014.qq.com      61.129.7.47
	123.qq.com       180.163.26.39
	1.qq.com         101.89.15.139
	2012.qq.com      61.129.7.47
	2008.qq.com      180.163.26.39
	12.qq.com        180.163.26.39
	17.qq.com        183.3.225.113
	3.qq.com         180.153.105.147, 180.153.105.153, 180.153.105.161, 180.153.105.162, 180.153.105.173, 180.153.105.195
	3g.qq.com        61.151.168.204
	3d.qq.com        180.153.105.147, 180.153.105.153, 180.153.105.161, 180.153.105.162, 180.153.105.173, 180.153.105.195


