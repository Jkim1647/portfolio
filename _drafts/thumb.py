from PIL import Image, ImageDraw, ImageFont
W,H=1200,630
S=2
img=Image.new('RGB',(W*S,H*S),'#0f172a'); d=ImageDraw.Draw(img)
B='C:/Windows/Fonts/malgunbd.ttf'; R='C:/Windows/Fonts/malgun.ttf'
f=lambda p,s: ImageFont.truetype(p,s*S)
def t(xy,s,font,fill): d.text((xy[0]*S,xy[1]*S),s,font=font,fill=fill)
def rr(box,r,fill=None,outline=None,w=1): d.rounded_rectangle([v*S for v in box],r*S,fill=fill,outline=outline,width=w*S)
# subtle grid
for x in range(0,W,40): d.line([(x*S,0),(x*S,H*S)],fill='#131c33',width=S)
for y in range(0,H,40): d.line([(0,y*S),(W*S,y*S)],fill='#131c33',width=S)
# badge
rr((64,60,410,104),22,fill='#1e293b',outline='#334155',w=2)
t((86,66),'SSAFY 16기 · AI 챌린지 회고',f(B,22),'#93c5fd')
# headline
t((64,140),'모델을 3배 키웠는데',f(B,64),'#f8fafc')
t((64,224),'점수가 안 올랐다',f(B,64),'#f8fafc')
t((64,322),'그래서 모델 대신 ',f(R,32),'#cbd5e1')
w=d.textlength('그래서 모델 대신 ',font=f(R,32))/S
t((64+w,318),'돋보기',f(B,36),'#facc15')
w2=d.textlength('돋보기',font=f(B,36))/S
t((64+w+w2,322),'를 쥐여줬다',f(R,32),'#cbd5e1')
# bars
rows=[('9B · 원본',0.943,'#475569','#cbd5e1'),('122B · 원본',0.949,'#64748b','#cbd5e1'),('35B · 확대+받아적기',0.9655,'#facc15','#facc15')]
x0,y0,bw=64,410,430
lo,hi=0.93,0.97
for i,(lab,v,c,tc) in enumerate(rows):
    y=y0+i*62
    t((x0,y),lab,f(B if i==2 else R,22),tc)
    L=bw*(v-lo)/(hi-lo)
    rr((x0+240,y+4,x0+240+L,y+34),8,fill=c)
    t((x0+240+L+12,y+2),f'{v:.4f}'.rstrip('0'),f(B,24),tc)
# magnifier
cx,cy,r=1000,250,120
d.ellipse([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S],outline='#facc15',width=18*S,fill='#111c35')
d.line([((cx+85)*S,(cy+85)*S),((cx+175)*S,(cy+175)*S)],fill='#facc15',width=34*S)
t((cx-68,cy-50),'00:30',f(B,48),'#f8fafc')
t((cx-74,cy+8),'1,000원',f(B,40),'#facc15')

# result line
t((x0,y0-0+186),'검증셋 667문제 정확도',f(R,18),'#64748b')
rr((800,470,1136,560),16,fill='#052e1a',outline='#166534',w=2)
t((826,480),'+2.1%p',f(B,40),'#86efac')
t((990,494),'추가 학습 0',f(R,20),'#86efac')
t((826,530),'Public 11위 / 217팀',f(B,20),'#bbf7d0')
img=img.resize((W,H),Image.LANCZOS); img.save('thumbnail.png',optimize=True)
