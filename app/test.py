from User import User

user = User()
user.new_user("new_test@test.com", "!23")

temp_data = {"2021": {"1": ["1","3","5"], "3":["1","4","14"]}}
user.save_cal(temp_data)
#user.connect_to_user(user.id)
#user.connect_to_user("62e2af67795f6fd26fae97fd")
user.checkForId()
print(user.id)
