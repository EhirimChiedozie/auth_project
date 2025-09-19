import requests



global base_url
base_url = 'http://localhost:8000/'


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
        resp = requests.post(base_url + 'todo/token/', json=details)
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
    
    resp = requests.get(base_url + 'todo/profile/', headers=headers)
    print(resp.json())


#Create 
def create(title, content):
    data = {
        'title': title,
        'content': content,
    }
    resp = requests.post(base_url + 'blog/create-post/', json=data, headers=headers)
    print(resp.json(), resp.status_code)


#Read
def read(post_id):
    resp = requests.get(base_url + f'blog/posts/{post_id}/comments/', headers=headers)
    print(resp.json())

#Update
def update(post_id, field_name, field_value):
    data = {
        field_name: field_value
    }
    resp = requests.patch(base_url + f'update-blogpost/{post_id}/', json=data, headers=headers)
    print(resp.status_code, resp.json())

#Delete
def delete(post_id):
    resp = requests.delete(base_url + f'delete-blogpost/{post_id}/', headers=headers)
    print(resp.status_code, resp.json())


def comments(post_id, commenter, comment):
    data = {
        'comment': comment,
        'commenter': commenter
    }
    resp = requests.post(base_url + f'blog/posts/{post_id}/comments/', headers=headers, json=data)
    print(resp.json(), resp.status_code)


# resp = requests.get('http://localhost:8000/blog/posts/1/')
# print(resp.json(), resp.status_code)

login('ChiedozieEhirim', 'Mmaduakolam_1996')

#profile_view()

#create('Igbo Proverb', 'Egbe bere, Ugo bere, nke si ibe ya ebela, nku kwapu ya n\'ike.')

#read(2)

#update(2, 'title', 'Job Seeker')

#delete(2)

#comments(3, 'Akpabu Caleb', 'Iseeeeeee !!!')