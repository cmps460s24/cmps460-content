users = {
    'aeinstein': {
        'first': 'Albert',
        'last': 'Einstein',
        'location': 'Princeton',
        },

    'abbas': {
        'first': 'Abbas',
        'last': 'Ibn Firnas',
        'location': 'Córdoba',
        },

    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")