# TP-SRL-Habitat-Rearrange-Challenge-2022-Study
This is a small work on testing and studing the method of Task Planning and Skills RL (TP-SRL) method on the long horizon mobile manipulation task on Habitat Rearrange Challenge 2022, and mainly tested and studied on the easy task. The work is inspired and learned from [habitat rearrange challenge 2022](https://github.com/facebookresearch/habitat-challenge/tree/rearrangement-challenge-2022).

# Task: Object Rearrangement
In the object rearrangement task, a Fetch robot is randomly spawned in an unknown environment and asked to rearrange 1 object from an initial to desired position – picking/placing it from receptacles (counter, sink, sofa, table), opening/closing containers (drawers, fridges) as necessary. A map of the environment is not provided and the agent must only use its sensory input to navigate and rearrange.

The Fetch robot is equipped with an egocentric 256x256 90-degree FoV RGBD camera on the robot head. 
The agent also has access to idealized base-egomotion giving the relative displacement and angle of the base since the start of the episode. 
Additionally, the robot has proprioceptive joint sensing providing access to the current robot joint angles.

For details about the agent, dataset, and evaluation, see the challenge website: [aihabitat.org/challenge/2022_rearrange](https://aihabitat.org/challenge/2022_rearrange/).

# Hardware Configuration
This small work is trained on 
