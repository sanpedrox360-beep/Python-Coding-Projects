test_settings = {'theme': 'light', 'language': 'English'}

def add_setting(old_settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in old_settings.keys():
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        old_settings[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(old_settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if not(key in old_settings.keys()):
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'
    else:
        old_settings[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'

def delete_setting(old_settings, key):
    key = key.lower()
    if key in old_settings.keys():
        del(old_settings[key])
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(settings):
    if len(settings.keys()) == 0:
        return 'No settings available.'
    else:
        view = f'Current User Settings:\n'
        for key, value in settings.items():
            key = key.capitalize()
            view += f'{key}: {value}\n'
        return view