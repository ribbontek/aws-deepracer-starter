import unittest

from main.reward_functions.main import reward_function_1, reward_function_2, reward_function_3, reward_function_4


# Testing the AWS recommended reward functions
# Use this link will help determine feasible param options to test & try out with future reward functions
# https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html
class RewardFunctionsTestCase(unittest.TestCase):

    def test_reward_function_1(self):
        """
        Test the default 'Time trail - follow the center line' reward function
        """
        params = {'track_width': inch_to_meter(24), 'distance_from_center': 0}
        self.assertEqual(reward_function_1(params), 1.0)
        params['distance_from_center'] = 0.1
        self.assertEqual(reward_function_1(params), 0.5)
        params['distance_from_center'] = 0.2
        self.assertEqual(reward_function_1(params), 0.1)
        params['distance_from_center'] = 0.4
        self.assertEqual(reward_function_1(params), 0.001)

    def test_reward_function_2(self):
        """
        Test the 'Time trial - stay inside the two borders' reward function
        """
        params = {'track_width': inch_to_meter(24), 'all_wheels_on_track': True, 'distance_from_center': 0.0}
        self.assertEqual(reward_function_2(params), 1.0)
        params['distance_from_center'] = 0.1
        self.assertEqual(reward_function_2(params), 1.0)
        params['distance_from_center'] = 0.2
        self.assertEqual(reward_function_2(params), 1.0)
        params['distance_from_center'] = 0.4
        self.assertEqual(reward_function_2(params), 0.001)
        params['distance_from_center'] = 0.0
        params['all_wheels_on_track'] = False
        self.assertEqual(reward_function_2(params), 0.001)

    def test_reward_function_3(self):
        """
        Test the 'Time trial - prevent zig-zag' reward function
        """
        params = {'track_width': inch_to_meter(24), 'steering_angle': 0, 'distance_from_center': 0.0}
        self.assertEqual(reward_function_3(params), 1.0)
        params['distance_from_center'] = 0.1
        self.assertEqual(reward_function_3(params), 0.5)
        params['distance_from_center'] = 0.2
        self.assertEqual(reward_function_3(params), 0.1)
        params['distance_from_center'] = 0.4
        self.assertEqual(reward_function_3(params), 0.001)
        params['steering_angle'] = 16
        params['distance_from_center'] = 0.0
        self.assertEqual(reward_function_3(params), 0.8)
        params['distance_from_center'] = 0.1
        self.assertEqual(reward_function_3(params), 0.4)
        params['distance_from_center'] = 0.2
        self.assertEqual(round(reward_function_3(params), 4), 0.0800)
        params['distance_from_center'] = 0.4
        self.assertEqual(round(reward_function_3(params), 4), 0.0008)

    def test_reward_function_4(self):
        """
        Test the 'Object avoidance and head-to-head - stay on one lane and not crashing (default for OA and h2h)' reward function
        """
        params = {
            'track_width': inch_to_meter(24),
            'steering_angle': 0,
            'distance_from_center': 0.0,
            'all_wheels_on_track': True,
            'objects_distance': [0, 1],  # [(0:track_length), … ]
            'closest_objects': [0, 1],  # [(0:len(object_locations)-1), (0:len(object_locations)-1]
            'objects_left_of_center': [False, False],  # True|False
            'is_left_of_center': False
        }
        self.assertEqual(reward_function_4(params), 5.001)
        params['distance_from_center'] = 0.4
        self.assertEqual(round(reward_function_4(params), 4), 4.0020)
        params['distance_from_center'] = 0.0
        params['all_wheels_on_track'] = False
        self.assertEqual(round(reward_function_4(params), 4), 4.0020)

        params['is_left_of_center'] = True
        params['objects_left_of_center'] = [False, True]
        self.assertEqual(round(reward_function_4(params), 4), 4.0020)
        params['objects_distance'] = [0, 0.5]
        self.assertEqual(round(reward_function_4(params), 4), 2.002)
        params['objects_distance'] = [0, 0.3]
        self.assertEqual(round(reward_function_4(params), 4), 0.802)
        params['objects_distance'] = [0, 0.1]
        self.assertEqual(round(reward_function_4(params), 4), 0.006)


def inch_to_meter(inch):
    return inch / 39.37


if __name__ == '__main__':
    unittest.main()
