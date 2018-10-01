import paramiko
from exceptions AuthenticationException,SSHException, BadHostKeyException
def ssh_execution(cmd):

    try:
        sys_ip = REMOTE_IP
        username = 'root'
        ssh_key = '/.ssh/id_rsa'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(sys_ip, username=username, key_filename=ssh_key) # Install ssh on host/client and create id_rsa files
    except paramiko.AuthenticationException as AuthenticationException: # Cutome exceptions
        return AuthenticationException
    except paramiko.SSHException as sshException:
        return sshException
    except paramiko.BadHostKeyException as badHostKeyException:
        return badHostKeyException
    try:
      stdin, stdout, stderr = ssh.exec_command(cmd)
      ret = ''.join(stdout.readlines())
      ssh.close()
    except paramiko.ProxyCommandFailure as ProxyCommandFailure:
      return ProxyCommandFailure
    return ret
