import os.path
from removebg import RemoveBg
from PIL import Image
import shutil

init_folder = 'C://李小蓉//外观//222'
cut_folder = init_folder + "//" + 'cut_img'
save_img_folder = init_folder + "//" + "matting"

# 抠图需要调用的库
rmbg = RemoveBg('e5toRpfFsqdo2tzrSoFqpAWY','error.log')

files = os.listdir(cut_folder)
for i,file in enumerate(files):
    img_path = cut_folder + "//" + file
    rmbg.remove_background_from_img_file(img_path)

    rmbg_save_name = file + "_no_bg.png"
    init_file = cut_folder + "//" + rmbg_save_name
    save_img_path = save_img_folder + "//" + file.split('.')[0] + '.png'

    shutil.move(init_file,save_img_path)
    print(i)








# for i in range(60):
#     save_img_path = 'C://李小蓉//外观//222//cut_img//' + str(i) + ".png"
#
#
#     rmbg.remove_background_from_img_file(save_img_path)
#
#     rmbg_name = save_img_path.split('//')[-1]
#     save_rmbg_name = 'C://李小蓉//外观//222//cut_img//' + rmbg_name + '_no_bg.png'
#
#
#     img = Image.open(save_img_path)
#
#
#





# color = (255,255,255)
# no_bg_image = Image.open('C://李小蓉//外观//222//cut_img//aa.png_no_bg.png')
# x, y = no_bg_image.size
# new_image = Image.new('RGBA', no_bg_image.size, color=color)
# new_image.paste(no_bg_image, (0, 0, x, y), no_bg_image)
# new_image.save('C://李小蓉//外观//222//cut_img//aa_white.png')
# a = 1