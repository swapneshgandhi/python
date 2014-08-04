#!/usr/bin/python
#client connects to the server and sends the program to excecute
import sys,argparse, socket, hashlib

# a function to convert the password to hash for comparison
def getHashPass(password):
    return hashlib.sha256(password).hexdigest()

def main(argv):
# parse the arguments using arugumnet parser module.
 parser = argparse.ArgumentParser(description='Client prog parser',prefix_chars='--')
 parser.add_argument("--server",'-s',help="Enter the Server here")
 parser.add_argument("--user",'-u', help="Enter username here",required=True)
 parser.add_argument("--password",'-p', help="Enter the Server here",required=True)
 parser.add_argument("--exc",'-e', help="Enter program to excecute", required=True)
 args = parser.parse_args()
 print(args.server)

 Hashed_passwd=getHashPass(args.password)

#try connecting to the server
 try:
  s = socket.socket()         # Create a socket object
  host = socket.gethostname() # Get local machine name
  port = 2000                 # Reserve a port for your service.

  s.connect((host, port))
  send_str=args.user+" " + Hashed_passwd +" " + args.exc  #send the request to the server to excecute the program
							  #the request is of type <username> <password> <prog-to-excecute>
  s.send(send_str)
  s.close                     # Close the socket when done
 except Exception,e:
  print e
  print "exiting..."
  exit(1)

if __name__ == '__main__':
    main(sys.argv)

