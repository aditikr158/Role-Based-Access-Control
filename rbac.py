from classes import User, Role, Resource, ActionType
from first import First
import sys
def view_user_roles(user):
    print("View User Roles")
    user_roles = user.get_user_role_desc()
    print("USER ROLES - ", user_roles)

def access_resources(user):
    print("Access Resources")
    print(list(Resource.resource_dict.keys()))
    resource_name = input("Enter Resource you wish to access : ")
    if resource_name in Resource.resource_dict:
        resource = Resource.resource_dict[resource_name]['object']
        roles_assigned = user.get_user_role()
        for roles in roles_assigned:
            user_resource = roles.resource
            if resource.name in list(map(lambda x:x.name, user_resource)):
                for action in ActionType:
                    print(action.name)
                user_action = input("Enter Action you wish to perform : ")
                if user_action in resource.action:
                    print("ACCESS GRANTED")
                    return
        print("ACCESS DENIED")
    else:
        print("NO SUCH RESOURCE PRESENT")

def login_as_user(user_name):
    user = check_user(user_name)
    if user is None:
        print("USER DOES NOT EXISTS")
        return
    role_list = user.get_user_role()
    if "Admin" in list(map(lambda x: x.name, role_list)):
        print("You can't login as Admin")
        print("Choose another user")
        return
    while True:
        print("Hi! You are logged in as User " + user_name)
        print("Press 1 to login as another User")
        print("Press 2 to view roles")
        print("Press 3 to access resource")
        print("Press 4 to exit from user login")
        try:
            option = int(input("Choose Option : "))
        except:
            print("Enter Valid option")
            continue

        if option == 1:
            print()
            user_name = input("Enter another user name : ")
            login_as_user(user_name)
        elif option == 2:
            view_user_roles(user)
        elif option == 3:
            access_resources(user)
        elif option == 4:
            print("EXIT USER LOGIN")
            print("Signing in as Admin")
            main()
        else:
            print("Choose correct option")

def check_user(user_name):
    if user_name in User.user_dict:
        user = User.user_dict[user_name]
        return user
    return None

def create_new_user():
    print("Creating new User by Admin")
    user_name = input("Enter Name for the User : ")
    user = check_user(user_name)
    if user:
        print("User already exists")
    else:
        user = User()
        user.create_user(user_name)
        user.display_user()

def assign_role_user(user_name):
    print("Assigning new Role to User")
    user = check_user(user_name)
    if user:
        present_roles = user.get_user_role_desc()
        print("present roles with the user : ", present_roles)
        print("")
        print("Roles to choose from - ", list(Role.role_dict.keys()))
        role_input = input("Enter the role name you want to assign : ")
        if role_input == "Admin":
            print("CAN'T ASSIGN ADMIN ROLE TO ANOTHER USER")
            return
        present_roles = user.get_user_role()
        assign_role = Role.role_dict[role_input]['object']
        if assign_role in present_roles:
            print("Role already assigned to User")
        else:
            user.assign_role(assign_role)
            print("ROLE ASSIGNED TO USER")
    else:
        print("USER DOES NOT EXISTS")

def remove_role_user(user_name):
    print("Removing Role from User")
    user = check_user(user_name)
    if user:
        present_roles = user.get_user_role_desc()
        print("present roles with the user : ", present_roles)
        print("")
        present_roles = user.get_user_role()
        role_input = input("Enter the role name you want to remove : ")
        remove_role = Role.role_dict[role_input]['object']
        if remove_role in present_roles:
            user.remove_role(remove_role)
            print("ROLE REMOVED")
        else:
            print("ROLE NOT ASSIGNED TO USER")
    else:
        print("USER DOES NOT EXISTS")

def main():
    first = First()
    while True:
        print("Hi! You are logged in as Admin")
        print("Press 1 to login as another User")
        print("Press 2 to create an user")
        print("Press 3 to assign role to a user")
        print("Press 4 to remove role from a user")
        print("Press 5 to exit System")
        try:
            option = int(input("Choose Option : "))
        except:
            print("Enter Valid option")
            continue
        if option == 1:
            print("")
            user_name = input("Enter another user name : ")
            login_as_user(user_name)
        elif option == 2:
            create_new_user()
        elif option == 3:
            print("")
            user_name = input("Enter user Name : ")
            assign_role_user(user_name)
        elif option == 4:
            print()
            user_name = input("Enter user Name : ")
            remove_role_user(user_name)
        elif option == 5:
            print("Exit System")
            sys.exit()
        else:
            print("Choose correct option")

if __name__ == '__main__':
    main()