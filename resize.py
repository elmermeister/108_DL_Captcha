
import os
from PIL import Image 


bgfold='captcha bg'
bglist=os.listdir(bgfold)
savedir='resize/'
if not os.path.isdir(savedir):
    os.mkdir(savedir)

for num,i in enumerate(bglist):
    bg=os.path.join(bgfold,i)
    im= Image.open(bg)
    im=im.resize((200,60))
    im.save(savedir+str('resize%03d'%num)+'.jpg')
#     im.save(testpath+str("bg_test_%06d"%i)+'.jpg')