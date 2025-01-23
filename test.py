from django.contrib.auth.hashers import make_password

# Hash the password "123"
hashed_password = make_password("123")
print(hashed_password)
