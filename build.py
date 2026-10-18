# Rebuilds index.html from src/template.html + src/data.json
t=open('src/template.html').read(); d=open('src/data.json').read()
open('index.html','w').write(t.replace('/*DATA*/',d))
print('built index.html',len(t)+len(d),'bytes')
