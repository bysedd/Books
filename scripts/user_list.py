from typing import Dict

from scripts.users import Users, generate_user
from utils.logger import log


class UserList:
    """
    This class provides capabilities for storing, searching for, and deleting User instances.
    """

    def __init__(self):
        """
        This constructor creates a new dictionary collection for User instances.
        """
        self.user_collection: Dict[str, Users] = {}

    def store_user(self, user_: Users):
        """
        This method stores a User instance in the collection.

        :param user_: The User instance to store.
        """
        try:
            if user_.username in self.user_collection:
                log(f"User '{user_.username}' already stored")
                return
            self.user_collection[user_.username] = user_
            log(f"User '{user_.username}' stored successfully")
        except Exception as ex:
            log(f"Failed to store user '{user_.username}' due to {ex}")

    def remove_user(self, first_name: str):
        """
        This method removes a user by their first name.

        If many users with the same first name exist, it informs the program users.

        :param first_name: The first name of the user to remove.
        """
        try:
            matching_users = [
                user_
                for user_ in self.user_collection.values()
                if user_.firstname == first_name
            ]

            if len(matching_users) > 1:
                log(
                    f"Warning: More than one user with the first name '{first_name}' exists."
                )
                usernames = ", ".join([user_.username for user_ in matching_users])
                log(f"Users with first name '{first_name}': {usernames}")
                username = input("Enter the username of the user you want to remove: ")

                if (
                    username in self.user_collection
                    and self.user_collection[username].firstname == first_name
                ):
                    del self.user_collection[username]
                    log(f"User '{username}' removed successfully")
                else:
                    log(
                        f"No user with username '{username}' and first name '{first_name}'"
                    )

            elif len(matching_users) == 1:
                for username, user_ in self.user_collection.items():
                    if user_ == matching_users[0]:
                        del self.user_collection[username]
                        log(f"User '{username}' removed successfully")
                        break

            else:
                log(f"No user with first name '{first_name}'")

        except Exception as ex:
            log(f"Failed to remove {first_name}'s user due to {ex}")

    def count_users(self) -> int:
        """
        This method returns the count of users in the system.

        This should be based on the number of user objects in the user collection.

        :return: Total count of users
        """
        return len(self.user_collection)

    def get_user(self, username: str) -> Users:
        """
        This method returns a user's detail by the username.

        :param username: The username of the user.
        :return: The User instance.
        """
        try:
            return self.user_collection[username]
        except KeyError:
            log(f"User '{username}' not found.")
        except Exception as ex:
            log(f"An error occurred: {ex}")

    def __repr__(self):
        return f"{type(self).__name__}({self.__dict__!r})"


if __name__ == "__main__":
    user_list = UserList()

    user1 = generate_user(first_name="Patrick")
    user2 = generate_user(first_name="Patrick")

    user_list.store_user(user1)
    user_list.store_user(user2)
    print()

    print(user_list.get_user(user1.username))
    print()
    print(user_list.get_user(user2.username))
    print()

    user_list.remove_user("Patrick")
    print()

    print(f"Total users: {user_list.count_users()}")
