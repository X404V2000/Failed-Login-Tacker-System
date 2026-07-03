#main menu security to access system
def security(key_store_db,passkey):	#main security for accessing the system
	try:
		if passkey == key_store_db:
			print('Access granted')
		else:
			print(f'Access denied\n...{passkey} is incorrect')
	except Exception as e:
		return f'{e}'
passkey=int(input('Enter key to continue\n>> '))
security(key_store_db,passkey)

#system dbases
#all need psql dbase integration after testing is complete
def dbase(key_store_db,login_logDB,brut_forceDB,isoDB):
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
	key_store_db=1896	#passwd dbase for temp use
	login_logDB=[]          #isolated dbase for storing login.logs
	brut_forceDB=[]		#DB to store brute force data
	isoDB=[]		#store ip in isolation for further investigation
print('DATABASES\n1. key_store_db\n2. login_logDB\n3. brut_forceDB\n4. isoDB')
dbase(key_store_db,login_logDB,brut_forceDB,isoDB)

def login_attempts(key_store_db,passkey,enter_passkey):
	if passkey == key_store_db:
		#try return ip by validating passkey
		enter_ip=str(input('Enter ip\n>> '))
		if enter_ip in ip_password_dict:
			print('ip found')
			while enter_ip in ip_password_dict:
				for i in range(10):      #break at 10 attempts
					enter_passkey=input('Enter passkey\n>> ')
					if enter_passkey not in ip_password_dict[enter_ip]:
						print('Access denied')
					else:
						print('Access granted')
					break
					
				def login_attempts_store(enter_passkey):
					if enter_passkey in ip_password_dict[enter_ip]:
						def fail_log(enter_ip,enter_passkey,login_logDB):
							for enter_passkey in enter_passkey:
								usr_log=f'{enter_ip} logs     ... passkey from {enter_ip} attempted >> {enter_passkey}'
								login_logDB.insert(0,usr_log)
								print(login_logDB)
								fail_log(enter_ip,enter_passkey,login_logDB)
					else:
						pass
				login_attempts_store(enter_passkey)	

				break
		else:
		    print('ip not found')
	else:
		return
login_attempts(key_store_db,passkey,enter_passkey)

def brut_det(key_store_db,passkey,enter_passkey):
	if passkey == key_store_db:
		if enter_passkey >= 5:		#5 or more login attempts
			log_text=f"IP: {enter_ip} attempted login to system... with passkey: {enter_passkey}"
			brut_forceDB.insert(0,log_text)
			while enter_passkey>=5:
				sys_analysis_arg=input('Want to analyse the situation much further\ny/N\n>> ')
				if sys_analysis_arg =="y" or "Y":
					print(brut_forceDB)
					sys_analysis_2_arg=int(input('Choose Option>>\n1. Isolate IP\n2. Cancel\n>> '))
					if sys_analysis_2_arg == 1:
						isoDB.insert(0,enter_ip)
						print(isoDB)		#for testing
					elif sys_analysis_2_arg == 2:
						print('Cancelling operation')
					else:
						print('Invalid Error')
				break
		else:
			pass
	else:
		return 
brut_det(key_store_db,passkey,enter_passkey)
