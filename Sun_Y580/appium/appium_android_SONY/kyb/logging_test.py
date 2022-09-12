import logging

# logging.basicConfig(filename='runlog.long',level=logging.DEBUG)
logging.basicConfig(filename='runlog.long', level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

logging.debug('debug info')
logging.info('helle,info')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')
