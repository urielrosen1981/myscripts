import paramiko

hosts = ['192.168.64.2','192.168.64.55']
cmd = "ls -ltr /etc"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in hosts:

    #try:    
        ssh.connect(i, username='uriel', password='uriel1981')
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.readlines()
        print(out)
        resp=''.join(out)
        print(resp) 
        ssh.close()
    #except socket.error as e:
     #   pass