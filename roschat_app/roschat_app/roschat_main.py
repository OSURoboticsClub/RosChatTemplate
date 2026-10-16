from rclpy.node import Node
import rclpy
import roschat_app.console_ui as c
import roschat_app.console_ui_elements as ce


#Define a function to send a message over the ROS network
def send_msg(msg: str):
    pass

#an example of how you could handle recieveing messages
def recv_msg(username: str, msg: str):
    chatDisplay.append_text(f"[{username}] - " + msg + "\n\n")

#Create your ROS Node here
class RosChatNode(Node):

    def __init__():
        super.__init__("node_name_here")


        


#Create UI and UI Elements
console = c.ConsoleUI(exit)

titleFg = c.Color(255,255,255)
primaryFg = c.Color(200,200,200)
primaryBg = c.Color(0,0,128)

chatInput = ce.InputField(
    console,
    0,
    console.get_size()[1] - 1,
    console.get_size()[0],
    onEnter=send_msg,
    fg = c.Color(255, 255, 255),
    bg = c.Color(0, 0, 0)
)

chatDisplay = ce.ScrollingTextField(
    console,
    0,
    0,
    console.get_size()[0],
    console.get_size()[1] - 1,
    "",
    primaryFg,
    primaryBg
)

def main(args=None):
    global node

    #create node and init ros
    rclpy.init(args=args)
    node = RosChatNode()

    while True:
        rclpy.spin_once(node, timeout_sec=0)

        if not chatInput.is_active():
            chatInput.activate()

        console.update(primaryFg, primaryBg)




if __name__ == "__main__":
    main()