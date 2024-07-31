# This script is designed to help with testing common SCIM operations.
# First Release Aug 31, 2022
# Last updated October 10, 2022
# Change:  added deactivate and reactivate
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests

#checking user list
def check_users(token):
  url = "https://api.control.verkada.com/scim/Users"
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  response = requests.get(url, headers=headers)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#checking group list
def check_groups(token):
  url = "https://api.control.verkada.com/scim/Groups"
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  response = requests.get(url, headers=headers)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#add a user to organization
def add_user(token, email, firstname, lastname, middlename, employeetitle, employeetype, companyname, employeeId, department, departmentId):
  url = "https://api.control.verkada.com/scim/Users"
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  data = {
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
  ],
  "userName": email,
  "active": True,
  "meta": {
    "resourceType": "User"
  },
  "name": {
    "familyName": lastname,
    "givenName": firstname,
    "middleName": middlename
  },
  "title" : employeetitle,
  "userType" : employeetype,
  "organization" : companyname,
  "employeeNumber" : employeeId,
  "department" : department,
  "costCenter" : departmentId
  }
  response = requests.post(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#delete a user from the organization
def delete_user(token, userId):
  url = "https://api.control.verkada.com/scim/Users/" + userId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  response = requests.delete(url, headers=headers)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#add a group to the organization
def add_group(token, addGroup):
  url = "https://api.control.verkada.com/scim/Groups"
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  data = {"displayName": "" + (addGroup)
  }
  response = requests.post(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Delete a group in the organization
def delete_group(token, groupId):
  url = "https://api.control.verkada.com/scim/Groups/" + groupId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  response = requests.delete(url, headers=headers)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Add users to groups
def add_into_group(token, groupId, userId):
  url = "https://api.control.verkada.com/scim/Groups/" + groupId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  data = {
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations": [{
            "op": "add",
            "path": "members",
            "value": [{
                "value": "" + userId
            }]
        }]
    }
  response = requests.patch(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Delete users from groups
def delete_from_group(token, groupId, userId):
  url = "https://api.control.verkada.com/scim/Groups/" + groupId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  data = {
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations": [{
            "op": "remove",
            "path": "members",
            "value": [{
                "value": "" + userId
            }]
        }]
    }
  response = requests.patch(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Check users in group
def check_users_in_group(token, groupId):
  url = "https://api.control.verkada.com/scim/Groups/" + groupId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  response = requests.get(url, headers=headers)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Check user details
def check_user_details(token, userId):
  url = "https://api.control.verkada.com/scim/Users/" + userId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
  }
  response = requests.get(url, headers=headers)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Change user details
def change_user_details(token, userId, userchanges):
  url = "https://api.control.verkada.com/scim/Users/" + userId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
  }
  data = userchanges
  response = requests.put(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Deactivate user
def deactivate_user(token, userId):
  url = "https://api.control.verkada.com/scim/Users/" + userId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  data = {
  "schemas": [
      "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
      {
          "op": "replace",
          "path": "active",
          "value": False
      }
  ]
  }
  response = requests.patch(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

#Reactivate user
def reactivate_user(token, userId):
  url = "https://api.control.verkada.com/scim/Users/" + userId
  headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + (token)
}
  data = {
  "schemas": [
      "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
      {
          "op": "replace",
          "path": "active",
          "value": True
      }
  ]
  }
  response = requests.patch(url, headers=headers, json = data)
  print("HTTP Response code: ")
  print(response.status_code)
  print("\n")
  print(response.text + "\n" + "\n")

def main():

  while True:

    #intro where you prompt for a token so that stuff can be done
    token = input("Enter SCIM token or enter q to exit\n")

    if token == "q":
      break
    elif len(token) != 72:
      print("Invalid token. Missing characters or too many characters on the token.\n")
    
    #found that all tokens are 72 characters
    elif len(token) == 72:
      pass
      

      #menu where stuff can actually be done
      while True:
        x = input("\nSCIM Options\n 1. List users\n 2. Check user's details (you'll need user ID from option 1)\n 3. Add user\n 4. Delete a user (you'll need user ID from option 1)\n 5. Change details in a user (you'll need user ID from option 1) !!Note: Phone number and email is unchangeable!!\n 6. Deactivate users\n 7. Reactivate users\n\n 8. List groups\n 9. Add groups\n 10. Delete groups (You'll need group ID from option 6)\n 11. Check all users in group\n 12. Add user into a group (You'll need group ID from option 6 and user ID from option 1)\n 13. Remove a user in a group (You'll need group ID from option 6 and user ID from option 1)\n \nAll outputs are in JSON and you'll need a JSON formatter to clearly see the output(make pretty). I personally use https://jsonformatter.org/ \n \nEnter q to change token.\n")
        
        #checking user list flow
        if x == "1":
          check_users(token)
        
        #check user details
        elif x == "2":
          userId = input("Enter user ID: \n")
          check_user_details(token, userId)

        #adding user flow
        elif x == "3":
          addEmail = input("Enter email:\n")
          addFirst = input("Enter first name:\n")
          addLast = input("Enter last name:\n")
          #wooooo badge printing AYYYYYY
          addmiddlename = input("Enter middle name (Optional! Hit enter to skip!)\n")
          addemployeetitle = input("Enter employee title (Optional! Hit enter to skip!)\n")
          addemployeetype = input("Enter employee type (Optional! Hit enter to skip!)\n")
          addcompanyname = input("Enter company name (Optional! Hit enter to skip!)\n")
          addemployeeId = input("Enter employee ID (Optional! Hit enter to skip!)\n")
          adddepartment = input("Enter name of department (Optional! Hit enter to skip!)\n")
          adddepartmentId = input("Enter department ID (Optional! Hit enter to skip!)\n")
          add_user(token, addEmail, addFirst, addLast, addmiddlename, addemployeetitle, addemployeetype, addcompanyname, addemployeeId, adddepartment, adddepartmentId)

        #deleting user flow
        elif x == "4":
          userId = input("Enter userId: \n")
          delete_user(token, userId)

        #change user flow
        elif x == "5":
          userId = input("Enter User ID that you want to change:\n")
          check_user_details(token, userId)
          userchanges = input("Copy the output, make your changes on the user in json (may need to make pretty), then enter in your new json (highly suggest you minify or compact it before entering it in)\n")
          change_user_details(token, userId, userchanges)

        #deleting user flow
        elif x == "6":
          userId = input("Enter userId: \n")
          deactivate_user(token, userId)

        #deleting user flow
        elif x == "7":
          userId = input("Enter userId: \n")
          reactivate_user(token, userId)

        #checking group flow
        elif x == "8":
          check_groups(token)

        #adding group flow
        elif x == "9":
          addGroup = input("Enter group name:\n")
          add_group(token, addGroup)

        #delete group flow
        elif x == "10":
          groupId = input("Enter group ID: \n")
          delete_group(token, groupId)
        
        #Check users in group flow
        elif x == "11":
          groupId = input("Enter group ID: \n")
          check_users_in_group(token, groupId)

        #add user into group flow
        elif x == "12":
          groupId = input("Enter group ID: \n")
          userId = input("Enter user Id that will go into the group: \n")
          add_into_group(token, groupId, userId)
        
        #delete user in group flow
        elif x == "13":
          groupId = input("Enter group ID: \n")
          userId = input("Enter user Id that will be removed in the group: \n")
          delete_from_group(token, groupId, userId)
        
        #Quit
        elif x == "q":
          break
        
        else:
          print("Invalid input. Try again\n")

if __name__ == "__main__":
    main()