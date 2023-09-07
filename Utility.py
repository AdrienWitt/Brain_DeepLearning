import os
import glob
import numpy as np
import nibabel as nib
from nilearn.image import concat_imgs



class NiiProcessor:
    def __init__(self, root_folder, output_foldername, files_type):
        self.root_folder = root_folder
        self.output_foldername = output_foldername
        self.files_type = files_type

    def concatenate_data(self):
        
        participant_folders = glob.glob(os.path.join(self.root_folder, 'p*'))
       
        for participant_folder in participant_folders:
            participant = participant_folder[-3:]
        
            run_folders = glob.glob(os.path.join(participant_folder, 'RUN*'))
        
            for run_folder in run_folders:
                nii_files = glob.glob(os.path.join(run_folder, f'{files_type}*.nii'))
                concatenated_data = []
                
                for file in nii_files:
                    img = nib.load(file)
                    concatenated_data.append(img)
        
        return concatenated_data
                    
    def save_concatenated(self):
    
        concatenated_data = self.concatenate_data()
        concatenated_img = concat_imgs(concatenated_data)
        run = run_folder[-4:]
        output_filename = f'{files_type}_{participant}_{run}'
        output_folder = os.path.join(root_folder, self.output_foldername)
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        output_path = os.path.join(output_folder, output_filename)
        nib.save(concatenated_img, output_path)
    
    def splitt_data(self):
        concatenated_data = self.concatenate_data()
        
        for participant in participant_data:
            
            
        
        
        
        

        
root_folder = r'C:\Users\adywi\OneDrive - unige.ch\Documents\Sarcasm_experiment\Adrien\fMRI_study\Preproc_Anlayses\data_done'
files_type = 'swrMF'
output_foldername = 'concatenated_images' 



participant_folders = glob.glob(os.path.join(root_folder, 'p*'))
participant_data = {}  

for participant_folder in participant_folders:
    participant = participant_folder[-3:]
    run_folders = glob.glob(os.path.join(participant_folder, 'RUN*'))
    run_info = {}

    for run_folder in run_folders:
        run_data = [] 
        run = run_folder[-4:]
        nii_files = glob.glob(os.path.join(run_folder, f'{files_type}*.nii'))
        
        for file in nii_files:
            img = nib.load(file)
            run_data.append(img)
            
        run_concatenated_data = concat_imgs(run_data)
        
        run_info[run]  = {
            'run folder': run_folder,
            'concatenated_data': run_concatenated_data
        }
        
        participant_data[participant] = run_info
    
            
for participant in participant_data:
        



a = 


# Usage
if __name__ == "__main__":
    root_folder = "/path/to/your/folder"
    nii_processor = NiiProcessor(root_folder)
    nii_processor.process_folders()
    


