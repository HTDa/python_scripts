from vidstab import VidStab
import matplotlib.pyplot as plt


stabilizer = VidStab(kp_method='FAST', threshold=42, nonmaxSuppression=False)
stabilizer.stabilize(input_path="DJI_0004.mp4", output_path="DJI_0004_output.mp4")


stabilizer.plot_trajectory()
plt.show()

stabilizer.plot_transforms()
plt.show()