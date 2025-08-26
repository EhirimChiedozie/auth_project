import requests



global base_url
base_url = 'http://localhost:8000/todo/'


try:
    import tokens
    global headers
    headers = {
            'Authorization': 'Bearer ' + tokens.access_token
        }
except ModuleNotFoundError as e:
    pass


#Make a Login request
def login(username, password):
    details = {
        'username': username,
        'password': password
    }
    try:
        resp = requests.post(base_url + 'token/', json=details)
        access_token = resp.json()['access']
        refresh_token = resp.json()['refresh']
    except KeyError:
        print('Invalid Login Details!!!')
    else:
        with open('tokens.py', 'w') as tok:
            tok.write('access_token = ' + "'" + access_token + "'")
            tok.write('\n'*2)
            tok.write('refresh_token = ' + "'" + refresh_token + "'")
        print('Login Successful and Authentication tokens provided'.title())
    
#View profile
def profile_view():
    
    resp = requests.get(base_url + 'profile/', headers=headers)
    print(resp.json())


#Create 
def create(task, description, deadline_day):
    data = {
        'task': task,
        'description': description,
        'deadline_day': deadline_day
    }
    resp = requests.post(base_url + 'create_todo/', json=data, headers=headers)
    print(resp.json(), resp.status_code)


#Read
def read():
    resp = requests.get(base_url + 'view_todo/', headers=headers)
    print(resp.json())

#Update
def update(post_id, field_name, field_value):
    data = {
        field_name: field_value
    }
    resp = requests.patch(base_url + f'update_todo/{post_id}/', json=data, headers=headers)
    print(resp.status_code, resp.json())

#Delete
def delete(post_id):
    resp = requests.delete(base_url + f'delete_todo/{post_id}/', headers=headers)
    print(resp.status_code, resp.json())


#login('ChiedozieEhirim', 'Mmaduakolam_1996')

#profile_view()

#create('Code Review', 'Review all the codes for the todo list', '2025-09-15')

#read()

#update(4, 'deadline_day', '2020-12-25')

#delete(3)