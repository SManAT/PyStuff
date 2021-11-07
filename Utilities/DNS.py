def reverse_nslookup(who):
    stdout = ""
    stderr = ""
    proc = subprocess.Popen("nslookup %s" % who,
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            bufsize=0,
                            preexec_fn=None)
    for line in iter(proc.stderr.readline, b''):
        stderr += line.decode()

    for line in iter(proc.stdout.readline, b''):
        stdout += line.decode()
    proc.communicate()
    # extract all names
    data = re.findall(r'name.=.(.*)\.', stdout)
    return data
