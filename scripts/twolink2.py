import math
import matplotlib.pyplot as plt
import os 
from PIL import Image
import glob
import plotly.express as px

def twolink(args):
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    results_dir = os.path.join(results_dir + os.sep + "static" + os.sep + "images" + os.sep + "results" + os.sep)
    print(results_dir)
    l1 = float(args['armfirst'])
    l2 = float(args['armsecond'])

    n_theta = int(args['divisions']) # No of divisions
    theta_start1 = math.radians(int(args['anglestart1'])) # Starting angle
    #theta_end = math.pi/2 # Ending angle
    theta_end1 = math.radians(int(args['angleend1'])) # Ending angle for arm2
    theta_start2 = math.radians(int(args['anglestart2'])) # Starting angle
    theta_end2 = math.radians(int(args['angleend2'])) # Ending angle for arm2
    theta1 = []
    theta2 = []
    imgsarr = []
    for i in range(0,n_theta):
        theta1.append(theta_start1+ (theta_end1-theta_start1)*i/(n_theta-1)) # Angles of link 1
        theta2.append(theta_start2+ (theta_end2-theta_start2)*i/(n_theta-1)) # Angles of link 2

        # Base posotion 
        x0 = 0 # Base position
        y0 = 0 # Base position
        ct = i # Counter

    # Link 1 end point
    for t1, t2 in zip(theta1, theta2):
    
        x1 = l1*math.cos(t1) # End of link 1
        y1 = l1*math.sin(t1) # End of link 1        
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
        imgsarr.append(dir)
        print(dir)
        plt.savefig(dir)
        print('ct is' + str(ct))
        #fig = px.plot([x0,x1],[y0,y1])
        #fig = px.plot([x1,x2],[y1,y2])
        #fig.show()
    
 
    # Create the frames
    frames = []
    imgs = glob.glob(results_dir + "/*.png")
    for i in imgsarr:
        new_frame = Image.open(i)
        frames.append(new_frame)
    print('gif created')
    # Save into a GIF file that loops forever
    gifpath = results_dir + '/png_to_gif.gif'
    frames[0].save(gifpath, format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300, loop=0)



#twolink({'armfirst': 0.5, 'armsecond': 1.0, 'divisions': 4, 'anglestart1':0, 'angleend1':30,'anglestart2':0,'angleend2':60})