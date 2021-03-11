# Start with users that need to be verifeied,
# and a empty list to hold the users.
unconfirmed_users = ['ojas', 'shubham', 'ishaan']
confirmed_users = []

# Verify each user until there are no unconfirmed users left.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)
# Display all the current users
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())