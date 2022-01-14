# RobotPackage

## Installation

Before starting, make sure to remove `franka_description` and `panda_moveit_config` pkg, if it exists.

## Usage

### task knowledge ~ task planning

1. convert original files(=v1) into v2 files in `test_set` folder
```
rosrun panda_move make_csv_v2.py
```
NOTE: v2 file includes additional infos

2. run main file for task planning
```
rosrun panda_move main.py tp
```
NOTE: task knowledge file should be in form of v2

### full sequence
```
rosrun panda_move main.py
```
NOTE: task knowledge file should be in form of v2