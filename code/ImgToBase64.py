import base64
import argparse
import hashlib
import os

def parse_args():
    parse = argparse.ArgumentParser(description='图片转base64')
    parse.add_argument('img_path', help='图片路径')
    args = parse.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    pic = open(args.img_path, "rb")
    pic_base64 = base64.b64encode(pic.read()).decode("utf-8")
    pic.close()

    img_name = os.path.basename(args.img_path)
    
    # 将img_name转成哈希码
    hash_name = hashlib.md5(img_name.encode("utf-8")).hexdigest()

    if os.path.exists("pic_base64.txt"):
        os.remove("pic_base64.txt")
        
    with open("pic_base64.txt", "w") as f:
        f.write("![image][{}]".format(hash_name))
        f.write("\n"*3)
        f.write("[{}]:data:image/png;base64,{}".format(hash_name, pic_base64))
        




