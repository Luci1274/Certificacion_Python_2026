def add_setting(config, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in config:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        config[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(config, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in config:
        config[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(config, setting):
    key = setting
    key = key.lower()
    if key in config:
        config.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(config):
    if not config:
        return "No settings available."
    
    resultado = "Current User Settings:\n"
    for key, value in config.items():
        resultado += f"{key.capitalize()}: {value}\n"
    
    return resultado


test_settings = {"theme": "light"}
setting = ("Volumen", "Alto")
key, value = setting
print(add_setting(test_settings, setting))
print(test_settings)

setting = ("Volumen", "bajo")
print(update_setting(test_settings, setting))
print(test_settings)

setting = ("Volumen")
print(delete_setting(test_settings, setting))
print(test_settings)

print(view_settings(test_settings))