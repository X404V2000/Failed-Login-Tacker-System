# Failed-Login-Tacker-System

# 📋 **Project Brief: Failed Login Tracker System**

## **Project Overview**
You are tasked with building a **Failed Login Tracker** - a cybersecurity monitoring tool that detects and alerts on suspicious login attempts. This is your first project as a junior security analyst.

---

## 🎯 **Core Requirements**

### **Phase 1: Basic Functionality (MVP)**
1. **Add Failed Login Attempts**
   - Record IP addresses of failed logins
   - Record the timestamp of each attempt
   - Record the username attempted

2. **Brute Force Detection**
   - Detect when an IP has 5 or more failed attempts
   - Trigger an alert when threshold is reached
   - Display suspicious IPs on demand

3. **View Functions**
   - Show all failed login attempts
   - Show only suspicious IPs (3+ attempts)
   - Count total failed attempts

4. **Data Storage**
   - Store all data in a Python list
   - Each entry stored as a formatted string

---

### **Phase 2: Advanced Features**
5. **IP Blacklist Management**
   - Manually add IPs to blacklist
   - Remove IPs from blacklist
   - Check if an IP is blacklisted

6. **Whitelist Functionality**
   - Add trusted IPs to whitelist
   - Ignore whitelisted IPs in threat detection
   - Display both lists on demand

7. **Reporting**
   - Generate a "suspicious activity report"
   - Show top offending IPs (most attempts)
   - Display attempted usernames for each IP

8. **Clear/Reset**
   - Clear all logs
   - Reset suspicious IP count

---

## 🛠️ **System Components to Build**

### **Core Data Components**
| Component | Purpose | Example Data |
|-----------|---------|--------------|
| Failed Logs List | Store all login attempts | `"2026-07-02 10:15|192.168.1.45|admin"` |
| Blacklist List | Store blocked IPs | `["192.168.1.45", "10.0.0.5"]` |
| Whitelist List | Store trusted IPs | `["192.168.1.1", "10.0.0.1"]` |

### **Functional Modules**
1. **Input Handler**
   - Function to add new login attempts
   - Function to add/remove blacklist entries
   - Function to add/remove whitelist entries

2. **Analysis Engine**
   - Count attempts per IP
   - Detect brute force attempts (≥5 failures)
   - Generate list of suspicious IPs (≥3 failures)
   - Check IP against blacklist/whitelist

3. **Display/Reporting Module**
   - Print all logs formatted nicely
   - Show suspicious IPs with counts
   - Generate summary statistics
   - Show blacklist/whitelist status

4. **Alert System**
   - Print warning when brute force detected
   - Suggest blocking the IP
   - Display alert severity level

### **Menu System**
Build a text-based menu with these options:
- Option 1: Add failed login attempt
- Option 2: View all logs
- Option 3: View suspicious IPs (3+ attempts)
- Option 4: View brute force attacks (5+ attempts)
- Option 5: Blacklist management
- Option 6: Whitelist management
- Option 7: Generate report
- Option 8: Clear logs
- Option 9: Exit

---

## 📝 **Data Format Specifications**

### **Log Entry Format**
```
"YYYY-MM-DD HH:MM|IP_ADDRESS|USERNAME"
```
Example: `"2026-07-02 14:23|192.168.1.100|jsmith"`

### **Requirements for Each Entry**
- Must include all 3 components separated by `|`
- Timestamp must be in the specified format
- IP must be valid (you don't need to validate, but follow format)
- Username can be any string

---

## 🔍 **Analysis Rules**

### **Suspicious Threshold**
- **Suspicious:** IP with ≥3 failed attempts
- **Brute Force:** IP with ≥5 failed attempts

### **Priority Rules**
1. Check whitelist FIRST - ignore whitelisted IPs
2. Then check blacklist - flag as blocked
3. Finally analyze attempts - check for brute force

---

## 📊 **Report Requirements**

A report should show:
1. **Summary:** Total attempts, unique IPs, suspicious IPs
2. **Top Offenders:** IPs with most failed attempts (sorted)
3. **Blacklisted IPs:** Show all currently blacklisted
4. **Whitelisted IPs:** Show all currently whitelisted
5. **Timeline:** Show attempts grouped by time

---

## 🧪 **Test Scenarios to Build**

### **Scenario 1: Basic Detection**
- Add 5 failed attempts from `192.168.1.45` with different usernames
- Should trigger brute force alert
- Should show this IP as suspicious

### **Scenario 2: Whitelist Override**
- Add `10.0.0.1` to whitelist
- Add 10 failed attempts from `10.0.0.1`
- Should NOT trigger any alerts (ignored)

### **Scenario 3: Blacklist Management**
- Add `203.0.113.5` to blacklist
- Add one failed attempt from this IP
- Should show "BLOCKED" message

### **Scenario 4: Multiple Attackers**
- Add 3 attempts from `192.168.1.10`
- Add 4 attempts from `192.168.1.20`
- Add 7 attempts from `192.168.1.30`
- Should show all 3 as suspicious, last one as brute force

---

## 🚀 **Stretch Goals (Optional)**

If you finish early:
- Save/load data to/from a text file
- Add password strength checking for attempted usernames
- Add time-based analysis (attempts per hour)
- Export report to a text file
- Add color coding (red for alerts, green for safe)

---

## 📅 **Project Timeline (Suggested)**

| Day | Focus |
|-----|-------|
| Day 1 | Set up project structure, implement log storage, add basic functions |
| Day 2 | Build analysis engine (counting, detecting brute force) |
| Day 3 | Implement blacklist and whitelist functionality |
| Day 4 | Build the menu system and user interface |
| Day 5 | Testing, debugging, and polish |

---

## ✅ **Acceptance Criteria**

Your project is complete when:
- [ ] Can add failed login attempts with all required data
- [ ] Automatically detects brute force (5+ attempts)
- [ ] Can show suspicious IPs (3+ attempts)
- [ ] Can add/remove IPs from blacklist
- [ ] Can add/remove IPs from whitelist
- [ ] Whitelist overrides detection
- [ ] Menu system works with all functions
- [ ] Can generate a report
- [ ] All test scenarios pass

---

## 💼 **Deliverables**

1. **Single Python file** with your complete project
2. **Test results** showing all scenarios work
3. **Screenshots** of the menu in action (optional)

---

## ❓ **Questions to Consider Before Coding**

1. How will you store timestamp, IP, and username in one string?
2. How will you extract IP from a log entry to count attempts?
3. How will you handle the case where an IP is in both blacklist and whitelist?
4. What happens if the user enters invalid data?
5. How will you display logs in a readable format?

---

**Get started by planning your data structures first, then build each feature one at a time. Test as you go!**

*Deadline: 5 days*  
*Priority: High*  
*Type: Individual Project*

Good luck, analyst! Let me know when you have questions about the requirements. 🎯
