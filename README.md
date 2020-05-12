# findSubDomains
A tool finding sub-domains of a target site for penetesters with python3.

Domain Collection please refer : [互联网公司子域名收集](https://github.com/starnightcyber/subDomains)

## Preface
This script is used to detect subdomains. 

Sombody made files output saved to the folder reuslts each target have a folder with its name.

## Dependencies

    python3 -m pip install -r requirements.txt

## Usage

    python3 findSubDomains.py target.com

## Example

```
python3 findSubDomains.py baidu.com
[*] Validate DNS servers ...
[+] Check DNS Server 119.29.29.29     < OK >   Found 4                                                                      
[+] Found 4 available DNS Servers in total
[*] Load sub names ...                                                                                                      
[*] Load sub names ...                                                                                                      
[*] Exploiting level-one sub domains of  baidu.com
[+] There are 15372 subs waiting for trying ...
--------------------------------------
[*] Initializing 100 threads
11.baidu.com 	 202.108.23.222, 61.135.186.230
0.baidu.com      111.206.223.136           
123.baidu.com    112.80.248.75, 112.80.248.76  
3g.baidu.com     112.80.255.162, 112.80.255.163  
01.baidu.com     153.37.235.93, 61.135.185.20     
8.baidu.com      111.206.37.81, 112.80.255.131, 61.135.186.244   
a.baidu.com      112.80.248.124, 123.125.114.38             
ab.baidu.com     61.135.185.81, 61.135.185.90 
abc.baidu.com    112.80.248.75, 112.80.248.76  
ac.baidu.com     112.80.248.234, 202.108.23.221    
act.baidu.com    112.80.255.85, 163.177.151.90, 202.106.2.65    
ad.baidu.com     182.61.62.50                 
```
