ay,ax,by,bx = map(int,input().split())
n,m,l = map(int,input().split())
adir=[]; amov=[]; bdir=[]; bmov=[]
for i in range(m):
	x,y=input().split()
	adir.append(x)
	amov.append(int(y))
for i in range(l):
	x,y=input().split()
	bdir.append(x)
	bmov.append(int(y))

adir.append(0); amov.append(0)
bdir.append(0); bmov.append(0)

a=[]; b=[]; mov=[]
adex=0; bdex=0
while adex!=m or bdex!=l:
	a.append(adir[adex])
	b.append(bdir[bdex])

	if amov[adex]<bmov[bdex]:
		mov.append(amov[adex])
		bmov[bdex]-=amov[adex]
		adex+=1
	elif amov[adex]>bmov[bdex]:
		mov.append(bmov[bdex])
		amov[adex]-=bmov[bdex]
		bdex+=1
	else:
		mov.append(bmov[bdex])
		adex+=1
		bdex+=1

ans=0

for i in range(len(mov)):
	aycp=ay; axcp=ax; bycp=by; bxcp=bx

	if a[i]=='U':
		ay-=mov[i]
	if a[i]=='D':
		ay+=mov[i]
	if a[i]=='L':
		ax-=mov[i]
	if a[i]=='R':
		ax+=mov[i]

	if b[i]=='U':
		by-=mov[i]
	if b[i]=='D':
		by+=mov[i]
	if b[i]=='L':
		bx-=mov[i]
	if b[i]=='R':
		bx+=mov[i]
	"""
	if (aycp<by<ay or aycp>by>ay) and (bxcp<ax<by or bxcp>ax>by):
		if abs(aycp-by)==abs(bxcp-ax):
			ans+=1
	if (bycp<ay<by or bycp>ay>by) and (axcp<bx<ay or axcp>bx>ay):
		if abs(bycp-ay)==abs(axcp-bx):
			ans+=1
	"""	
	if axcp==ax==bxcp==bx and abs(aycp-bycp)%2==0:
		if (aycp<bycp and ay>by) or (aycp>bycp and ay<by):
			ans+=1
	if aycp==ay==bycp==by and abs(axcp-bxcp)%2==0:
		if (axcp<bxcp and ax>bx) or (axcp>bxcp and ax<bx):
			ans+=1

	if ay==by and ax==bx:
		if axcp==bxcp and aycp==bycp:
			ans+=mov[i]
		else:
			ans+=1

print(ans)