# Captcha 



>  **此為108學年度深度學習程式設計期末專題資料集生成程式碼**



#### Run:

```
python main.py --savepath="savepath/" --sample_num=1000 --val_size=0.1 --test_size=0.1 --method=0
```



#### Size :

width=200, length=60

Font_path="Fonts"

background_image_path="captcha bg"



#### method:

0:shift_code,![0_shift_code](https://github.com/masahiro1025/Captcha/blob/master/example_img\0_shift_code.jpg)

1:rotate_code,![1_rotate_code](https://github.com/masahiro1025/Captcha/blob/master/example_img\1_rotate_code.jpg)

2:gradient_shift_code,![2_gradient_shift_code](https://github.com/masahiro1025/Captcha/blob/master/example_img\2_gradient_shift_code.jpg)

3:bg_shift_code,![3_bg_shift_code](https://github.com/masahiro1025/Captcha/blob/master/example_img\3_bg_shift_code.jpg)

4:bg_rotate_noise_code,![4_bg_rotate_noise_code](https://github.com/masahiro1025/Captcha/blob/master/example_img\4_bg_rotate_noise_code.jpg)

