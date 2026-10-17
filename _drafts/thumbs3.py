import math, os
from PIL import Image, ImageDraw, ImageFont
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1200,630
NOTO='C:/Windows/Fonts/NotoSansKR-VF.ttf'; EMO='C:/Windows/Fonts/seguiemj.ttf'
def F(size,w=900):
    f=ImageFont.truetype(NOTO,size); f.set_variation_by_axes([w]); return f
def E(size): return ImageFont.truetype(EMO,size)
def txt(d,xy,s,font,fill,stroke=0,sf='black',anchor='la'):
    d.text(xy,s,font=font,fill=fill,stroke_width=stroke,stroke_fill=sf,anchor=anchor)
def emoji(img,xy,s,size,anchor='mm'):
    ImageDraw.Draw(img).text(xy,s,font=E(size),embedded_color=True,anchor=anchor)
def grad(c1,c2,horizontal=False):
    g=Image.new('RGB',(W,H)); d=ImageDraw.Draw(g); n=W if horizontal else H
    for i in range(n):
        t=i/(n-1); c=tuple(int(c1[k]+(c2[k]-c1[k])*t) for k in range(3))
        d.line([(i,0),(i,H)] if horizontal else [(0,i),(W,i)],fill=c)
    return g
def rays(img,center,color,n=24,alpha=40):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov); cx,cy=center
    for i in range(0,n,2):
        a1=2*math.pi*i/n; a2=2*math.pi*(i+1)/n; R=1500
        d.polygon([(cx,cy),(cx+R*math.cos(a1),cy+R*math.sin(a1)),(cx+R*math.cos(a2),cy+R*math.sin(a2))],fill=color+(alpha,))
    img.alpha_composite(ov)

# ---------- A: VS battle ----------
img=grad((90,10,20),(15,5,30)).convert('RGBA')
rays(img,(600,360),(255,200,60),alpha=28)
d=ImageDraw.Draw(img)
txt(d,(600,150),'작은 놈이 이겼다?!',F(84),'#ffe14d',stroke=10,anchor='mm')
d.rounded_rectangle([70,215,500,525],28,fill='#3b3f4a',outline='#9aa0aa',width=6)
txt(d,(285,315),'122B',F(120),'#d6d9de',stroke=6,anchor='mm')
txt(d,(285,405),'거대 모델',F(40,700),'#9aa0aa',anchor='mm')
txt(d,(285,470),'0.949',F(56),'#ffffff',stroke=5,anchor='mm')
emoji(img,(105,235),'😵',80)
d=ImageDraw.Draw(img)
d.rounded_rectangle([760,275,1110,525],28,fill='#ffd21f',outline='#ffffff',width=8)
txt(d,(935,355),'35B',F(100),'#1a1a1a',anchor='mm')
txt(d,(935,425),'+ 돋보기',F(40,800),'#1a1a1a',anchor='mm')
txt(d,(935,482),'0.9655',F(54),'#d7191c',anchor='mm')
emoji(img,(1095,280),'🔍',90)
emoji(img,(935,250),'👑',70)
d=ImageDraw.Draw(img)
txt(d,(630,380),'VS',F(120),'#ff3b3b',stroke=10,sf='white',anchor='mm')
txt(d,(600,600),'SSAFY 16기 AI 챌린지 회고',F(26,700),'#ffffff',anchor='mm')
img.convert('RGB').save('thumb_A.png')

# ---------- B: warning ----------
img=Image.new('RGBA',(W,H),'#ffd400'); d=ImageDraw.Draw(img)
for band in (0,H-60):
    for x in range(-60,W+60,60):
        d.polygon([(x,band),(x+30,band),(x+90,band+60),(x+60,band+60)],fill='#111')
txt(d,(600,118),'⚠ 잠깐!',F(54),'#111',anchor='mm')
txt(d,(540,245),'모델 키우지',F(140),'#e10600',stroke=12,sf='#111',anchor='mm')
txt(d,(540,400),'마세요',F(140),'#e10600',stroke=12,sf='#111',anchor='mm')
emoji(img,(1040,320),'✋',190)
d=ImageDraw.Draw(img)
d.rounded_rectangle([150,470,1050,545],38,fill='#111')
txt(d,(600,507),'3배 키웠는데 +0.45%p … 진짜 범인은 따로 있었다',F(36,800),'#ffffff',anchor='mm')
st=Image.new('RGBA',(300,120),(0,0,0,0)); sd=ImageDraw.Draw(st)
sd.rounded_rectangle([6,6,294,114],16,outline='#e10600',width=8)
txt(sd,(150,60),'실화임',F(62),'#e10600',anchor='mm')
st=st.rotate(-14,expand=True,resample=Image.BICUBIC)
img.alpha_composite(st,(880,60))
img.convert('RGB').save('thumb_B.png')

# ---------- C: zoom reveal ----------
img=grad((10,25,60),(5,10,25),horizontal=True).convert('RGBA')
rays(img,(900,330),(120,200,255),alpha=22)
d=ImageDraw.Draw(img)
txt(d,(650,150),'이거 하나로 +2.1%p',F(76),'#ffffff',stroke=9,sf='#000',anchor='mm')
d.rounded_rectangle([70,215,470,480],18,fill='#1d2433',outline='#5b6b8a',width=5)
small=Image.new('RGB',(160,60),'#0b1220'); sd=ImageDraw.Draw(small)
sd.text((80,18),'00:30 1,000원',font=F(18,700),fill='#cfe3ff',anchor='mm')
sd.text((80,44),'01:00 1,800원',font=F(18,700),fill='#cfe3ff',anchor='mm')
img.paste(small.resize((40,15),Image.BILINEAR).resize((340,128),Image.NEAREST),(100,262))
d=ImageDraw.Draw(img)
txt(d,(270,440),'원본: ???',F(36,800),'#9fb3d1',anchor='mm')
d.ellipse([85,245,455,405],outline='#ff2e2e',width=8)
d.line([(480,345),(640,345)],fill='#ff2e2e',width=18)
d.polygon([(640,310),(700,345),(640,380)],fill='#ff2e2e')
cx,cy,r=900,355,150
d.ellipse([cx-r,cy-r,cx+r,cy+r],fill='#fffdf2',outline='#ffd21f',width=20)
d.line([(cx+108,cy+108),(cx+190,cy+190)],fill='#ffd21f',width=40)
txt(d,(cx,cy-40),'00:30',F(72),'#111',anchor='mm')
txt(d,(cx,cy+50),'1,000원',F(62),'#e10600',anchor='mm')
emoji(img,(185,148),'😱',90)
d=ImageDraw.Draw(img)
d.rounded_rectangle([280,540,920,600],32,fill='#ffd21f')
txt(d,(600,570),'추가 학습 0 · 같은 35B · 사진만 확대',F(32,800),'#111',anchor='mm')
img.convert('RGB').save('thumb_C.png')

# contact sheet with hub-card crop preview (hub card ~2.67:1, center crop)
sheet=Image.new('RGB',(1260,3*370+20),'#ffffff'); sd=ImageDraw.Draw(sheet)
ch=int(W/2.67)
for i,n in enumerate('ABC'):
    im=Image.open(f'thumb_{n}.png'); y=20+i*370
    sheet.paste(im.resize((600,315)),(20,y))
    sheet.paste(im.crop((0,(H-ch)//2,W,(H+ch)//2)).resize((600,225)),(640,y+45))
    sd.text((20,y+320),f'{n}안 — 원본',font=F(20,800),fill='#222')
    sd.text((640,y+275),'허브 카드에서 보이는 영역 (가운데 크롭)',font=F(20,700),fill='#555')
sheet.save('thumb_candidates.png')
