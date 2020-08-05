from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname = 'vip.xiaomiqiu.com'
    username = 'admin'
    password = 'ygwl@fh027'
    s.login(hostname, username, password, port=37417, auto_prompt_reset=False, login_timeout=5)
    fout = open('/mnt/d/Documents/a.txt', 'wb+')
    s.logfile = fout
    s.sendline('sho cloc')   # run a command
    s.prompt()             # match the prompt
    s.sendline('sho vers')   # run a command
    while True:
        s.sendline()
        if s.prompt():
            s.sendline("sho ip interface")
        else:
            break
    s.prompt()
    # print(s.before)             # match the prompt
    # print(s.before)        # print everything before the prompt.
    s.sendline('ls')
    s.prompt()
    # print(s.before)
    s.sendline('sho devi')
    s.prompt()
    # print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
