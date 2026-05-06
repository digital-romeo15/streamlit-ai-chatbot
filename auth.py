#A simple in-memory dictionary that stores usernames and passwords
#This is only for learning purposes (NOT secure for production use)
USERS = {
    "admin": "password123",
    "user": "streamlit"
}

def authenticate(username: str, password: str) -> bool:
    """
    Checks whether the provided username and password are valid.

    Args:
        username (str): The username entered by the user
        password (str): The password entered by the user

    Returns:
        bool: True if credentials are correct, False otherwise
    """
    #USERS.get(username) returns the password for that user (or None)
        #We compare it to the password provided
    return USERS.get(username) == password
