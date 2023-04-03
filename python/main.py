# import automation


# login_Status = False
login_Status = False
resp = input("New User?(Y/N)\n")
resp = resp.capitalize().strip()
if login_Status == False:
    while resp != "Y" or resp != "N" and not login_Status:
        if resp == "N":
            name = input("enter the business name:")
            # Search user files to see if the BUSINESS_NAME.json is there
            login_Status = True
        elif resp == "Y":
            account_Make = input("Make a account?")
            account_Make = account_Make.capitalize().strip()
            while account_Make != "Y" or account_Make != "N":
                if account_Make == "Y":
                    print()
                    # run make user
                    login_Status = True
                    break
                elif account_Make == "N":
                    exit()
                else:
                    print("invalid response try again")
                    account_Make = input("New User? (Y/N)\n")
                    account_Make.capitalize().strip()
        else:
            print("invalid response try again")
            resp = input("New User? (Y/N)\n")
            resp.capitalize().strip()
if login_Status:
    print("Running Automation..............")
    while login_Status:  # while Logged in print user status run automation
        # Start adding threads to split for Scheduler/Arduino
        automation()
        x = 3
