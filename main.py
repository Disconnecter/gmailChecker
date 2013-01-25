import imaplib,time,winsound, os

beeped = False
lastChekedCounter = -1

os.system("startnotify.bat")
while True:
    print("start check")
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('login@gmail.com', 'password')
    mail.select()
    unreadCount = len(mail.search(None, 'UnSeen')[1][0].split())
    if unreadCount > 0:
        print("new messages ", unreadCount)
        if lastChekedCounter != unreadCount:
            lastChekedCounter = unreadCount;
            beeped = False
        if beeped == False:
           # winsound.Beep(440, 500)
            os.system("notify.bat")
            beeped = True
    print("stop check")
    mail.logout()
    time.sleep(30)

