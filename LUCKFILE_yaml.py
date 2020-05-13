
from luck.shorts import LSC,TSSR,NCR,RNS,DNS,MFP
from luck.defer import str_expand
from luck.header import rstrip
ns = RNS()
p = DNS()

# MFP.M(p, 'output/%.html')

from path import Path
def yaml_src(c):
	od = Path(c.o[0]).makedirs_p()
	for html in c.i:
		of =  od / html.split('/',1)[1]
		of.dirname().makedirs_p()
		print(f'[yaml_src]{html}')
		LSC(f'html_to_yaml.py --from html {html} -o {of}')
		# with open(of,'w') as f:
		# 	with open(html,'r') as fi:
		# 		LSC(f'html_to_yaml.py {}')
		# 		buf = fi.read()
		# 		f.write()
		# o = c.
	pass
# TSSR.M(ns,'output_image/**.html')
src_files = str_expand('output_image/**.html')
for x in src_files.split():
	TSSR.M(ns, x)
# yaml_src_files = for k in yaml
yaml_src_files  =[]
for k in src_files.split():	
	of = 'yaml-src/%s'%(k.split('/',1)[-1])+'.yaml'
	TSSR.MWF(ns, of, k, 'html_to_yaml.py --from html {c.i[0]} -o {c.o[0]} || {{ subl {c.i[0]}; exit 1; }}')
	yaml_src_files.append(of)
NCR.M(ns, 'yaml-src', ' '.join(yaml_src_files))


yaml_output_files = []
for k in yaml_src_files:
	of = 'yaml-output/%s'%(k.split('/',1)[-1])
	of = rstrip(of,'.yaml')
	TSSR.MWF(ns, of, k, 'html_to_yaml.py --from yaml {c.i[0]} -o {c.o[0]} || {{ subl {c.i[0]}; exit 1; }}')
	yaml_output_files.append(of)

NCR.M(ns, 'yaml-output',' '.join(yaml_output_files))
	# LSC(f'html_to_yaml.py --from html {html} -o {of}'))
# TSSR.M(ns, yaml_src_files, yaml_src)
