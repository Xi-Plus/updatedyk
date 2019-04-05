#!/usr/bin/env python

from sys import path, argv
from os import getpid
from os.path import join, dirname
from datetime import datetime

CODE_DIR = dirname(__file__)
path.append(CODE_DIR)

ID_STR = '[%s-%d-%s]' % (datetime.utcnow().strftime('%Y%m%d%H%M%S'),
                         getpid(), argv[1])

logf = open(join(CODE_DIR, 'exec.log'), 'a')
print(ID_STR, 'LOADING', file=logf)

import updatedyk
import traceback

try:
    if argv[1] == 'main':
        updatedyk.main(error_log=logf)
    elif argv[1] == 'maintenance':
        updatedyk.maintenance()
    else:
        raise Exception('Unknown action: %s' % argv[1])
except Exception as e:
    print('TRACEBACK', file=logf)
    print(traceback.format_exc(), file=logf)
    print(ID_STR, 'TBEND', file=logf)
else:
    print('DONE', file=logf)

logf.close()
