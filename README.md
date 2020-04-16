# findSubDomains
A tool finding sub-domains of a target site for penetesters with python3.

## Preface
This script is from starnightcyber/findSubDomains, which is used to detect subdomains. I just make the results files output saved to the folder reuslts each target have a folder with its name.

You can find the original project here:： https://github.com/starnightcyber/findSubDomains

## Dependencies

    python3 -m pip install -r requirements.txt

## Usage

    python3 findSubDomains.py target.com

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
	...
	zip.mail.qq.com	14.17.19.106
	zip.m.qq.com	101.227.131.64
	zip.photo.qq.com	183.61.46.186
	zip.zg.qq.com	122.228.0.141, 180.153.105.147, 180.153.105.159, 180.153.105.162, 180.153.105.173, 180.153.105.195, 180.153.93.22, 180.153.93.33
	zip.z.qq.com	61.151.168.204
                                4365 found | 0 remaining | 151347 scanned in 485.14 seconds
	4365 subnames found in total
	[*] Results are saved to threes files starts with ['qq.com']
	[*] Program running 485.2 seconds 

## Sample
![image](https://raw.githubusercontent.com/korsanye/findSubDomains/master/baidu.png)
