import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener #TransformListener = reads data | Buffer = holds data TransformListener reads
from geometry_msgs.msg import PointStamped #used to pinpoint positions with time
import tf2_geometry_msgs

class Position1_Listener(Node):
    def __init__(self):
        super().__init__('position1_listener')

       #creating where we would contain the data read off of TransformListener
        self.tf_buffer = Buffer()

        #calling transform listener and letting it know where to store its data (in this case goes to self.tf_buffer)
        self.tf_listener = TransformListener(self.tf_buffer, self)

        #creating a timer so transform listener has enough time to dump all of its information into the buffer before moving on 
        #inside () we defined how long it has to read data, and WHERE to read from (in this case self.get_paper_transform)
        self.timer = self.create_timer(2.0, self.get_paper_transform)

        def get_paper_transform(self):
            try:
                #this is where it looks up transform given off of time and references given
                transform = self.tf_buffer.lookup_transform(
                    'paper_center',   #parent
                    'fold_point_1',   #child
                    rclpy.time.Time()  #defining at what time we want to see position (nothing inside () so it means getting most current transform)

                )

                #defining where fold_point1 is relative to the paper center
                #basically this spits back the answer for us

                x = transform.transform.translation.x
                y = transform.transform.translation.y
                z = transform.transform.translation.z

                #making sure we get confirmation that everything went right and actually seeing the answer
                self.get_logger().info(
                    f'fold_point_1 is at x:{x:.3f} y:{y:.3f} z:{z:.3f} relative to paper center'
                )

                #in case if anything goes wrong we can capture the error (most common error to see is frame not existing in the frame yet)
            except Exception as e:
                self.get_logger().warn(f'Could not get transform: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = Position1_Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()