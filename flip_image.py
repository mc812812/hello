from PIL import Image
 import matplotlib.pyplot as plt
 def flip_image_left_right(img):
     """
     输入图片对象，返回左右翻转后的图片
     """
     flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
     return flipped_img
 if __name__ == "__main__":
     # 测试图片，放到hello文件夹里，名字改成test.jpg
     original = Image.open("test.jpg")
     flipped = flip_image_left_right(original)
     # 并排显示原图 和 翻转图
     plt.subplot(1, 2, 1)
     plt.title("Original")
     plt.imshow(original)
     plt.axis("off")
     plt.subplot(1, 2, 2)
     plt.title("Flipped")
     plt.imshow(flipped)
     plt.axis("off")
     plt.show()