#!/usr/bin/python
#server program to execute the programs sent form client
import sys,socket, re, hashlib, commands

# a function to convert the password to hash for comparison
def getHashPass(password):
    return hashlib.sha256(password).hexdigest()

# function to setup the server
def Server_Start(port):
 s = socket.socket()         # Create a socket object
 host = socket.gethostname() # Get local machine name
 s.bind((host, port))        # Bind to the port
 return s

def main():
  server_port=2000           #server port set to 2000
  user_pass_hash={}          #define hash table which <username,password> as a key value pair
  user_program_hash={}       #define hash table which <username,list of programs the user can excecute> as a key value pair

  if(len(sys.argv)) < 2:     #error check the arguments
    print 'Too few arguments'
    print 'Usage: ',sys.argv[0],' config-file'
    exit(1)

  try:
   file = open(sys.argv[1], 'rU')
   for line in file:   ## iterates over the lines of the file
    match=re.findall(r'[\S]+',line)   # regular expression which splits username, password and program names assumed to be of type
                                      # <username> <password> <prog1,prog2,prog3>
    if match:
       user_pass_hash[match[0]]=getHashPass(match[1])        #make entry to password hash table
       user_program_hash[match[0]]=match[2].split(",")       #make entry to programs hash table
   file.close
  except IOError as e:
    print "Unable to open file"
    print "exiting..."
    exit(1)

  s=Server_Start(server_port)          #start the server
  print "Server running on port 2000"

  s.listen(5)                         #listen to requests
  while True:
    c, addr = s.accept()              # Establish connection with client.
    print 'Got connection from', addr
    clinet_data=c.recv(1024)          # receive form client      
    extract_client_data=re.findall(r'[\S]+',clinet_data)      #apply regular expreression to client data.

								#check if user is valid and if password is valid
    if extract_client_data[0] in user_pass_hash and user_pass_hash[extract_client_data[0]]==extract_client_data[1]:     

								#check if user has permission to excecute
       if extract_client_data[0] in user_program_hash and extract_client_data[2] in user_program_hash[extract_client_data[0]]:
														
          program_to_exec=extract_client_data[2]
          (status,output)=commands.getstatusoutput(program_to_exec)		#excecute the program and check status
    
          if status:
           print "Error occured in excecuting the program",extract_client_data[2]
           sys.stderr.write(output)
          else:
           print "The program ",extract_client_data[2]," excecuted correctly"
           print output 					#display the output of the program 				
       else:
         print "Error:The user ",extract_client_data[0]," does not have required permission."  

    else:print "Error:can't authenticate the user ",extract_client_data[0]
    c.close()
     
if __name__ == '__main__':
    main()
