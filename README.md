# TP-SRL-Habitat-Rearrange-Challenge-2022-Study
This is a small work on testing and studing the method of Task Planning and Skills RL (TP-SRL) method on the long horizon mobile manipulation task on Habitat Rearrange Challenge 2022, and mainly tested and studied on the easy task. The work is inspired and learned from the [facebookresearch/habitat-challenge/rearrange-challenge-2022](https://github.com/facebookresearch/habitat-challenge/tree/rearrangement-challenge-2022).

# Task: Object Rearrangement
In the object rearrangement task, a Fetch robot is randomly spawned in an unknown environment and asked to rearrange 1 object from an initial to desired position – picking/placing it from receptacles (counter, sink, sofa, table), opening/closing containers (drawers, fridges) as necessary. A map of the environment is not provided and the agent must only use its sensory input to navigate and rearrange.

The Fetch robot is equipped with an egocentric 256x256 90-degree FoV RGBD camera on the robot head. 
The agent also has access to idealized base-egomotion giving the relative displacement and angle of the base since the start of the episode. 
Additionally, the robot has proprioceptive joint sensing providing access to the current robot joint angles.

For details about the agent, dataset, and evaluation, see the challenge website: [aihabitat.org/challenge/2022_rearrange](https://aihabitat.org/challenge/2022_rearrange/).

# Preparation
## Hardware Configuration
This small work is trained on:
(1) CPU: I7 8700
(2) GPU: Nvidia GeForce GTX 1060 6GB

## Environment Configuration
You may use conda to create a environment
(1) Python: 3.7.12
(2) Pytorch: 1.13.1
(3) Cuda: 11.7
(4) Cudnn: 8.6.0

## Installing Habitat-Sim and Downloading data
First setup Habitat Sim in a new conda environment so you can download the datasets to evaluate your models locally

1. Prepare your [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) env:
    ```bash
    # python>=3.7 and cmake>=3.10
    conda create -n habitat python=3.7 cmake=3.14.0
    conda activate habitat
    ```

1. Install Habitat-Sim using our custom Conda package for habitat challenge 2022 with: 
    ```
    conda install -y habitat-sim-rearrange-challenge-2022  withbullet  headless -c conda-forge -c aihabitat
    ```
    **On MacOS, omit the `headless` argument**.    
    Note: If you face any issues related to the `GLIBCXX` version after conda installation, please uninstall this conda package and install the habitat-sim repository from source (more information [here](https://github.com/facebookresearch/habitat-sim/blob/main/BUILD_FROM_SOURCE.md#build-from-source)). Make sure that you are using the `hab2_challenge_2022` tag and not the `stable` branch for your installation. 

1. Clone the challenge repository:

    ```bash
    git clone -b rearrangement-challenge-2022 https://github.com/facebookresearch/habitat-challenge.git
    cd habitat-challenge
    ```

1. Download the episode datasets, scenes, and all other assets with 
    ```
    python -m habitat_sim.utils.datasets_download --uids rearrange_task_assets --data-path <path to download folder>
    ```
    If this step was successful, you should see the train, val and minival splits in the `<path to download folder>/datasets/replica_cad/rearrange/v1/{train, val, minival}` folders respectively. 

1. Now, create a symlink to the downloaded data in your habitat-challenge repository:
    ```
    ln -s <absolute path to download folder> data
    ```
1. Replace the config file in from the repository

1. Model could be download at [models](https://drive.google.com/drive/folders/1g1CKh_uclKiFxCiL59F3lBRxiyXtT8kF)

# TP-SRL
Train individual skill policies with RL, and evaluate with the 'rearrange_easy' task
1. Install [Habitat-Lab](https://github.com/facebookresearch/habitat-lab/) - Use the `rearrange_challenge_2022` branch in our Github repo, which can be cloned using: 
    ```
    git clone --branch rearrange_challenge_2022 https://github.com/facebookresearch/habitat-lab.git
    ``` 
    Install Habitat Lab along with the included RL trainer code by first entering the `habitat-lab` directory, activating the `habitat` conda environment from step 1, and then running `pip install -r requirements.txt && python setup.py develop --all`.
(It is recomended that habitat lab should be put in the same directory with habitat-challenge)
1. Steps to train the skills from scratch:

    1. Train the Pick skill. From the Habitat Lab directory, run 
    ```bash
    python habitat_baselines/run.py \
        --exp-config habitat_baselines/config/rearrange/ddppo_pick.yaml \
        --run-type train \
        TENSORBOARD_DIR ./pick_tb/ \
        CHECKPOINT_FOLDER ./pick_checkpoints/ \
        LOG_FILE ./pick_train.log
    ```
    1. Train the Place skill. Use the exact same command as the above, but replace every instance of "pick" with "place".
    1. Train the Navigation skill. Use the exact same command as the above, but replace every instance of "pick" with "nav_to_obj".
    1. Copy the checkpoints for the different skills to the `data/models` directory in the Habitat Challenge directory. There should now be three files `data/models/[nav,pick,place].pth`.

1. Instead of training the skills, you can also use the provided trained skills. Download the skills via [models](https://drive.google.com/drive/folders/1g1CKh_uclKiFxCiL59F3lBRxiyXtT8kF)

1. Finally, evaluate the combined policies on the minival dataset for the `rearrange_easy` task from the command line. First enter the `habitat-challenge` directory. Ensure, you have the datasets installed in this directory as well. If not, run `python -m habitat_sim.utils.datasets_download --uids rearrange_task_assets`.
    ```bash
    CHALLENGE_CONFIG_FILE=configs/tasks/rearrange_easy.local.rgbd.yaml python agents/habitat_baselines_agent.py --evaluation local --input-type depth --cfg-path configs/methods/tp_srl.yaml
    ```
    Using the pre-trained skills from the Google Drive, you should see around a `20%` success rate.

# Result
## Pick Success Rate per checkpoints (100 Million Training Steps)
![image](https://github.com/timmy168/TP-SRL-Habitat-Rearrange-Challenge-Easy-2022-Study/blob/main/result/pick_result.png)

## Place Success Rate per checkpoints (100 Million Training Steps)
![image](https://github.com/timmy168/TP-SRL-Habitat-Rearrange-Challenge-Easy-2022-Study/blob/main/result/place_result.png)

## Navigation to Object Rate per checkpoints (100 Million Training Steps)
![image](https://github.com/timmy168/TP-SRL-Habitat-Rearrange-Challenge-Easy-2022-Study/blob/main/result/nav_to_obj_result.png)

## Evaluation Result
![image](https://github.com/timmy168/TP-SRL-Habitat-Rearrange-Challenge-Easy-2022-Study/blob/main/result/result.png)
