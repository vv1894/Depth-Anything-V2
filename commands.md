run on different images
python run.py --encoder vits --img-path assets/examples_1 --outdir depth_vis

python metric_depth/depth_to_pointcloud.py --encoder vitb --load-from checkpoints/depth_anything_v2_vitb.pth --max-depth 20 --img-path assets/examples_2/demo01.jpg --outdir depth_pcd

python depth_to_pointcloud.py \
  --encoder vitb \
  --load-from checkpoints/depth_anything_v2_metric_hypersim_vitb.pth \
  --max-depth 80 \
  --img-path assets/examples_2/demo01.jpg --outdir depth_pcd

# test_indoor
python run.py \
  --encoder vitb \
  --load-from checkpoints/depth_anything_v2_metric_hypersim_vitb.pth \
  --max-depth 20 \
  --img-path assets/examples_2/demo01.jpg --outdir depth_test

# test_outdoor
python run.py \
  --encoder vitb \
  --load-from checkpoints/depth_anything_v2_metric_vkitti_vitb.pth \
  --max-depth 80 \
  --img-path assets/examples_2/demo01.jpg --outdir depth_test

# generate pcd
python run.py \
  --encoder vits \
  --img-path assets/cus_exp \
  --outdir /media/ryan/ldata/rhino_res/depth_anything_firstrun

# prepare new kitti dataset
python run_kitti.py \
  --encoder vitb \
  --img-path dataload/train_files.txt \
  --img-dir /media/ryan/ldata/monodepth2/kitti_data \
  --outdir /media/ryan/ldata/eigen_zhou/kitti_data \
  --pred-only

python run_kitti.py \
  --encoder vitb \
  --img-path dataload/val_files.txt \
  --img-dir /media/ryan/ldata/monodepth2/kitti_data \
  --outdir /media/ryan/ldata/eigen_zhou/kitti_data \
  --pred-only