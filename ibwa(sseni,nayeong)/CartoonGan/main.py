# -*- coding: utf-8 -*-

from CartoonGan.cartoon import MODEL_ROOT
from CartoonGan.cartoon.models import cartoon_generator
from CartoonGan.cartoon.utils import postprocess
from CartoonGan.cartoon.utils import load_net_in
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse


def main():

    INPUT_IMG_FNAME = "static/images/b_iu.jpg"
    
    save_file = "static/images/b_iu_cartoongan.jpg"
    INPUT_SIZE = 512

    # argparser = argparse.ArgumentParser(description='CartoonGan')
    # argparser.add_argument(
    #     '-i',
    #     '--input_img_fname',
    #     default=INPUT_IMG_FNAME,
    #     help='input image filename')
    # argparser.add_argument(
    #     '-s',
    #     '--input_size',
    #     default=INPUT_SIZE,
    #     help='generator network input size')


    # args = argparser.parse_args()
    model_names = ["CartoonGan/params/Hayao.h5", "CartoonGan/params/Hosoda.h5", "CartoonGan/params/Paprika.h5", "CartoonGan/Params/Shinkai.h5"]
    model = cartoon_generator(input_size=INPUT_SIZE)

    for j, model_path in enumerate(model_names):
        model.load_weights(model_path)
   
        imgs = np.expand_dims(load_net_in(INPUT_IMG_FNAME, desired_size=INPUT_SIZE), axis=0)
        ys = model.predict(imgs)
        y = postprocess(ys)[0]
        y = cv2.cvtColor(y, cv2.COLOR_BGR2RGB)
        y = cv2.normalize(y, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        tmp = "static/images/b_iu_cartoongan" + str(j) + ".jpg"

        cv2.imwrite(tmp, y)

    return y

    # for j, model_path in enumerate(model_names):
    #     model.load_weights(model_path)

    #     imgs = np.expand_dims(load_net_in(args.input_img_fname, desired_size=args.input_size), axis=0)
    #     ys = model.predict(imgs)
    #     y = postprocess(ys)[0]

    #     save_file = "sjtu" + str(j) + ".jpg"
    #     y = cv2.cvtColor(y, cv2.COLOR_BGR2RGB)

    #     cv2.imwrite(save_file, y)
    #     # cv2.imshow("y", y)
    #     cv2.waitKey(0)



if __name__ == '__main__':
    main()

# def main():

#     INPUT_IMG_FNAME = "static/images/b_iu.jpg"
#     save_file = "static/images/b_iu_cartoongan.jpg"

#     INPUT_SIZE = 512

#     argparser = argparse.ArgumentParser(description='CartoonGan')
#     argparser.add_argument(
#         '-i',
#         '--input_img_fname',
#         default=INPUT_IMG_FNAME,
#         help='input image filename')
#     argparser.add_argument(
#         '-s',
#         '--input_size',
#         default=INPUT_SIZE,
#         help='generator network input size')

#     args = argparser.parse_args()
#     model_names = ["params/Hayao.h5", "params/Hosoda.h5", "params/Paprika.h5", "params/Shinkai.h5"]
#     model = cartoon_generator(input_size=args.input_size)

#     model.load_weights(model_names[0])

#     imgs = np.expand_dims(load_net_in(args.input_img_fname, desired_size=args.input_size), axis=0)
#     ys = model.predict(imgs)
#     y = postprocess(ys)[0]

#     cv2.imwrite(save_file, y)

#     return y



# if __name__ == '__main__':
#     main()
    
