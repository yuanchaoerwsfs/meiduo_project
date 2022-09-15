from pymysql import install_as_MySQLdb
install_as_MySQLdb()
# 可能出现的错误
#
# Error loading MySQLdb module: No module named 'MySQLdb'.
# 出现错误的原因：
#
# Django中操作MySQL数据库需要驱动程序MySQLdb
# 目前项目虚拟环境中没有驱动程序MySQLdb
# 解决办法：
#
# 安装PyMySQL扩展包
# 因为MySQLdb只适用于Python2.x的版本，Python3.x的版本中使用PyMySQL替代MySQLdb



