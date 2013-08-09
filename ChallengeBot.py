#=========================================================#
# [+] Title: Code A Bot To Take The Challenge For You     #
# [+] Author: Z3r0n3                                      #
# [+] Blog: 01day.wordpress.com                           #
# [+] Twitter: @Z3r0n301                                  #
#=========================================================#

import socket, time, os, math

def ginpong():
    while 1:
        junk=b""
        junk=bot.recv(7000)
        print(junk)
        beg=junk.find(b"PING") # Get the index of "PING"
        if beg>-1:             # If PING is captured
            junk=junk[beg:]
            if junk[5:].find(b" ")>0: # Check if there is a data sent after "PING"
                junk=junk[:(junk[5:].find(b" "))+4]+b"\r\n" # If TRUE, strip the data
                                                            # to obtain only "PING" message
            junk=junk.replace(b"PING",b"PONG") # raplace "PING" with "PONG"
            bot.send(junk) # send back the "PONG" message
            bot.send(junk) # do it more than once to make sure it's received
            bot.send(junk)
            break

def GetEm():
    bot.send(b"PRIVMSG "+enemy+b" :!ep1\r\n") # Start the challenge
    while 1:
        junk=b""
        junk=bot.recv(7000)
        print(junk)
        if junk.find(b"/")>-1: # Just to make sure if we're receiving the challenge message
            try:
                junk=junk[(junk[1:].find(b":"))+2:] # strip the message to look
                junk=junk[:junk.find(b".")]         # like number1/number2
                print(junk)
                nb1=int(junk[:junk.find(b"/")])     # get number1
                nb2=int(junk[(junk.find(b"/"))+1:]) # get number2
                answer=round(math.sqrt(nb1)*nb2,2)  # calculate the answer
                answer=bytes(str(answer).encode("ASCII")) # convert answer to bytes so it
                bot.send(b"PRIVMSG "+enemy+b" :!ep1 -rep "+answer+b"\r\n") # send answer
                print(bot.recv(7000)) # Get validation password
                bot.send(b"QUIT :By3 By3!") # End up client session
                break
            except:
                print("[!] Waiting for challenge...")
                


host="irc.root-me.org"           # Challenge's IRC server
port=6667                        # Connection port
channel=b"#Root-Me_Challenge"    # Challenge's channel
enemy=b"Candy"                   # Challenge's bot

try:
    print("[+] Creating socket")
    bot = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    print("[+] Connecting with %s:%d"%(host,port))
    bot.connect((host,port))
except:
    print("[!] Can't connect!")
else:
    print("[+] Sending nickname")
    bot.send(b"NICK Z3r0n3\r\n")
    print("[+] Sending USER command")
    bot.send(b"USER Z3r0n3 irc.root-me.org root-me :ChallengeBot")
    print("[+] Join",channel)
    bot.send(b"JOIN "+channel)
    print("[+] Playing PING PONG to impose our bot presence")
    ginpong()
    print("[+] Getting'em")
    GetEm()

print("[+] Go To Sleep")
bot.close()
