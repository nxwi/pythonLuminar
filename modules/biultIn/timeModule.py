import time

# print(time.localtime())
# print((time.localtime()).tm_year)
# print((time.localtime()).tm_zone)
# print(time.asctime())
#
# for i in range(10):
#     time.sleep(1)
#     print(i+1)

print(time.strftime(
    '%A\t%a\n'
    '%B\t%b\n'
    '%D\t%d\n'
    '%Y\t\t%y\n'
    '%M\n'
    '%S\n'
    '%H\t\t\t%I\n'
    '%m'
))
