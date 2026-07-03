key_store_db=1869	#passkey store here for temp.until testing is complete

login_logDB=[]          #isolated dbase for storing login.logs

def security(key_store_db,passkey):	#main security for accessing the system
	try:
		if passkey == key_store_db:
			print('Access granted')
		else:
			print(f'Access denied\n...{passkey} is incorrect')
	except Exception as e:
		return f'{e}'
passkey=int(input('Enter key to continue\n>> ')
security()

def login_attempts(key_store_db,passkey):
	#try return ip by validating passkey
	enter_ip=str(input('Enter ip\n>> '))
	if enter_ip in ip_password_dict:
		print('ip found')
			while enter_ip in ip_password_dict:
			for i in range(3):      #break at 3 attempts
				enter_passkey=input('Enter passkey\n>> ')
				if enter_passkey not in ip_password_dict[enter_ip]:
					print('Access denied')
				else:
					print('Access granted')
					if enter_passkey in ip_password_dict[enter_ip]:
						def fail_log(enter_ip,enter_passkey,login_logDB):
							for enter_passkey in enter_passkey:
								usr_log=f'{enter_ip} logs     ... passkey from {enter_ip} attempted >> {enter_passkey}'
								login_logDB.insert(0,usr_l    og)
								print(login_logDB)
								fail_log(enter_ip,enter_passkey,login_logDB)
					else:
						pass
					break
				break
	else:
            print('ip not found')

login_attempts()

def menu():
	if passkey==key_store_db:
		print('1. Add failed login attempt')
		print('2. View all logs')
		print('3. View suspicious IPs (3+ attempts)')
		print('4. View brute force attacks (5+ attempts)')
		print('5. Blacklist management')
		print('6. Whitelist management')
		print('7. Generate report')
		print('8. Clear logs')
		print('9. Exit')
	else:
		return
sel_menu=int(input('Choose option\n>> '))
menu()
