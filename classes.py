import enum

class User:
    user_count = 1
    user_dict = {}

    def create_user(self, name):
        self.id = User.user_count
        User.user_count += 1
        self.name = name
        self.role = []
        User.user_dict[name] = self

    def assign_role(self, Role):
        return self.role.append(Role)

    def remove_role(self, Role):
        return self.role.remove(Role)

    def display_user(self):
        print("Id : ", self.id, ", Name : ", self.name, ", Role: ", self.get_user_role_desc())

    def get_user_role_desc(self):
        role_name = []
        for role in self.role:
            role_name.append(role.get_role_desc())
        return role_name

    def get_user_role(self):
        return self.role


class ActionType(enum.Enum):
    READ = 1
    WRITE = 2
    DELETE = 3


class Resource:
    resource_count = 1
    resource_dict = {}

    def get_action_type(self, action_type):
        for i in range(len(action_type)):
            action_type[i] = ActionType(action_type[i]).name
        return action_type

    def display_resource(self):
        return "resource name : " + str(self.name) + ", action : " + str(self.get_action_type(self.action))

    def create_resource(self, name, action_type):
        self.id = Resource.resource_count
        Resource.resource_count += 1
        self.name = name
        self.action = action_type
        Resource.resource_dict[self.name] = {"object": self, "name": name, "action": self.action}


class Role(Resource):
    role_count = 1
    role_dict = {}


    def create_role(self, name, resource_dict):
        self.id = Role.role_count
        Role.role_count += 1
        self.name = name
        resource_obj_list = []
        res_display_list = []
        for key in resource_dict:
            resource = Resource()
            resource.create_resource(key, resource_dict[key])
            resource_obj_list.append(resource)
            res_display_dict = {}
            res_display_dict['resource_name'] = key
            res_display_dict['resource_action'] = self.get_action_type(resource_dict[key])
            res_display_list.append(res_display_dict)
        self.resource = resource_obj_list
        self.resource_desc = res_display_list
        Role.role_dict[name] = {'object': self, 'resource': self.resource}


    def get_role_desc(self):
        return "Name : " + str(self.name) +" ," + str(self.resource_desc)
