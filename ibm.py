import os
import re
import sys


import pexpect


def telnet_login(server, user, passwd, shell_prompt="# |->"):
    """
    @summary: This logs the user into the given server.
    It uses the 'shell_prompt' to try to find the prompt right after login.
    When it finds the prompt it immediately tries to reset the prompt to '#UNIQUEPROMPT#'
    more easily matched.
    @return: If Login successfully ,It will return a pexpect object
    @raise exception: RuntimeError will be raised when the cmd telnet failed or the user
    and passwd do not match
    @attention:1. shell_prompt should not include '$',on some server, after sendline
                  (passwd)   the pexpect object will read a '$'.
    2.sometimes the server's output before its shell prompt will contain '#' or
     '->'  So the caller should kindly assign the shell prompt
    """
    if not server or not user or not passwd or not shell_prompt:
        raise RuntimeError('You entered empty parameter for telnet_login')
    child = pexpect.spawn('telnet %s' % server)
    child.logfile_read = sys.stdout
    index = child.expect(['(?i)login:', '(?i)username', '(?i)Unknown host'])
    if index == 2:
        raise RuntimeError('unknown machine_name' + server)
    child.sendline(user)
    child.expect('(?i)password:')
    child.logfile_read = None  # To turn off log
    child.sendline(passwd)

    while True:
        index = child.expect([pexpect.TIMEOUT, shell_prompt])
        child.logfile_read = sys.stdout
        if index == 0:
            if re.search('an invalid login', child.before):
                raise RuntimeError(
                    'You entered an invalid login name or password.')
        elif index == 1:
            break
    child.logfile_read = sys.stdout  # To tun on log again
    child.sendline("PS1=# UNIQUEPROMPT#")
    # This is very crucial to wait for PS1 has been modified successfully
    # child.expect(“#UNIQUEPROMPT#”)
    child.expect("%s.+%s" % ("#UNIQUEPROMPT#" "#UNIQUEPROMPT#"))
    return child
