'''city='Bhopal'
print(city[0])
print(city[2])

print(city[-1])
print(city[5])

print(city[-3])
print(city[3])

name='Priya Sharma'
print(name[0:5])
print(name[6:])
print(name[:5])
print(name[::2])
print(name[::-1])

print(len(name))

text='  Hello Python World  '
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.strip())

print('python' in text)
print(text.find('Python'))
print(text.count('l'))

print(text.replace('Python','AI'))

csv='Rahul , 22 , Bhopal , Engineer'
parts=csv.split(',')
print(parts)
print(parts[0])
rejoined='|'.join(parts)
print(rejoined)

print('hello123'.isalnum())
print('12345'.isdigit())
print('Python'.isalpha())
print(' '.isspace())

email='student@gmail.com'
print(email.endswith('.com'))
print(email.startswith('stu'))

name,marks,rank='Anita',97.78,3
print(f'Hello , {name}!')
print(f'marks: {marks:.2f}')
print(f'marks: {marks:.0f}')
print(f'count: {1000000:,}')

print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')
print(f'hello {name:^10}')
print(f'hello {name:>10}')
print(f'hello {name:<10}')
# print(f'hello {name:*10}')
price,gst=500,0.18
print(f'price:Rs.{price}|gst:Rs.{price*gst:.2f}|total:Rs.{price*(1+gst):.2f}')
'''
string="Hello,How are you doing today"
vovels='a','e','i','o','u'
count=0
for i in string:
    if i in vovels:
        count += 1
print(count)
print(string[14:17])
print(string[::-1])
