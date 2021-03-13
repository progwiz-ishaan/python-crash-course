def build_profile(first, last, **user_info):
    """Build a dict containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('ishaan', 'kale', password=411057)
print(user_profile)