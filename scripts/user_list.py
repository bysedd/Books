class UserList:
    def __init__(self):
        self.user_collection = {}

    def store_user(self, user):
        self.user_collection[user.username] = user

    def remove_user(self, firstname):
        count = 0
        for username, user in list(self.user_collection.items()):
            if user.firstname == firstname:
                del self.user_collection[username]
                count += 1
        if count > 1:
            print(f"Warning: There are {count} users with the same first name.")

    def count_users(self):
        return len(self.user_collection)

    def get_user_details(self, username):
        user = self.user_collection.get(username)
        if user:
            return (
                f"Username: {user.get_username()}, Firstname: {user.get_firstname()}, Surname: {user.get_surname()}, "
                f"House Number: {user.get_house_number()}, Street Name: {user.get_street_name()}, "
                f"Postcode: {user.get_postcode()}, Email: {user.get_email()}, DOB: {user.get_dob()}"
            )
        else:
            return "User not found."
