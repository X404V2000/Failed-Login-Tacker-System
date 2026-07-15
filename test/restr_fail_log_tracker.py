from datetime import datetime

#CLI color
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

#CONSTANTS
MAX_ATTEMPTS = 5

# DATA STORAGE	//all dbase.tables must be migrated into mysql/psql dbase//
sys_logs = []           # [timestamp, ip, password, status]
iso_dbase = []          # Suspicious IPs (not yet blocked)
blocked_ip = []         # Blocked IPs
failed_counts = []      # [ip, failure_count]
blacklist_ip = []	# blacklisted IPs
whitelist_ip = []	# whitelist IPs
sus_attempts = []	# suspicious login attempts
most_offending_ips = []	# ips with most login failed attempt
	
# CREDENTIALS
ip_password_dict = {"189.136.1.101": "anwbfw9209", "192.168.1.105": "x9k3m7p2q5","203.45.78.22": "p8s1t4u6v2", "10.0.0.15": "r3w5e7q9t1","172.16.0.45": "m2n4b6v8c0", "87.65.43.21": "z9x8c7v6b5","145.32.87.12": "h4j5k6l7p8", "200.100.50.30": "w2q3e4r5t6","192.168.1.200": "y7u8i9o0p1", "10.0.0.25": "a2s3d4f5g6","172.16.1.100": "b7n8m9k0l1", "203.0.113.5": "c3v4b5n6m7","198.51.100.20": "q8w9e0r1t2", "87.65.43.99": "p5o6i7u8y9","145.32.87.55": "l4k5j6h7g8", "192.168.0.50": "f9d0s1a2q3","10.10.10.10": "z8x7c6v5b4", "172.31.0.75": "n3m4k5j6h7","203.45.78.99": "g8f7d6s5a4", "198.51.100.88": "h3j4k5l6q7"}

def log_attempt(ip, password, status):
	#Log a login attempt with timestamp
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")	#timestamp for logs output
	entry = f"{timestamp} | {ip} | {password} | {status}"		#sys.logs structure
	report_entry =  f"{ip} login attempt @ {timestamp} ...  status = {status}"
	sys_logs.insert(0, entry)	#for dbase.sys_logs ... to access system logs
	sus_attempts.insert(0, report_entry)	#for dbase.sus_attempts ... to access system report
	print(f"[LOG] {status}: {ip}")

def is_blocked(ip):
	#Check if IP is in blocked list
	return ip in blocked_ip

def get_fail_count(ip):
	#Get number of failed attempts for an IP
	for entry in failed_counts:
		if entry[0] == ip:
			return entry[1]
	return 0

def increment_fail_count(ip):
	#Increment failed attempt counter
	for entry in failed_counts:
		if entry[0] == ip:
			entry[1] += 1
			return entry[1]
	# First failure for this IP
	failed_counts.append([ip, 1])
	return 1

def reset_fail_count(ip):
	#Reset failed attempts on successful login
	for i, entry in enumerate(failed_counts):
		if entry[0] == ip:
			failed_counts.pop(i)
			return

def block_ip(ip):	#manually adds IPs to blocked dbase.blocked_ip_table
	#Add IP to blocked list
	if ip not in blocked_ip:
		blocked_ip.append(ip)
		print(f"IP {ip} has been BLOCKED.")
		return True
	print(f"IP {ip} is already blocked.")
	return False

def unblock_ip(ip):
	#Remove IP from blocked list
	if ip in blocked_ip:
		blocked_ip.remove(ip)
		reset_fail_count(ip)  # Reset their failures too
		print(f"IP {ip} has been UNBLOCKED.")
		return True
	print(f"IP {ip} is not blocked.")
	return False

def view_blocked():
	#Display all blocked IPs
	if not blocked_ip:
		print("\nNo IPs are currently blocked.")
	else:
		print("\nBLOCKED IPs:")
		for ip in blocked_ip:
			status = []	#storage needed
			if ip in blacklist_ip:
				status.append("BLACKLISTED")
			if ip in whitelist_ip:
				status.append("WHITELISTED")
			status_str = f" ({', '.join(status)})" if status else ""
			print(f">> {ip}{status_str}")

def ip_blacklist(ip):	#manually adds IPs to blacklist dbase.blacklist_table
	if ip in whitelist_ip:
		whitelist_ip.remove(ip)
		print(f"IP {ip} removed from whitelist")

	if ip not in blacklist_ip:
		blacklist_ip.append(ip)
		print(f"IP {ip} has been blacklisted from the system.")
		return True
	print(f"IP {ip} is already blacklisted")
	return False		

# new whitelist function
def ip_whitelist(ip):
	#Checks if IP already whitelisted
	if ip in whitelist_ip:
		print(f"IP {ip} is already whitelisted.")
		return False
	#Removes IP from blacklist if in blacklist
	if ip in blacklist_ip:
		blacklist_ip.remove(ip)
	#Add IP to whitelist
	if ip in blocked_ip:
		reset_fail_count(ip)
	#Unblock IP if blocked
	if ip in blocked_ip:
		blocked_ip.remove(ip)
	print(f"IP {ip} has been WHITELISTED.")
	return True

def view_whitelisted():
	if not whitelist_ip:
		print(f"\nNo IPs are currently whitelisted.")
	else:
		print("\nWHITELISTED IPs (Bypass all restrictions):")
		for ip in whitelist_ip:
			print(f">> {ip}")

def remove_whitelist(ip):
	if ip in whitelist_ip:
		whitelist_ip.remove(ip)
		print(f"IP {ip} removed from whitelist.")
		return True
	print(f"IP {ip} is not whitelisted.")
	return False

def view_blacklisted():
	if not blacklist_ip:
		print(f"\nNo IPs are currently blackedlisted.")
	else:
		print("\nBLACKELISTED IPs:")
		for ip in blacklist_ip:
			print(f">> {ip}")

# MAIN AUTHENTICATION
def authenticate(ip, password):
	#Main authe_funct with brute force detection
	if ip in whitelist_ip:		#Checks whitelist 
		print(f"\nWhitelisted IP: {ip}")

	if ip in blacklist_ip:		#Checks if IP is blacklisted
		print(f"\nPERMANENTLY BLACKLISTED: {ip}")
		log_attempt(ip, password, "BLACKLISTED")
		return False

	if is_blocked(ip):		#Checks if IP is blocked
		print(f"\nACCESS DENIED: IP {ip} is BLOCKED.")
		log_attempt(ip, password, "BLOCKED")
		return False
    
	if ip not in ip_password_dict:		#Checks if IP exists in system
		print(f"\nIP {ip} not found in system.")
		log_attempt(ip, password, f"UNKNOWN IP...who is {ip}")
		iso_dbase.append(ip)  # Track suspicious IPs
		return False
    
	correct_password = ip_password_dict[ip]		#Checks password ... with attempt limit
	for attempt in range(1, MAX_ATTEMPTS + 1):
		if attempt == 1:
			current_password = password		#First attempt uses passed parameter
		else:
			current_password = input(f"\nEnter Password (attempt {attempt}/{MAX_ATTEMPTS})\n>> ")		#Subsequent attempts prompt user
        
		if current_password == correct_password:	#Checks password
			print(f"\n{GREEN}ACCESS GRANTED for {ip}{RESET}")
			log_attempt(ip, current_password, "SUCCESS")
			reset_fail_count(ip)  # Reset on success
			return True
		else:
			print(f"{GREEN}Invalid password (attempt {attempt}/{MAX_ATTEMPTS}{RESET})")
			fail_count = increment_fail_count(ip)		# Counts failures
			log_attempt(ip, current_password, f"{GREEN}FAILED{RESET}")
			if fail_count >= MAX_ATTEMPTS:		# Checks for brute force
				print(f"\nBRUTE FORCE DETECTED! {ip} has {fail_count} failed attempts.")
				block_ip(ip)
				return False
    
	# This should never reach, but just in case
	return False

#MENU SYSTEM
def show_menu():
	RED = '\033[91m'
	GREEN = '\033[92m'
	RESET = '\033[0m'
	print("="*100)
	print(" "*4,f"{GREEN}0110{RESET}"," "*5,f"{GREEN}0110 0110{RESET}", " "*7,f"{GREEN}0110 0110{RESET}", " "*11,f"{GREEN}0110 0110{RESET}", " "*5,f"{GREEN}0110 0110{RESET}", " "*2,f"{GREEN}0110 0110{RESET}")
	print(" "*3,f"{GREEN}0110{RESET}", " "*4,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " "*7,f"{GREEN}0110{RESET}", " "*2,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " "*6,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}")
	print(" "*2,f"{GREEN}0110{RESET}", " "*4,f"{GREEN}0110{RESET}", " "*5,f"{GREEN}0110{RESET}", " "*1,f"{GREEN}0110{RESET}", " "*19,f"{GREEN}0110{RESET}", " "*8,f"{GREEN}0110 0110{RESET}", " "*1,f"{GREEN}0110{RESET}")
	print(" "*1,f"{GREEN}0110{RESET}", " "*4,f"{GREEN}0110{RESET}", " "*5,f"{GREEN}0110{RESET}", " "*1,f"{GREEN}0110  0110 0110{RESET}", " "*12,f"{GREEN}0110{RESET}", " "*4,f"{GREEN}0110 0110{RESET}", " "*1,f"{GREEN}0110{RESET}")
	print("",f"{GREEN}0110 0110{RESET}", " "*1,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}", " ",f"{GREEN}0110{RESET}", "",f"{GREEN}0110{RESET}", " "*2,f"{GREEN}0110{RESET}", " "*1,f"{GREEN}0110{RESET}", " "*7,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110{RESET}")
	print(f"{GREEN}0110 0110{RESET}", " "*4,f"{GREEN}0110 0110{RESET}", " "*7,f"{GREEN}0110 0110{RESET}", " "*1,f"{GREEN}0110{RESET}", " "*3,f"{GREEN}0110 0110{RESET}", " "*2,f"{GREEN}0110 0110{RESET}", " "*5,f"{GREEN}0110 0110{RESET}")
	print(f"{RED}LOGIN TRACKER SYSTEM{RESET}")
	print("="*100)
	print(f"{RED}[1]{RESET}{GREEN}. Attempt Login{RESET}")
	print(f"{RED}[2]{RESET}{GREEN}. View Logs{RESET}")
	print(f"{RED}[3]{RESET}{GREEN}. View Blocked IPs{RESET}")
	print(f"{RED}[4]{RESET}{GREEN}. Unblock IP{RESET}")
	print(f"{RED}[5]{RESET}{GREEN}. View Failed Attempts{RESET}")
	print(f"{RED}[6]{RESET}{GREEN}. View Blacklisted IPs{RESET}")
	print(f"{RED}[7]{RESET}{GREEN}. Blacklist IP{RESET}")
	print(f"{RED}[8]{RESET}{GREEN}. View Whitelisted IPs{RESET}")
	print(f"{RED}[9]{RESET}{GREEN}. Whitelist IP{RESET}")
	print(f"{RED}[10]{RESET}{GREEN}. Remove from Whitelist{RESET}")	#Add this //new feature update//
	print(f"{RED}[11]{RESET}{GREEN}. Suspicious Report{RESET}")
	print(f"{RED}[12]{RESET}{GREEN}. Most Offending IPs{RESET}")
	print(f"{RED}[13]{RESET}{GREEN}. Clear All Data{RESET}")
	print(f"{RED}[14]{RESET}{GREEN}. Exit{RESET}")
	print("="*50)

def view_logs():
	#Display login logs
	if not sys_logs:
		print(f"\n{GREEN}No logs recorded yet.{RESET}")
		return
	print("\n" + "="*70)
	print(f"{'TIMESTAMP':<20} {'IP':<16} {'STATUS':<10} {'PASSWORD'}")
	print("="*70)
	for entry in sys_logs:
		parts = entry.split(" | ")
		print(f"{parts[0]:<20} {parts[1]:<16} {parts[3]:<10} {parts[2]}")
	print("="*70)

def view_failed_counts():
	#Display failed attempt counters
	if not failed_counts:
		print(f"\n{GREEN}No failed attempts recorded.{RESET}")
		return
	print(f"\n{RED}FAILED ATTEMPTS:{RESET}")
	print("-" * 30)
	for ip, count in failed_counts:
		status = "BLOCKED" if is_blocked(ip) else "ACTIVE"
		print(f"  {ip}: {count} failures - {status}")
	print("-" * 30)

def view_sus_attempt_():
	if not sus_attempts:
		print(f"\n{GREEN}No report found{RESET}")
		return
	print("\n" + "="*70)
	print(f"{RED}SYSTEM REPORT{RESET}")
	print("="*70)
	for report_entry in sus_attempts:
		print(report_entry)
	print("="*70)

#new function
#view most offending login attempts
#attempts = 5 are on top since they indicate suspicious activity
#attempts below 5 and above 2 are in the bottom
def view_most_offending_ips():
	if not failed_counts:  #Checks if there are any failures
		print(f"\n{GREEN}No failed attempts recorded.{RESET}")
		return
    
	print("\n" + "="*70)
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"{RED}OFFENDING IPS REPORT ... {timestamp}{RESET}")
	print("="*70)
    
	# Sort by failure count (highest first)
	sorted_ips = sorted(failed_counts, key=lambda x: x[1], reverse=True)
    
	for ip, count in sorted_ips:
		if count >= 5:
			entry_1 = f"{ip}: {count} failures ... IMMEDIATE ACTION REQUIRED!"
			most_offending_ips.append(entry_1)
		elif count >= 4:
			entry_2 = f"{ip}: {count} failures ... INVESTIGATE TRAFFIC"
			most_offending_ips.append(entry_2)
		elif count >= 3:
			entry_3 = f"{ip}: {count} failures ... INVESTIGATE TRAFFIC"
			most_offending_ips.append(entry_3)
		elif count >= 2:
			entry_4 = f"{ip}: {count} failures ... INVESTIGATE TRAFFIC"
			most_offending_ips.append(entry_4)
		else:
			entry_5 = f"{ip}: {count} failures ... Monitor"
			most_offending_ips.append(entry_5)
	
	print("="*70)

def clear_all():
	global sys_logs, iso_dbase, blocked_ip, failed_counts, blacklist_ip, whitelist_ip, most_offending_ips
	sys_logs = []
	iso_dbase = []
	blocked_ip = []
	failed_counts = []
	blacklist_ip = []
	whitelist_ip = []
	most_offending_ips = []
	print(f"{GREEN}All data cleared.{RESET}")

# MAIN PROGRAM
def main():
	#Main program loop
	print(f"\n{RED}Welcome!\n... log_tracker.sys running{RESET}")

	while True:
		show_menu()
		choice = input(f"\n{GREEN}Choose Option: {RESET}").strip()
		if choice == "1":
			print(f"\n{GREEN}--- LOGIN ATTEMPT ---{RESET}")
			ip = input(f"{GREEN}Enter IP: {RESET}").strip()
			password = input(f"{GREEN}Enter Password: {RESET}").strip()
			authenticate(ip, password)
		elif choice == "2":
			view_logs()
		elif choice == "3":
			view_blocked()
		elif choice == "4":
			ip = input(f"{GREEN}Enter IP to unblock: {RESET}").strip()
			unblock_ip(ip)
		elif choice == "5":
			view_failed_counts()
		elif choice == "6":
			view_blacklisted()
		elif choice == "7":
			ip = input(f"{GREEN}Enter IP you want to blacklist: {RESET}").strip()
			ip_blacklist(ip)
		elif choice == "8":
			view_whitelisted()
		elif choice == "9":
			ip = input(f"{GREEN}Enter IP to remove from blacklisted IPs: {RESET}").strip()
			ip_whitelist(ip)
		elif choice == "10":
			ip = input(f"{GREEN}Enter IP to remove from whitelist: {RESET}").strip()
			remove_whitelist(ip)
		elif choice == "11":
			view_sus_attempt_()
		elif choice == "12":	#new argument //under-going development//
			view_most_offending_ips()
		elif choice == "13":
			confirm = input(f"{GREEN}Clear ALL data? (y/n): {RESET}").strip().lower()
			if confirm == 'y':
				clear_all()
		elif choice == "14":
			print("\nGoodbye!")
			break
		else:
			print(f"{RED}Invalid choice. Enter 1-10.{RESET}")
		input(f"\n{RED}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    main()
