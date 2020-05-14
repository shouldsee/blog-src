
# import sys;sys.path.append('/home/shouldsee/.local/lib/python3.7/site-packages')
from luck.shorts import LSC,TSSR,NCR,RNS,DNS,MFP
from luck.defer import str_expand
from luck.header import rstrip
import os
import jinja2
ns = RNS()
ctx = DNS()
p = DNS()

# ctx.BaseUrl = 'http://localhost:1313/blog'
# ctx.BaseUrl = 'http://localhost:8001/blog'
ctx.BaseUrl = "http://newflaw.com/blog/"
ctx.Port = '8000'
NCR.M(ns,'add_config',None,lambda c:
write_close(
'config.yaml',

f'''
baseURL: '{ctx.BaseUrl}'
languageCode: en-gb
title: Newflaw
theme: hyde
params:
  description: Nature is never flawless
menu:
  main:
    - name: About
      _pre: <i class='fa fa-heart'></i>
      url: /pages/0001_about/
      weight: -110
    - name: Posts
      _pre: <i class='fa fa-road'></i>
      url: /posts/
      weight: -100
    - name: Projects
      _pre: <i class='fa fa-road'></i>
      url: /projects/
      weight: -100
markup:
  goldmark:
    parser:
      attribute: true
      autoHeadingID: true
      autoHeadingIDType: github
    renderer:
      hardWraps: false
      unsafe: true
      xhtml: false

'''.encode()
))


# MFP.M(p, 'output/%.html')

import io
def read_close(fn,mode='rb'):
	with open(fn,mode) as f:
		return f.read()
def write_close(fn,buf,mode='wb'):
	with open(fn, mode ) as f:
		f.write(buf)

from path import Path
def yaml_src(c):
	od = Path(c.o[0]).makedirs_p()
	for html in c.i:
		of =  od / html.split('/',1)[1]
		of.dirname().makedirs_p()
		print(f'[yaml_src]{html}')
		LSC(f'html_to_yaml.py --from html {html} -o {of}')

# # TSSR.M(ns,'output_image/**.html')
src_files = str_expand('src/content/**.md')
# output_image/**.html')
for x in src_files.split():
	TSSR.M(ns, x)
src_outputs = []
for k in src_files.split():
	# print(k)
	# d = "content/"
	of =  k.split('/',1)[-1]
	# of = '%s/%s'%(d, k.split('/',1)[-1])
	TSSR.MWF(ns, of, k, lambda c: [
		print(c.i),
		LSC(f'ln -f {c.i[0]} {c.o[0]}'),
		# write_close(
		# 	c.o[0],
		# 	jinja2.Template(read_close(c.i[0],'r')).render(**dict(ctx=ctx))
		# 	.encode() 
		# 	),
		print(c.o),
		]
		)
	src_outputs.append(of)

NCR.M(ns, 'contents', ' '.join(src_outputs))
NCR.M(ns, 'build', 'contents add_theme add_config  bin/hugo', lambda c:LSC(f'''
	bin/hugo -b {ctx.BaseUrl}
	'''))

TSSR.M(ns, 'themes/hyde')
NCR.M(ns, 'add_theme', 'themes/hyde', lambda c: (LSC('''
git clone https://github.com/spf13/hyde.git themes/hyde 
''')if not os.path.isdir(c.i[0]) else None ))

TSSR.M(ns, 'bin/hugo',None,lambda c:LSC('''
	mkdir -p bin
curl -sL https://github.com/gohugoio/hugo/releases/download/v0.70.0/hugo_0.70.0_Linux-64bit.tar.gz | tar -xvzf- -C bin/
hugo version'''
	))
NCR.M(ns,'serve', 'build', lambda c:LSC(f'''
ln -sf public blog;
python3 -m http.server {ctx.Port}
	'''))


'''
# eval "$(curl -sL https://raw.githubusercontent.com/travis-ci/gimme/master/gimme | GIMME_GO_VERSION=1.14.2 bash)"
# go get github.com/gohugoio/hugo
'''

# # yaml_src_files = for k in yaml
# yaml_src_files  =[]
# for k in src_files.split():	
# 	of = 'yaml-src/%s'%(k.split('/',1)[-1])+'.yaml'
# 	TSSR.MWF(ns, of, k, 'html_to_yaml.py --from html {c.i[0]} -o {c.o[0]} || {{ subl {c.i[0]}; exit 1; }}')
# 	yaml_src_files.append(of)
# NCR.M(ns, 'yaml-src', ' '.join(yaml_src_files))


# yaml_output_files = []
# for k in yaml_src_files:
# 	of = 'yaml-output/%s'%(k.split('/',1)[-1])
# 	of = rstrip(of,'.yaml')
# 	TSSR.MWF(ns, of, k, 'html_to_yaml.py --from yaml {c.i[0]} -o {c.o[0]} || {{ subl {c.i[0]}; exit 1; }}')
# 	yaml_output_files.append(of)

# NCR.M(ns, 'yaml-output',' '.join(yaml_output_files))
	# LSC(f'html_to_yaml.py --from html {html} -o {of}'))
# TSSR.M(ns, yaml_src_files, yaml_src)
