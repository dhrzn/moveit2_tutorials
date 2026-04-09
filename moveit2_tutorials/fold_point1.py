import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped #type of message sent to tf2
from tf2_ros import StaticTransformBroadcaster

class Fold_Point_1_broadcaster:
    def __init__(self):
        super().__init__('fold_point1_broadcaster')

        self.broadcaster = StaticTransformBroadcaster(self) #this creates/opens the communication channel to tf2

        self.publish_paper_frame() # this is where we would send and define what data we are sending

    def publish_paper_frame(self):
        t = TransformStamped() #where all the info about tf2 and time gets stored

        #stamp is basically saying "what time is this transform valid at"
        #tf2 keeps history of 10 seconds by default
        t.header.stamp = self.get_clock().now().to_msg()

        #defining the two frames this transform connects to
        t.header.frame_id = 'paper_center'
        t.child_frame_id = 'fold_point_1'

        #defining the translation
        #defining point 5cm to the right of paper with no rotation
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.05
        t.transform.translation.z = 0.0

        #defining the rotation/orientation
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        #this is where we actually send the data to tf2 tree
        self.broadcaster.sendTransform(t)
        self.get_logger().info('Paper frame delivered to tf2 tree')

def main(args=None):
    rclpy.init(args=args)
    node = Fold_Point_1_broadcaster()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()