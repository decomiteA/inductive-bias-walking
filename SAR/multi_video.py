import pickle
import numpy as np
import skvideo.io
import os

with open(os.path.join('run0','tot_frames_1.pkl'),'rb') as f1:
    frames0 = np.squeeze(np.array(pickle.load(f1)))
with open(os.path.join('run1','tot_frames_1.pkl'),'rb') as f2:
    frames1 = np.squeeze(np.array(pickle.load(f2)))
with open(os.path.join('run2','tot_frames_1.pkl'),'rb') as f3:
    frames2 = np.squeeze(np.array(pickle.load(f3)))
with open(os.path.join('run3','tot_frames_1.pkl'),'rb') as f4:
    frames3 = np.squeeze(np.array(pickle.load(f4)))
with open(os.path.join('run4','tot_frames_1.pkl'),'rb') as f5:
    frames4 = np.squeeze(np.array(pickle.load(f5)))

list_fr = [frames0, frames1, frames2, frames3, frames4]
for vid in range(len(list_fr)):
    if list_fr[vid].shape[0]!=1000:
        print(vid)
        list_fr[vid] = np.concatenate((list_fr[vid], np.zeros((1000-list_fr[vid].shape[0],480,480,3))))


tot_frames = np.concatenate((list_fr[0],list_fr[1],list_fr[2],list_fr[3],list_fr[4]),2)
skvideo.io.vwrite('video_tot.mp4',np.squeeze(np.array(tot_frames)),outputdict={'-pix_fmt':'yuv420p'})
print('Done')