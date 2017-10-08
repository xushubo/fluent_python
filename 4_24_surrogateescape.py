import os

print(os.listdir('text_file/.'))
print(os.listdir(b'text_file/.'))
pi_name_bytes = os.listdir(b'text_file/.')[1]
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
# print(pi_name_str)
print(pi_name_str.encode('ascii', 'surrogateescape'))