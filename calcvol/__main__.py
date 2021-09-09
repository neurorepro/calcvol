import os
import sys
import argparse
import textwrap
import numpy as np
import nibabel as nib

########################################################################################
### Argument parsing
###
def main():
    ##### PARSER
    def type_isfile(f):
        if not os.path.isfile(f):
            raise argparse.ArgumentTypeError("%s does not exist" % f)
        return f
    def type_isdir(d):
        if not os.path.isdir(d):
            raise argparse.ArgumentTypeError("Directory %s does not exist" % d)
        return d
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Computes the volume of the non zero voxels of a NIFTI file.
            You can choose the volume unit between mm3, cm3 and number of voxels'''),
        epilog=textwrap.dedent('''\
            Example: calc_vol.py --nifti_file T1_brain.nii.gz --unit cm3'''))
    parser.add_argument("--nifti_file", required=True, help="path to the NIFTI file", type=type_isfile)
    parser.add_argument("--unit", required=False, help="volume unit", choices=['mm3', 'cm3', 'voxels'], default="mm3")
    args = parser.parse_args()
    ### Get arguments
    nifti_file = os.path.abspath(args.nifti_file)
    unit = args.unit

    ####  Brain volume calculation
    nifti_image = nib.load(nifti_file)
    nifti_data = nifti_image.get_fdata()
    vox_size = np.array(nifti_image.header.get_zooms()).prod()
    n_voxels = np.count_nonzero(nifti_data)
    vol_mm3 = n_voxels * vox_size

    if unit == "voxels":
        print(n_voxels)
    elif unit == "mm3":
        print(vol_mm3)
    elif unit == "cm3":
        print(vol_mm3/1000)

if __name__ == "__main__":
    main()


