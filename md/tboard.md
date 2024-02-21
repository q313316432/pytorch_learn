SummaryWriter 类完成写log的作用

```python
from torch.utils.tensorboard import SummaryWriter

 # create a summary writer with automatically generated folder name.
 writer = SummaryWriter()
 # folder location: runs/May04_22-14-54_s-MacBook-Pro.local/

 # create a summary writer using the specified folder name.
 writer = SummaryWriter("my_experiment")
 # folder location: my_experiment

 # create a summary writer with comment appended.
 writer = SummaryWriter(comment="LR_0.1_BATCH_16")
 # folder location: runs/May04_22-14-54_s-MacBook-Pro.localLR_0.1_BATCH_16/

 writer.close() # 需要关闭
```

add_scalar
```python
def add_scalar(
        self,
        tag,
        scalar_value,
        global_step=None,
        walltime=None,
        new_style=False,
        double_precision=False,
    ):
# Add scalar data to summary.
# 
# Args:
#     tag (str): Data identifier
#     scalar_value (float or string/blobname): Value to save  这里代表X轴
#     global_step (int): Global step value to record   这里代表Y轴
#     walltime (float): Optional override default walltime (time.time())
#       with seconds after epoch of event
#     new_style (boolean): Whether to use new style (tensor field) or old
#       style (simple_value field). New style could lead to faster data loading.
# Examples::
# 
#     from torch.utils.tensorboard import SummaryWriter
#     writer = SummaryWriter()
#     x = range(100)
#     for i in x:
#         writer.add_scalar('y=2x', i * 2, i)
#     writer.close()
# 
# Expected result:
# 
# .. image:: _static/img/tensorboard/add_scalar.png
#    :scale: 50 %

```

pip install tensorboard

tensorboard --logdir=logs 指定路径


图像

```python
from torchvision import transforms
to_tensor = transforms.ToTensor()
```

transforms.ToTensor()用来创建工具

### openCV方式打开
```shell
pip install opencv-python
```

```python
import cv2
cv_img = cv2.imread(img_path)
```

## Transforms
transforms.compose 将不同的transform组合

__call__的用法
```python
class Person:
    def __call__(self, name):
        print("123")

a = Person()
a("123")
```

ToTensor 将PIL or ndarray 转化为Tensor


Normalize 归一化
