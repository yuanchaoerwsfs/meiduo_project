import yaml

file = open('config_yaml', 'r')
data = yaml.load(file)

slogan = ['welcome', 'to', '51zxw']
website = {'url': 'www.51zxw.net'}

print(data)

print(data['name'])
print(data['age'])

data['name'] = '51zxw'
print(data['name'])

print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'][0]['name'])
print(data['children'][0]['age'])
print(data['children'][1]['name'])
print(data['children'][1]['age'])


print(slogan)
print(website)

print(yaml.dump(slogan))
print(yaml.dump(website))