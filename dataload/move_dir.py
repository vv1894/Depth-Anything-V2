import shutil
import os

src_dir = '/media/ryan/ldata/monodepth2/kitti_data'
dest_dir = '/media/ryan/ldata/eigen_zhou/kitti_data'
cp_dir = ['/oxts', '/velodyne_points']

with open('unique_directories.txt', 'r') as f:
    lines = f.read().splitlines()
    for dir in lines:
        for cp in cp_dir:
            ori = src_dir + '/' + dir + cp
            tar = dest_dir + '/' + dir
            print(f'ori:{ori}')
            print(f'tar:{tar}')
            if os.path.exists(ori):
                if not os.path.exists(tar):
                    os.makedirs(tar)
            tar = tar + cp
            # 使用 copytree 函数拷贝目录
            try:
                shutil.copytree(ori, tar)
                print(f"Directory '{ori}' has been copied to '{tar}'")
            except shutil.Error as e:
                print(f"Error: {e}")
