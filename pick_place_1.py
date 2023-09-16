# Copyright 2022 Trossen Robotics 
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def main():
    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )

    bot.arm.go_to_home_pose()

    bot.gripper.set_pressure(1.0)  # Adjust gripper pressure if necessary before releasing

    bot.gripper.release(2.0)


    # Rotate the waist to face the block's starting position (left side)
    bot.arm.set_single_joint_position(joint_name='waist', position=np.pi/2.0)

    # Approach the block by moving downwards and then translating in the x direction
    bot.arm.set_ee_cartesian_trajectory(z=-0.15)
    bot.arm.set_ee_cartesian_trajectory(x=-0.2)

    # Grasp the block
    bot.gripper.grasp(2.0)

    # Lift the block slightly upwards to ensure it's clear from the table or surface
    bot.arm.set_ee_cartesian_trajectory(z=0.1)

    # Rotate the waist to face the opposite side (right side)
    bot.arm.set_single_joint_position(joint_name='waist', position=-np.pi/2.0)

    # Move forward to the desired position on the opposite side 
    bot.arm.set_ee_cartesian_trajectory(x=0.2)

    # Lower the block to the destination surface
    bot.arm.set_ee_cartesian_trajectory(z=-0.1)

    # Release the block
    bot.gripper.release(2.0)

    # Retract the arm slightly upwards to avoid any collision with the placed block
    bot.arm.set_ee_cartesian_trajectory(z=0.1)

    # Return the robot arm to its home position and then to its sleep position
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

if __name__ == '__main__':
    main()
