from pyiex_config import *


def companyName(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["companyName"]
    
    
def exchange(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["exchange"]
    
    
def description(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["description"]
    
    
def industry(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["industry"]
    
    
def website(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["website"]
    
    
def CEO(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["CEO"]
    
    
def issueType(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["issueType"]
    
    
def sector(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["sector"]
           
           
def tags(symbol):
    return requests.get(base_url + version +"/stock/" +
           symbol + "/company").json()["tags"]
