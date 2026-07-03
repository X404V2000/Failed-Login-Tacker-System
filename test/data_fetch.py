ip_user_dict = {
    "189.136.1.101": {"john_doe": "x7kL9pQ2"},
    "189.136.1.102": {"jsmith87": "wR3tZ8cV"},
    "189.136.1.103": {"m_wilson": "bN4fX6jP"},
    "189.136.1.104": {"emily_chen": "aH9sV2kT"},
    "189.136.1.105": {"david_kim": "jM5pQ8wL"},
    "189.136.1.106": {"sarah_j": "cR7nF3xZ"},
    "189.136.1.107": {"mike_ross": "vP2kD9bN"},
    "189.136.1.108": {"lisa_wang": "gS6tY4mE"},
    "189.136.1.109": {"alex_miller": "qZ8rW1hK"},
    "189.136.1.110": {"jessica_t": "fU3eJ7cA"},
    "189.136.1.111": {"ryan_cooper": "nB5yL9xP"},
    "189.136.1.112": {"amanda_l" "xR2wQ8mF"},
    "189.136.1.113": {"chris_evans": "dH7jK4tZ"},
    "189.136.1.114": {"nicole_b": "pS9vC3gE"},
    "189.136.1.115": {"kevin_nguyen": "lM6pX1nR"},
    "189.136.1.116": {"rachel_g": "yW4fJ8bT"},
    "189.136.1.117": {"steven_huang": "kD2qL5vN"},
    "189.136.1.118": {"michelle_lee": "rF9hG6zC"},
    "189.136.1.119": {"brian_taylor": "zX3vP7mK"},
    "189.136.1.120": {"angela_white": "eN8wB4jL"}
}

enter_usr=input('Enter username: ')
enter_passwd=input('Enter password: ')
for ip_user_dict in ip_user_dict:
	if enter_usr in ip_user_dict[enter_usr]:
		print('username found in system')
	else:
		print('no username found in system')
