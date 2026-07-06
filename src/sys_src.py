def auth_(ip_key,passwd_key):
	try:
		if ip_key in ip_password_dict:
			print(f'IP {ip_key} found')
			for i in range(5):
				if passwd_key in ip_password_dict[ip_key]:
					print('Access granted')
					return True
				else:
					if i < 4:
						print(f'Access denied. {4-i} attempts remaining')
						passwd_key=input('Enter Password\n>> ')
					else:
						print('Access denied. Maximum attempts exceeded.')
						return False	
		else:
			print(f'IP {ip_key} not in system')
	except Exception as e:
		return f'{e}'

ip_password_dict = {"189.136.1.101": "anwbfw9209",
		"192.168.1.105": "x9k3m7p2q5",
		"203.45.78.22": "p8s1t4u6v2",
		"10.0.0.15": "r3w5e7q9t1",
		"172.16.0.45": "m2n4b6v8c0",
		"87.65.43.21": "z9x8c7v6b5",
		"145.32.87.12": "h4j5k6l7p8",
		"200.100.50.30": "w2q3e4r5t6",
		"192.168.1.200": "y7u8i9o0p1",
		"10.0.0.25": "a2s3d4f5g6",
		"172.16.1.100": "b7n8m9k0l1",
		"203.0.113.5": "c3v4b5n6m7",
		"198.51.100.20": "q8w9e0r1t2",
		"87.65.43.99": "p5o6i7u8y9",
		"145.32.87.55": "l4k5j6h7g8",
		"192.168.0.50": "f9d0s1a2q3",
		"10.10.10.10": "z8x7c6v5b4",
		"172.31.0.75": "n3m4k5j6h7",
		"203.45.78.99": "g8f7d6s5a4",
		"198.51.100.88": "h3j4k5l6q7"}
ip_key=input('Enter IP\n>> ')
passwd_key=input('Enter Password\n>> ')
auth_(ip_key,passwd_key)
