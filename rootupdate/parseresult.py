import os.path as path
import os
import re
import pickle

def getbuilddate(sessionid,basedir='/home/flask1/source/log/',masterfile='.allhosts'):
  alldir = {}
  log = path.join(basedir,str(sessionid))
  inv = path.join(log,masterfile)
  try:
      if not path.getsize(inv):
         return alldir
      else:
         with open(inv,'rb') as fh:
             hsarr = pickle.load(fh)
  except FileNotFoundError:
      return alldir
  unreachdir = {'unreachable':0,'hosts':[]}
  successdir = {'success':0,'hosts':[]}
  faileddir = {'failed':0,'hosts':[]}
  totaldir = {'all':0,'hosts':[]}
  pendingdir = {'pending':0,'hosts':[]}
  summarydir = {}
  totaldir['all'] = len(hsarr)
  totaldir['hosts'] = hsarr

  re_unreachable = re.compile('unreachable=1')
  re_failed = re.compile('failed=0')
  for f in os.listdir(log):
    logpath = log+'/'+f
    if (path.getsize(logpath) != 0) and (f != masterfile) :
      with open(logpath) as fi:
        line = fi.read()
        if re_unreachable.search(line):
          unreachdir['unreachable'] += 1
          unreachdir['hosts'].append(f)
        elif re_failed.search(line):
          successdir['success'] += 1
          successdir['hosts'].append(f)
        else:
          faileddir['failed'] += 1
          faileddir['hosts'].append(f)
  tpend = list(set(totaldir['hosts'])-set(unreachdir['hosts'])-set(successdir['hosts'])-set(faileddir['hosts']))
  print(tpend)
  pendingdir['pending'] = len(tpend)
  pendingdir['hosts'] = tpend
  summarydir['all'] = totaldir['all']
  summarydir['success'] = successdir['success']
  summarydir['failed'] = faileddir['failed']
  summarydir['unreachable'] = unreachdir['unreachable']
  summarydir['pending'] = pendingdir['pending']
  summarydir['percentage'] = "{:.2f}%".format(pendingdir['pending'] / totaldir['all'] * 100)
  alldir['Summary'] = summarydir
  alldir['unreachable hosts info'] = unreachdir
  alldir['success hosts info'] = successdir
  alldir['failed hosts info'] = faileddir
  alldir['All hosts info'] = totaldir
  alldir['Pending hosts info'] = pendingdir

  return alldir

print(getbuilddate(123456))

