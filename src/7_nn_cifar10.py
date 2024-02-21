import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter


class Yang(nn.Module):

    def __init__(self,):
        super().__init__()

        # self.conv1 = nn.Conv2d(3, 32, 5, 1, 2)
        # self.maxpool1 = nn.MaxPool2d(2)
        # self.conv2 = nn.Conv2d(32, 32, 5, padding=2)
        # self.maxpool2 = nn.MaxPool2d(2)
        # self.conv3 = nn.Conv2d(32, 64, 5, padding=2)
        # self.maxpool3 = nn.MaxPool2d(2)
        # self.flatten = nn.Flatten()
        # self.linear1 = nn.Linear(1024, 64)
        # self.linear2 = nn.Linear(64, 10)

        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, padding=2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        # x = self.conv1(x)
        # x = self.maxpool1(x)
        # x = self.conv2(x)
        # x = self.maxpool2(x)
        # x = self.conv3(x)
        # x = self.maxpool3(x)
        # x = self.flatten(x)
        # x = self.linear1(x)
        # x = self.linear2(x)
        return self.model(x)


yang = Yang()
print(yang)

input = torch.ones(64, 3, 32, 32)
output = yang(input)
print(output.shape)

writer = SummaryWriter("../logs")
writer.add_graph(yang, input)
writer.close()