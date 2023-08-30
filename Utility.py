import os
import glob
import numpy as np
import nibabel as nib

class NiiProcessor:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def process_folders(self):
        participant_folders = glob.glob(os.path.join(self.root_folder, 'p*'))
        
        for participant_folder in participant_folders:
            participant_number = participant_folder.split('p')[-1]

            run_folders = glob.glob(os.path.join(participant_folder, 'RUN*'))
            concatenated_data = []

            for run_folder in run_folders:
                nii_files = glob.glob(os.path.join(run_folder, 'wrMF*.nii'))
                nii_data_list = [nib.load(nii_file).get_fdata() for nii_file in nii_files]
                concatenated_data.extend(nii_data_list)

            if concatenated_data:
                concatenated_data = np.array(concatenated_data)
                output_filename = f'p{participant_number}_RUN{len(run_folders)}.nii'
                output_path = os.path.join(self.root_folder, output_filename)

                # Create a new NIfTI image
                nii_img = nib.Nifti1Image(concatenated_data, affine=None)
                nib.save(nii_img, output_path)

                print(f"Processed participant {participant_number} and saved {output_filename}")

# Usage
if __name__ == "__main__":
    root_folder = "/path/to/your/folder"
    nii_processor = NiiProcessor(root_folder)
    nii_processor.process_folders()