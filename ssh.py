from pickle import LIST
from webbrowser import get
import paramiko
import subprocess
import os
import datetime
import os.path
import csv

#create file test.27.03.22 ie
cmd = "DATE=`date +%d-%m-%y` ; touch test.$DATE"
#list all machine ips
ipaddressess = "hostname --all-ip-addresses"
getslashusage = "df -h /  | awk '{print $5}' | tail -1"
getmem = "free -h | awk '{print $2}' |sed '1d; $d;'"
def gethostsfile():
   
    fileobj=open("/Users/uriel/python/ssh_hosts.txt", "r")
    it=iter(fileobj)
    lines=[]
    while True:
        try:    
            line=next(it)
            line=line.strip()
            lines.append(line)
        except StopIteration:
            break
       # print(lines)

    fileobj.close()

    return lines 



iplist = gethostsfile()
#print("iplist" , iplist)


def sshtohost():
    newiplist = []
    totalmem = []
    print("iplist" , iplist)
    for server in iplist:
        #print(iplist)
       # print("server",server)
    #try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server,22,username='debian', password='debian', timeout=600)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.readlines()
    #print(out)
        resp=''.join(out)
    #print(resp) 
        stdin, stdout, stderr = ssh.exec_command(ipaddressess)
        iplines = stdout.readlines()
        print("iplines",iplines)
        newip = ''.join(iplines)
        print("newip",newip)
        firstip = newip.split(' ')[0]
        print("firstip",firstip)
        newiplist.append(firstip)
        print("newiplist",newiplist)
        stdin, stdout, stderr = ssh.exec_command(getslashusage)
        slashuse = stdout.readlines()
        stdin, stdout, stderr = ssh.exec_command(getmem)
        rawmem = stdout.readlines()
        newmem = rawmem 
        for i in range(len(newmem)):
            newmem[i]=newmem[i].replace('\n','')
        totalmem.append(newmem)
        print("totalmem",totalmem)

        print(slashuse)
        ssh.close()
    return newiplist ,totalmem; 
    
        
hostlist = sshtohost()
#totalmem = sshtohost()
newiplistforcsv = sshtohost()
print (newiplistforcsv)
def createcsvreport(hostlist):
    print("hostlist",hostlist)

      
    with open('servers.csv', mode='w') as servers:
        print(hostlist)
        servers_writer = csv.writer(servers, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        servers_writer.writerow(hostlist)
        #servers_writer.writerow(totalmem)


def main():
    gethostsfile()
    sshtohost()
    createcsvreport(hostlist)

    #flatten_list()
if __name__ == "__main__":
    main()
    ######