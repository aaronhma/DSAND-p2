class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# COMPLETE FUNCTION


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Returns true if user is in the group name or if user is in group
    # Base case for recursion
    if user == group.get_name() or user in group.get_users():
        return True

    for i in group.get_groups():
        return is_user_in_group(user, i)

    # User is not in group
    return False

# COMPLETE FUNCTION


# Setup data
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# STUDENT TESTS
if __name__ == "__main__":
    print("[RUNNING] Running student tests!")

    try:
        # Test 1
        print(is_user_in_group("child", child))  # True
        assert(is_user_in_group("child", child))

        # Test 2
        print(is_user_in_group("parent", parent))  # True
        assert(is_user_in_group("parent", parent))

        # Test 3
        print(is_user_in_group("", child))  # False
        assert(not is_user_in_group("", child))

        # Test 4
        print(is_user_in_group("", parent))  # False
        assert(not is_user_in_group("", parent))

        # Test 5
        print(is_user_in_group("child", parent))  # True
        assert(is_user_in_group("child", parent))

    except AssertionError:
        raise AssertionError("Tests failed!")

    print("[PASS] Finished student tests!")
# STUDENT TESTS
