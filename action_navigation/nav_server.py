import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
# On utilise NavigateToPose car Pose2D n'a pas d'action native simple, 
# mais on simule la logique demandée
from nav2_msgs.action import NavigateToPose 

class NavigationServer(Node):
    def __init__(self):
        super().__init__('navigation_server_node')
        self._action_server = ActionServer(
            self,
            NavigateToPose,
            'navigate_to_target',
            self.execute_callback)
        self.get_logger().info('Action Server Navigation démarré...')

    async def execute_callback(self, goal_handle):
        self.get_logger().info('Exécution du déplacement...')
        feedback_msg = NavigateToPose.Feedback()
        
        # Simulation d'une distance de 10m à 0m
        for i in range(10, -1, -1):
            feedback_msg.distance_remaining = float(i)
            self.get_logger().info(f'Feedback: Distance restante {i}m')
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1.0) # Simulation du mouvement

        goal_handle.succeed()
        result = NavigateToPose.Result()
        return result

def main(args=None):
    rclpy.init(args=args)
    node = NavigationServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
