import os.path
from glob import glob
from tqdm import tqdm
import codecs
import argparse
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='trocr vocab生成')
    parser.add_argument('--cust_vocab', default="./cust-data/vocab.txt", type=str, help="自定义vocab文件生成")
    parser.add_argument('--dataset_path', default="./dataset/train/*/*.jpg", type=str, help="自定义训练数字符集")
    args = parser.parse_args()
    paths = glob(args.dataset_path)
    vocab =[]
    for p in tqdm(paths):
       with open(p,'r',encoding='utf-8') as f:
           label = f.readline().strip()
           for c in set(label):
               if c not in vocab:
                  vocab.append(c)

    root_path = os.path.split(args.cust_vocab)
    os.makedirs(root_path, exist_ok=True)
    with open(args.cust_vocab, 'w') as f:
        f.write('\n'.join(list(vocab)))





