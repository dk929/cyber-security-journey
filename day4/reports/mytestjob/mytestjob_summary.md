# Automated Scan Summary

**Scan args:** /usr/lib/nmap/nmap --privileged -sS -sV -O --script=banner,vuln -p- -T4 -oX /home/templemaster/cyber-security/reports/mytestjob/mytestjob.xml 192.168.127.130

## Host 1: 192.168.127.130, 00:0C:29:4F:C1:DC

|Severity|Port|Service|State|Notes|
|---|---:|---|---|---|

|High|21|ftp|open|ftp-vsftpd-backdoor: 
  VULNERABLE:
  vsFTPd version 2.3.4 backdoor
    State: VULNERABLE (Exploitable)
    IDs:  BID:48539  CVE:CVE-2011-2523
      vsFTPd version 2.3.4 backdoor, this was reported on 2011-07-04.
    Disc | banner: 220 (vsFTPd 2.3.4)|

|High|23|telnet|open|banner: \xFF\xFD\x18\xFF\xFD \xFF\xFD#\xFF\xFD'|

|High|25|smtp|open|banner: 220 metasploitable.localdomain ESMTP Postfix (Ubuntu) | smtp-vuln-cve2010-4344: 
  The SMTP server is not Exim: NOT VULNERABLE
 | sslv2-drown: 
  ciphers: 
    SSL2_RC4_128_WITH_MD5
    SSL2_RC2_128_CBC_WITH_MD5
    SSL2_RC4_128_EXPORT40_WITH_MD5
    SSL2_DES_64_CBC_WITH_MD5
    SSL2_DES_192_EDE3_CBC_WITH_MD5
    SSL2_RC2_128_CBC_EXPORT40_WI|

|High|111|rpcbind|open|rpcinfo: 
  program version    port/proto  service
  100000  2            111/tcp   rpcbind
  100000  2            111/udp   rpcbind
  100003  2,3,4       2049/tcp   nfs
  100003  2,3,4       2049/udp   nfs
  |

|High|445|netbios-ssn|open||

|High|2121|ftp|open|banner: 220 ProFTPD 1.3.1 Server (Debian) [::ffff:192.168.127.130]|

|Medium|22|ssh|open|banner: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1|

|Medium|80|http|open|http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug) | http-slowloris-check: 
  VULNERABLE:
  Slowloris DOS attack
    State: LIKELY VULNERABLE
    IDs:  CVE:CVE-2007-6750
      Slowloris tries to keep many connections to the target web server open and hold
      them open as  | http-dombased-xss: Couldn't find any DOM based XSS. | http-csrf: 
Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.127.130
  Found the following possible CSRF vulnerabilities: 
    
    Path: http://192.168.127.130:80/dvwa/
    Form id: 
    Fo | http-trace: TRACE is enabled | http-server-header: Apache/2.2.8 (Ubuntu) DAV/2 | http-fileupload-exploiter: 
  
    Couldn't find a file-type field. | http-stored-xss: Couldn't find any stored XSS vulnerabilities. | http-enum: 
  /tikiwiki/: Tikiwiki
  /test/: Test page
  /phpinfo.php: Possible information file
  /phpMyAdmin/: phpMyAdmin
  /doc/: Potentially interesting directory w/ listing on 'apache/2.2.8 (ubuntu) dav/2'
 | http-sql-injection: 
  Possible sqli for queries:
    http://192.168.127.130:80/dav/?C=N%3BO%3DD%27%20OR%20sqlspider
    http://192.168.127.130:80/dav/?C=M%3BO%3DA%27%20OR%20sqlspider
    http://192.168.127.130:80/dav/?C|

|Medium|3306|mysql|open|banner: >\x00\x00\x00\x0A5.0.51a-3ubuntu5\x00`\x02\x00\x00!0n[^F$}\x00,
\xAA\x08\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00...
|

|Medium|5432|postgresql|open|ssl-ccs-injection: 
  VULNERABLE:
  SSL/TLS MITM vulnerability (CCS Injection)
    State: VULNERABLE
    Risk factor: High
      OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h
      does not proper | ssl-dh-params: 
  VULNERABLE:
  Diffie-Hellman Key Exchange Insufficient Group Strength
    State: VULNERABLE
      Transport Layer Security (TLS) services that use Diffie-Hellman groups
      of insufficient streng | ssl-poodle: 
  VULNERABLE:
  SSL POODLE information leak
    State: VULNERABLE
    IDs:  BID:70574  CVE:CVE-2014-3566
          The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
          products|

|Medium|8180|http|open|http-slowloris-check: 
  VULNERABLE:
  Slowloris DOS attack
    State: LIKELY VULNERABLE
    IDs:  CVE:CVE-2007-6750
      Slowloris tries to keep many connections to the target web server open and hold
      them open as  | http-dombased-xss: Couldn't find any DOM based XSS. | http-cookie-flags: 
  /admin/: 
    JSESSIONID: 
      httponly flag not set
  /admin/index.html: 
    JSESSIONID: 
      httponly flag not set
  /admin/login.html: 
    JSESSIONID: 
      httponly flag not set
  /admin | http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug) | http-enum: 
  /admin/: Possible admin folder
  /admin/index.html: Possible admin folder
  /admin/login.html: Possible admin folder
  /admin/admin.html: Possible admin folder
  /admin/account.html: Possible admin | http-csrf: 
Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.127.130
  Found the following possible CSRF vulnerabilities: 
    
    Path: http://192.168.127.130:8180/admin/
    Form id: user | http-stored-xss: Couldn't find any stored XSS vulnerabilities.|

|Low|53|domain|open||

|Low|139|netbios-ssn|open||

|Low|512|exec|open|banner: \x01Where are you?|

|Low|513|login|open||

|Low|514|shell|open|banner: \x01getnameinfo: Temporary failure in name resolution|

|Low|1099|java-rmi|open|rmi-vuln-classloader: 
  VULNERABLE:
  RMI registry default configuration remote code execution vulnerability
    State: VULNERABLE
      Default configuration of RMI registry allows loading classes from remote URLs which |

|Low|1524|bindshell|open|banner: root@metasploitable:/#|

|Low|2049|nfs|open||

|Low|3632|distccd|open|distcc-cve2004-2687: 
  VULNERABLE:
  distcc Daemon Command Execution
    State: VULNERABLE (Exploitable)
    IDs:  CVE:CVE-2004-2687
    Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
      Allows exe|

|Low|5900|vnc|open|banner: RFB 003.003|

|Low|6000|X11|open||

|Low|6667|irc|open|banner: :irc.Metasploitable.LAN NOTICE AUTH :*** Looking up your hostna
me...|

|Low|6697|irc|open|banner: :irc.Metasploitable.LAN NOTICE AUTH :*** Looking up your hostna
me... | irc-unrealircd-backdoor: Looks like trojaned version of unrealircd. See http://seclists.org/fulldisclosure/2010/Jun/277 | ssl-ccs-injection: No reply from server (TIMEOUT) | irc-botnet-channels: 
  ERROR: Closing Link: [192.168.127.129] (Ping timeout)
|

|Low|8009|ajp13|open||

|Low|8787|drb|open||

|Low|41265|nlockmgr|open||

|Low|43614|status|open||

|Low|55951|mountd|open||

|Low|57277|java-rmi|open|rmi-vuln-classloader: 
  VULNERABLE:
  RMI registry default configuration remote code execution vulnerability
    State: VULNERABLE
      Default configuration of RMI registry allows loading classes from remote URLs which |


