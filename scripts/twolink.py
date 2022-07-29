import math
import matplotlib.pyplot as plt
import os 
from PIL import Image
import glob
def twolink(args):
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    results_dir = os.path.join(results_dir + os.sep + "static" + os.sep + "images" + os.sep + "results" + os.sep)
    print(results_dir)
    l1 = float(args['armfirst'])
    l2 = float(args['armsecond'])

    n_theta = int(args['divisions']) # No of divisions
    theta_start = int(args['anglestart']) # Starting angle
    theta_end = math.pi/2 # Ending angle
    theta1 = []
    theta2 = []

    for i in range(0,n_theta):
        theta1.append(theta_start+ (theta_end-theta_start)*i/(n_theta-1)) # Angles of link 1
        theta2.append(theta_start+ (theta_end-theta_start)*i/(n_theta-1)) # Angles of link 2

        # Base posotion 
        x0 = 0 # Base position
        y0 = 0 # Base position
        ct = 1 # Counter

        # Link 1 end point
        for t1 in theta1:
        
            x1 = l1*math.cos(t1) # End of link 1
            y1 = l1*math.sin(t1) # End of link 1
            for t2 in theta2:
            
                x2 = x1+l2*math.cos(t2) # End of link 2
                y2 = y1+l2*math.sin(t2) # End of link 2

                filename = str(ct) + '.png'
                ct = ct+1
                plt.figure()
                plt.plot([x0,x1],[y0,y1])
                plt.plot([x1,x2],[y1,y2])
                plt.xlim([-1,2])
                plt.ylim([-1,2])
                dir = os.path.join(results_dir+filename)
                print(dir)
                plt.savefig(dir)
    
 
    # Create the frames
    frames = []
    imgs = glob.glob(results_dir + "/*.png")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
    print('gif created')
    # Save into a GIF file that loops forever
    gifpath = results_dir + '/png_to_gif.gif'
    frames[0].save(gifpath, format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300, loop=0)


#twolink(2)