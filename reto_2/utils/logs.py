WARNING_TYPE = 'WARNING'
ERROR_TYPE = 'ERROR'
LOG_TYPE = 'LOG'

# TODO: All some colors
def log(ltype: str, msg: any):
  print('-- [{}] {} --'.format(ltype, msg))

def log_info(msg: any):
  log(LOG_TYPE, msg)

def log_error(msg: str, err: Exception):
  log(ERROR_TYPE, '{}: {}'.format(msg, err))

def log_warning(msg: str, err: Exception = None):
  log(WARNING_TYPE, '{}: {}'.format(msg, err))
