# Auto Command

This can be used to automatically run the same command over and over.  Only works for Cisco IOS.

Example:
```
Device IP address:  10.5.1.1
Username:  da2257adm
Password:  

Every X seconds, run the commands:  5

Enter/Paste your commands. Ctrl-C or Ctrl-Z to finish.
---------------------------------------------

show clock
show ip bgp sum | i ^Nei|^10\.
^Z

---------------------------------------------

Stop the loop with Ctrl-C


23:03:37.679 MST Tue Jun 23 2020
Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.200.31.189   4        65359 3586422 3520617    34928    0    0 5w6d          192
10.201.31.185   4        65090 12747896 12752852    34928    0    0 21w4d         106


23:03:46.804 MST Tue Jun 23 2020
Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.200.31.189   4        65359 3586431 3520626    34929    0    0 5w6d          10
10.201.31.185   4        65090 12747905 12752861    34928    0    0 21w4d         106


23:03:55.943 MST Tue Jun 23 2020
Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.200.31.189   4        65359 3586432 3520627    34930    0    0 5w6d          192
10.201.31.185   4        65090 12747905 12752861    34928    0    0 21w4d         106

---- CONNECTION CLOSED ----


Press ENTER to close window.
```