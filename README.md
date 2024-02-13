# cmd_vel_pubsub

[ROS 2入門セミナー](https://rt-net.jp/service/ros2seminar2024/)に使用するROS 2のサンプルパッケージです。

## 動作環境

- Linux OS
  - Ubuntu 22.04
- ROS
  - [Humble Hawksbill](https://docs.ros.org/en/humble/Installation.html)

## インストール方法

下記のコマンドを順に実行してください。

```sh
# Setup ROS environment
source /opt/ros/humble/setup.bash

# Download cmd_vel_pubsub repositories
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/rt-education/cmd_vel_pubsub.git

# Install dependencies
rosdep install -r -y -i --from-paths .

# Build & Install
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```

## 動作方法

### talkerとlistenerの実行

```sh
# 1つめのターミナル
source ~/ros2_ws/install/setup.bash
ros2 run demo_nodes_cpp talker

# 2つめのターミナル
source ~/ros2_ws/install/setup.bash
ros2 run demo_nodes_cpp listener

# Press [Ctrl-c] to terminate.
```

### cmd_vel_talkerの実行

```sh
source ~/ros2_ws/install/setup.bash
ros2 run cmd_vel_pubsub cmd_vel_talker

# Press [Ctrl-c] to terminate.
```

## ライセンス

(C) 2024 RT Corporation \<support@rt-net.jp\>

各ファイルはライセンスがファイル中に明記されている場合、そのライセンスに従います。
特に明記されていない場合は、Apache License, Version 2.0に基づき公開されています。  
ライセンスの全文は[LICENSE](./LICENSE)または[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)から確認できます。

## 謝辞
以下のリポジトリのファイルをベースに作成されています。

* [ros2/examples at humble](https://github.com/ros2/examples/tree/humble)
  *  Copyright 2016 Open Source Robotics Foundation, Inc.
  * [Apache - 2.0 License](https://github.com/ros2/examples/blob/humble/LICENSE)