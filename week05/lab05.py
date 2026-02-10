"""Lab 05: functions and error handling."""

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {
        "name": "charlie",
        "age": 35,
        "is_active": True,
        "email": "charlie@example.com",
    },
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(users_list):
    """Calculate the average age from a list of user dictionaries.

    Parameters
    ----------
    users_list : list
        List of dictionaries that may include an "age" key.

    Returns
    -------
    float
        Average of integer ages. Returns 0.0 on error or when no valid ages exist.
    """
    total_age = 0
    user_count_for_age = 0

    try:
        for user in users_list:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                user_count_for_age += 1
        return total_age / user_count_for_age
    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list.")
        return 0.0
    except (TypeError, AttributeError):
        print("error: users must be a list of dictionaries.")
        return 0.0


def get_active_user_emails(users_list):
    """Return emails for active users.

    Parameters
    ----------
    users_list : list
        List of user dictionaries that may include "is_active" and "email" keys.

    Returns
    -------
    list
        List of email strings for active users. Returns an empty list on error.
    """
    active_user_emails = []

    try:
        for user in users_list:
            if user.get("is_active") and user.get("email"):
                active_user_emails.append(user["email"])
    except (TypeError, AttributeError):
        print("error: users must be a list of dictionaries.")
        return []

    return active_user_emails


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
