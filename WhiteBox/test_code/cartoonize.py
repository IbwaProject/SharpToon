import os
import cv2
import numpy as np
import tensorflow as tf 
from WhiteBox.test_code.network import resblock, unet_generator
from WhiteBox.test_code.guided_filter import guided_filter
from tqdm import tqdm



def resize_crop(image):
    h, w, c = np.shape(image)
    if min(h, w) > 720:
        if h > w:
            h, w = int(720*h/w), 720
        else:
            h, w = 720, int(720*w/h)
    image = cv2.resize(image, (w, h),
                       interpolation=cv2.INTER_AREA)
    h, w = (h//8)*8, (w//8)*8
    image = image[:h, :w, :]
    return image
    

def cartoonize():
    img = cv2.imread("static/images/input/imageTemp1.jpg")
    save_file = "static/images/b_iu_whitebox.jpg"
    model_path = 'WhiteBox/test_code/saved_models'
    # load_file = 'static/images/b_iu.jpg'
    # save_file = 'static/images/b_iu_whitebox.jpg'

    input_photo = tf.placeholder(tf.float32, [1, None, None, 3])
    network_out = unet_generator(input_photo)
    final_out = guided_filter(input_photo, network_out, r=1, eps=5e-3)

    all_vars = tf.trainable_variables()
    gene_vars = [var for var in all_vars if 'generator' in var.name]
    saver = tf.train.Saver(var_list=gene_vars)
    
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    sess.run(tf.global_variables_initializer())
    saver.restore(sess, tf.train.latest_checkpoint(model_path))
    # name_list = os.listdir(load_folder)
    image = resize_crop(img)
    batch_image = image.astype(np.float32)/127.5 - 1
    batch_image = np.expand_dims(batch_image, axis=0)
    output = sess.run(final_out, feed_dict={input_photo: batch_image})
    output = (np.squeeze(output)+1)*127.5
    output = np.clip(output, 0, 255).astype(np.uint8)
    cv2.imwrite(save_file, output)

    return output


if __name__ == '__main__':
    cartoonize()
    

    