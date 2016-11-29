docs = []
from os import listdir, chdir
import re
import os

   
# Here's my attempt at coming up with regular expressions to filter out
# parts of the enron emails that I deem as useless.

email_pat = re.compile(".+@.+")
to_pat = re.compile("To:.+\n")
cc_pat = re.compile("cc:.+\n")
subject_pat = re.compile("Subject:.+\n")
from_pat = re.compile("From:.+\n")
sent_pat = re.compile("Sent:.+\n")
received_pat = re.compile("Received:.+\n")
ctype_pat = re.compile("Content-Type:.+\n")
reply_pat = re.compile("Reply- Organization:.+\n")
date_pat = re.compile("Date:.+\n")
xmail_pat = re.compile("X-Mailer:.+\n")
mimver_pat = re.compile("MIME-Version:.+\n")
dash_pat = re.compile("--+.+--+", re.DOTALL)
star_pat = re.compile('\*\*+.+\*\*+', re.DOTALL)
uscore_pat = re.compile(" __+.+__+", re.DOTALL)
equals_pat = re.compile("==+.+==+", re.DOTALL)
contentinfo_pat = re.compile("----------------------------------------.+----------------------------------------")
forwardedby_pat = re.compile("----------------------.+----------------------")
caution_pat = re.compile('''\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*''')
privacy_pat = re.compile(" _______________________________________________________________.+ _______________________________________________________________")

# The enron emails are in 151 directories representing each each senior management
# employee whose email account was entered into the dataset.
# The task here is to go into each folder, and enter each 
# email text file into one long nested list.
# I've used readlines() to read in the emails because read() 
# didn't seem to work with these email files.

chdir("/home/pratik/Desktop/Users")
names = [d for d in listdir(".") if "." not in d]
for name in names:
    chdir("/home/pratik/Desktop/Users/%s" % name)
    newnames=[d for d in listdir(".") if "." not in d]
    for newname in newnames:
        chdir("/home/pratik/Desktop/Users/%s/%s" %(name,newname))
        path=('/home/pratik/Desktop/NewUsers/%s/%s' %(name,newname))
        os.makedirs(path)
        file_list = listdir('.')
        for file in file_list:
            if "." in file:
                f=open(file,'r')
                temp=f.readlines()
                email=''.join(temp)
                if ".nsf" in email:
                    etype = ".nsf"
                elif ".pst" in email:
                    etype = ".pst"
                email_new = email[email.find(etype)+4:]
                email_new = to_pat.sub('', email_new)
                email_new = cc_pat.sub('', email_new)
                email_new = subject_pat.sub('', email_new)
                email_new = from_pat.sub('', email_new)
                email_new = sent_pat.sub('', email_new)
                email_new = email_pat.sub('', email_new)
                if "-----Original Message-----" in email_new:
                    email_new = email_new.replace("-----Original Message-----","")
                email_new = ctype_pat.sub('', email_new)
                email_new = reply_pat.sub('', email_new)
                email_new = date_pat.sub('', email_new)
                email_new = xmail_pat.sub('', email_new)
                email_new = mimver_pat.sub('', email_new)
                email_new = contentinfo_pat.sub('', email_new)
                email_new = forwardedby_pat.sub('', email_new)
                email_new = caution_pat.sub('', email_new)
                email_new = privacy_pat.sub('', email_new)
                outfile = open("/home/pratik/Desktop/NewUsers/%s/%s/%stxt" % (name,newname,file),'w')
                outfile.write(email_new)
                outfile.close()

        
