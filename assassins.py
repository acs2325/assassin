from random import shuffle
import email.mime.multipart
import email.mime.text
import smtplib

 
smtp_host = "cernmx.cern.ch"
smtp_port = 25

def compose_mail(origin, destination, subject, message):
    """Creates and returns an email object from the requested parameters."""
    msg = email.mime.multipart.MIMEMultipart()  # create a message
    msg['From'] = origin  # setup the parameters of the message
    msg['To'] = destination
    msg['Subject'] = subject
    msg.attach(email.mime.text.MIMEText(message, 'plain'))  # add in the message body
    return msg


sender_email = "*******@cern.ch"  # Enter your address
receiver_email = "*********@gmail.com" # Enter receiver address
m = "This message is sent with Python."
s = "Your assassin target"

msg = compose_mail(sender_email, receiver_email, s, m)
s = smtplib.SMTP(host=smtp_host, port=smtp_port)  # Setting up SMTP server
s.starttls()
# s.login(MY_ADDRESS, PASSWORD)
s.send_message(msg)  # send the message via the server
s.quit()

def loadPlayers():
    players = []
    emails = []
    
    file1 = open('players.txt', 'r')
    while True:
        line = file1.readline()
        #print(line)
        if not line: break
        (player,email) = line.split()
        players.append(player)
        emails.append(email)
    
    return (players,emails)

def main():
    players,emails = loadPlayers()
    mail_dict = {}
    for i,player in enumerate(players):
        mail_dict[player] = emails[i]

    shuffle(players)
    
    targets = players[:]
    total = len(players)

    
    for i in range(total):
        print(mail_dict[players[i]] + ": your target is " + targets[(i+1) % total] + ".\n")
           
main()
