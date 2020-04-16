#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @2017.09.23
        program description : subDomainsBrute is for finding sub domains of a target domain
        a very simple way turns to be brute force, simple and effective

        ~ and the idea is simple too, find the target sub domains using dictionary (important)
        ~ using the found sub domains for further brute force
    @2019.5.13
        For python 3 only
    @2019.7.27
        For better presentation
"""

import warnings
warnings.simplefilter("ignore", category=UserWarning)
import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
from gevent.queue import PriorityQueue
import sys
import dns.resolver
import time
import optparse
import os
from multiprocessing import cpu_count


class SubNameBrute:
    """
        receive commandline args and do some initialization work
    """
    def __init__(self, target, options):
        self.start_time = time.time()
        self.target = target.strip()
        self.options = options
        self.scan_count = self.found_count = 0
        self.console_width = os.get_terminal_size()[0] - 2

        # create dns resolver pool ~ workers
        self.resolvers = [dns.resolver.Resolver(configure=False) for _ in range(options.threads)]
        for resolver in self.resolvers:
            resolver.lifetime = resolver.timeout = 10.0

        self.print_count = 0
        self.STOP_ME = False

        # load dns servers and check whether these dns servers works fine ?
        self._load_dns_servers()

        # load sub names
        self.subs = []                          # subs in file
        self.goodsubs = []                      # checks ok for further exploitation
        self._load_subname('dict/subnames.txt', self.subs)

        # load sub.sub names
        self.subsubs = []
        self._load_subname('dict/next_sub.txt', self.subsubs)

        # results will save to target.txt
        
        global path
        
        path = os.path.join("results", target)
        if not os.path.exists(path):
            os.makedirs(path)
        
        self.outfile = open('%s/%s.txt' % (path, target), 'w')

        self.ip_dict = set()                            #
        self.found_sub = set()

        # task queue
        self.queue = PriorityQueue()
        for sub in self.subs:
            self.queue.put(sub)

    """
        Load DNS Servers(ip saved in file), and check whether the DNS servers works fine
    """
    def _load_dns_servers(self):
        print('[*] Validate DNS servers ...')
        self.dns_servers = []

        # create a process pool for checking DNS servers, the number is your processors(cores) * 2, just change it!
        processors = cpu_count() * 2
        pool = Pool(processors)

        # read dns ips and check one by one
        for server in open('dict/dns_servers.txt').readlines():
            server = server.strip()
            if server:
                pool.apply_async(self._test_server, (server, ))

        pool.join()                                     # waiting for process finish
        self.dns_count = len(self.dns_servers)

        sys.stdout.write('\n')
        dns_info = '[+] Found {} available DNS Servers in total'.format(self.dns_count)
        print(dns_info)

        if self.dns_count == 0:
            print('[ERROR] No DNS Servers available.')
            sys.exit(-1)

    """
        test these dns servers whether works fine
    """
    def _test_server(self, server):

        # create a dns resolver and set timeout
        resolver = dns.resolver.Resolver()
        resolver.lifetime = resolver.timeout = 10.0

        try:
            resolver.nameservers = [server]

            answers = resolver.query('public-dns-a.baidu.com')
            if answers[0].address != '180.76.76.76':
                raise Exception('incorrect DNS response')
            self.dns_servers.append(server)
        except:
            self._print_msg('[-] Check DNS Server %s <Fail>   Found %s' % (server.ljust(16), len(self.dns_servers)))

        self._print_msg('[+] Check DNS Server %s < OK >   Found %s' % (server.ljust(16), len(self.dns_servers)))

    """
        load sub names in dict/*.txt, one function would be enough
        file for read, subname_list for saving sub names
    """
    def _load_subname(self, file, subname_list):
        self._print_msg('[*] Load sub names ...')

        with open(file) as f:
            for line in f:
                sub = line.strip()
                if sub and sub not in subname_list:
                    tmp_set = {sub}

                    """
                        in case of the sub names which contains the following expression
                        and replace them {alphnum}, {alpha}, {num} with character and num
                    """
                    while len(tmp_set) > 0:
                        item = tmp_set.pop()
                        if item.find('{alphnum}') >= 0:
                            for _letter in 'abcdefghijklmnopqrstuvwxyz0123456789':
                                tmp_set.add(item.replace('{alphnum}', _letter, 1))
                        elif item.find('{alpha}') >= 0:
                            for _letter in 'abcdefghijklmnopqrstuvwxyz':
                                tmp_set.add(item.replace('{alpha}', _letter, 1))
                        elif item.find('{num}') >= 0:
                            for _letter in '0123456789':
                                tmp_set.add(item.replace('{num}', _letter, 1))
                        elif item not in subname_list:
                            subname_list.append(item)

    """
        for better presentation of brute force results, not really matters ...
    """
    def _print_msg(self, _msg=None, _found_msg=False):
        if _msg is None:
            self.print_count += 1
            if self.print_count < 100:
                return
            self.print_count = 0
            msg = '%s Found| %s Groups| %s scanned in %.1f seconds' % (
                self.found_count, self.queue.qsize(), self.scan_count, time.time() - self.start_time)
            sys.stdout.write('\r' + ' ' * (self.console_width - len(msg)) + msg)
        elif _msg.startswith('[+] Check DNS Server'):
            sys.stdout.write('\r' + _msg + ' ' * (self.console_width - len(_msg)))
        else:
            sys.stdout.write('\r' + _msg + ' ' * (self.console_width - len(_msg)) + '\n')
            if _found_msg:
                msg = '%s Found| %s Groups| %s scanned in %.1f seconds' % (
                    self.found_count, self.queue.qsize(), self.scan_count, time.time() - self.start_time)
                sys.stdout.write('\r' + ' ' * (self.console_width - len(msg)) + msg)
        sys.stdout.flush()

    def _print_domain(self, msg):
        console_width = os.get_terminal_size()[0]
        msg = '\r' + msg + ' ' * (console_width - len(msg))
        # msg = '\033[0;31;47m%s{}\033[0m'.format(msg)
        sys.stdout.write(msg)


    def _print_progress(self):
        """
            显示扫描进度,显示更美观
        """
        msg = '\033[0;31;47m%s\033[0m found | %s remaining | %s scanned in %.2f seconds' % \
              (self.found_count, self.queue.qsize(), self.scan_count, time.time()- self.start_time)

        console_width = os.get_terminal_size()[0]
        out = '\r' + ' ' * int((console_width - len(msg)) / 2) + msg
        sys.stdout.write(out)

    """
        important : assign task to resolvers
    """
    def _scan(self, j):
        self.resolvers[j].nameservers = [self.dns_servers[j % self.dns_count]]
        while not self.queue.empty():
            sub = self.queue.get(timeout=1.0)
            self.scan_count += 1

            try:
                cur_sub_domain = sub + '.' + self.target
                answers = self.resolvers[j].query(cur_sub_domain)
            except:
                continue

            if answers:
                ips = ', '.join(sorted([answer.address for answer in answers]))

                # exclude : intranet or kept addresses
                if ips in ['1.1.1.1', '127.0.0.1', '0.0.0.0', '0.0.0.1']:
                    continue
                if SubNameBrute.is_intranet(answers[0].address):
                    continue

                self.found_sub.add(cur_sub_domain)
                for answer in answers:
                    self.ip_dict.add(answer.address)

                if sub not in self.goodsubs:
                    self.goodsubs.append(sub)

                self.found_count += 1
                ip_info = '{} \t {}'.format(cur_sub_domain, ips)
                # print(ip_info)
                self.outfile.write(cur_sub_domain + '\t' + ips + '\n')
                self._print_domain(ip_info)
                sys.stdout.flush()
                self._print_progress()
                sys.stdout.flush()

    @staticmethod
    def is_intranet(ip):
        ret = ip.split('.')
        if len(ret) != 4:
            return True
        if ret[0] == '10':
            return True
        if ret[0] == '172' and 16 <= int(ret[1]) <= 32:
            return True
        if ret[0] == '192' and ret[1] == '168':
            return True
        return False

    """
        assign task to threads ...
    """
    def run(self):
        threads = [gevent.spawn(self._scan, i) for i in range(self.options.threads)]

        print('[*] Initializing %d threads' % self.options.threads)

        try:
            gevent.joinall(threads)
        except KeyboardInterrupt as e:
            msg = '[WARNING] User aborted.'
            sys.stdout.write('\r' + msg + ' ' * (self.console_width - len(msg)) + '\n\r')
            sys.stdout.flush()


def wildcard_test(dns_servers, domain, level=1):
    try:
        r = dns.resolver.Resolver(configure=False)
        r.nameservers = dns_servers
        answers = r.query('lijiejie-not-existed-test.%s' % domain)
        ips = ', '.join(sorted([answer.address for answer in answers]))
        if level == 1:
            print('any-sub.%s\t%s' % (domain.ljust(30), ips))
            wildcard_test(dns_servers, 'any-sub.%s' % domain, 2)
        elif level == 2:
            exit(0)
    except Exception as e:
        return domain


if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog [options] target.com', version="%prog 2.0")
    parser.add_option('-f', dest='file', default='subnames.txt',
                      help='Dictionary file, default is subnames.txt.')
    parser.add_option('--full', dest='full_scan', default=False, action='store_true',
                      help='To carry out full bruteforce, subnames_full.txt will be used as dictionary file')
    parser.add_option('-t', '--threads', dest='threads', default=100, type=int,
                      help='Num of scan threads, 100 by default')

    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)

    # initialization ...
    d = SubNameBrute(target=args[0], options=options)
    wildcard_test(d.dns_servers, args[0])

    print('[*] Exploiting level-one sub domains of ', args[0])
    print('[+] There are %d subs waiting for trying ...' % len(d.queue))
    print('--------------------------------------')
    d.run()
    print('--------------------------------------')
    print('%d subnames found' % len(d.found_sub))
    print('[*] Program running %.1f seconds ' % (time.time() - d.start_time))

    print('Exploiting level-two sub domains ... ')
    time.sleep(1)

    d.queue = PriorityQueue()
    for subsub in d.subsubs:
        for sub in d.goodsubs:
            subname = subsub + '.' + sub
            d.queue.put(subname)

    print('There are %d subs waiting for trying ...' % len(d.queue))
    d.run()
    print()
    sys.stdout.flush()
    print('%d subnames found in total' % len(d.found_sub))
    print('[*] Results are saved to threes files starts with %s' % args)

    """
        save ips and domains to files
    """
    
    ipFileName = args[0] + '-ip.txt'
    subDomainsFileName = args[0] + '-subdomain.txt'    
    
    with open(os.path.join(path, ipFileName), 'w') as f:
        for ip in d.ip_dict:
            f.write(ip + '\n')

    with open(os.path.join(path, subDomainsFileName), 'w') as f:
        for domain in d.found_sub:
            f.write(domain + '\n')

    print('[*] Program running %.1f seconds ' % (time.time() - d.start_time))

    d.outfile.flush()
    d.outfile.close()
