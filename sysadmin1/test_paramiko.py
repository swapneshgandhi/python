#!/usr/bin/env python
import paramiko

paramiko.util.log_to_file('paramiko.log')
s = paramiko.SSHClient()
s.load_system_host_keys()
s.connect('localhost', 22, 'testuser', 'password')
stdin, stdout, stderr = s.exec_command('ifconfig')
print stdout.read()
s.close()
