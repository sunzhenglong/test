# 远程操作linux系统
# 需要的模块：paramiko
import paramiko
#连接Linux系统:
#第一个：建立连接,创造一个SSHClien对象
#第一步
s = paramiko.SSHClient()
#第二步,信任Linux的主机
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#第三步，使用connect()连接远程linux主机
s.connect(
    hostname="192.168.10.45",
    port=22,
    username="root",
    password="123456",
)
#第二个：执行命令
stdin,stdout,stderr  = s.exec_command("ls -al")
#括号里边写的需要执行的命令 (stdin,stdout,stderr)是变量 std-in,out,err
print(stdout.read().decode())      #  decode(解码)---encode(编码)

#第三个：文件上传，下载
#SFTPClient(参数):sftp客户端方法,参数指的是之前建立的连接
#第二种连接方式：使用端口号连接
#端口号连接Linux系统，括号内包含IP地址，端口号的元组
t = paramiko.Transport(('192.168.10.45',22))
t.connect(username="root",password="123456")

#sftp客户端方法，括号内指的是一个套字节
sftp = paramiko.SFTPClient.from_transport(t)
x1 = '/etc/cc.txt'          #找到目标linux 远程文件
x2 = 'E:\Python\ccc.txt'    #保存到本地的位置
sftp.get(x1,x2)             #下载文件,（括号写远程文件，本地文件）

sftp.put(x2,x1)             #上传文件
t.close()#关闭连接，断开连接
s.close()