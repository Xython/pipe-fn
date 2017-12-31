import pipe_fn
from pattern_matching import Match, _



def length(self):
    return len(self)


serverTime = 20
endTime = 100
users = ['a', 'b', 'c', 'd', 'e', '7']
joinedGroup  = '1'
configure = dict(serverTime=serverTime,
                endTime=endTime,
                users=users,
                joinedGroup=joinedGroup)


# def logistic(conf):
#     with Match(conf) as m:
#         for () in m.case({
#                 'serverTime ':_ > endTime,
#                 }):
#             return 0
#         for () in m.case({
#                 'users': _
#                      .when(lambda x: length(x) == 5)
#                 }):
#             return 1
#         for () in m.case({
#                 'joinedGroup': _ == '0'
#                 }):
#             return 2
#         else:
#             return 3
#
# logistic(configure) | pipe_fn.e/print


