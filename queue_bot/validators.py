def validate_name(name):
    clean_name = name.strip()
    return 2 <= len(clean_name) <= 80
