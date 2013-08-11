#!/usr/bin/env python  
#coding=utf8 
'''
Created on Jul 15, 2013

@author: labuser
'''
import WeiboCrawl  
import WeiboSearchCrawl
import yaml

if __name__ == '__main__':  
    cfg = open("conf.yaml")
    cfg = yaml.load(cfg)
    kw = open('keywords.yaml')
    kw = yaml.load(kw)
    weiboLogin = WeiboCrawl.WeiboLogin(cfg['node']['user'], cfg['node']['pwd'], cfg['node']['cookie'])  
    if weiboLogin.login() == True:  
        print "Login Success!", cfg['node']['user'] 
        webCrawl = WeiboSearchCrawl.WebCrawl(kw, maxSearchPage=cfg['max_search_page'], 
                maxThreadNum=cfg['max_thread'], database=cfg['database'], host=cfg['host'], 
                port=cfg['port'], user=cfg['user'], pwd=cfg['pwd'], pref=cfg['pref'])  
        webCrawl.Crawl()  
        del webCrawl 
    else:
        print "Login Fail!", cfg['node']['user']