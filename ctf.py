import urllib
import base64

def base64_encode(s):
    return base64.b64encode(s)
    
def base64_decode(s):
    return base64.b64decode(s)



def percent_encode(s):
    return urllib.quote(s)

def percent_decode(s):
    return urllib.unquote(s)



def split_by(string, by=1):
    '''chop the string into n character chunks'''
    return [string[i:i+by] for i in range(0,len(string), by)]


def str2hex(s,sep=''):
    return sep.join(['{:02x}'.format(ord(i)) for i in s])
  

def hex2str(h,sep=''):
    if sep!='':
        res = ''.join([chr(int(i,16)) for i in h.split(sep)])
    else:
        res = ''.join([chr(int(h[i:i+2],16)) for i in range(0,len(h),2)])
    return res
 

def byte2hex(s,sep=''):
    return sep.join(['{:02x}'.format(i) for i in s])


def hexdump(inputs, stride=4, cols=6, sep=' '):
    if isinstance(inputs, bytes):
        hexstr = byte2hex(inputs)
    elif isinstance(inputs, str):
        hexstr = str2hex(inputs)

    hexstr = split_by(hexstr, stride*cols*2)
    hexstr = [sep.join(split_by(row, stride*2)) for row in hexstr]
    hexstr = '\n'.join(hexstr)
    return hexstr