from sys import argv

script, filename=argv

txt_open=open(filename)
opened=txt_open.read()
print(opened)