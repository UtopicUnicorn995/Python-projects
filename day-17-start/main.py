class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.user = username


user_1 = User('001', "Joey")
# user_1.id = "001"
# user_1.username = "Ian"
#
# print(user_1.username)'

print(user_1.user)