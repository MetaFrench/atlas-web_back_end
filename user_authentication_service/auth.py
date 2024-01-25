# auth.py

from auth import _hash_password
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes the input password with bcrypt.hashpw and returns the salted hash.

    Args:
    - password (str): The input password to be hashed.

    Returns:
    - bytes: The salted hash of the input password.
    """
    # Generate a random salt using bcrypt.gensalt()
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt using bcrypt.hashpw
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

# Example usage in main.py

# main.py


# Call _hash_password with a sample password
hashed_password = _hash_password("Hello Holberton")

# Print the result
print(hashed_password)
