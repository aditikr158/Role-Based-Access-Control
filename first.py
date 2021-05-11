from classes import Role, User, ActionType, Resource

class First():
    role1 = Role()
    role1.create_role("Admin", {"Resource1": [1, 2, 3], "Resource2": [1, 2]})
    role2 = Role()
    role2.create_role("Customer", {"Resource1": [1], "Resource3": [1, 2]})
    role3 = Role()
    role3.create_role("Partner", {"Resource2": [1, 2]})

    user = User()
    user.create_user("Admin")
    user.assign_role(role1)
    user.display_user()

    user1 = User()
    user1.create_user("User1")
    user1.assign_role(role2)
    user1.display_user()

    user2 = User()
    user2.create_user("User2")
    user2.assign_role(role3)
    user2.display_user()