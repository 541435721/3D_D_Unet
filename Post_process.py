# -*- coding: utf-8 -*-
# @Author: bxsh
# @Email:  xbc0809@gmail.com
# @File:  Post_process.py
# @Date:  2017/9/29 9:21


from SimpleITK import ReadImage, WriteImage, ImageSeriesReader_GetGDCMSeriesFileNames
from SimpleITK import Cast, GetArrayFromImage

path1 = 'C:/Users/wow00/Desktop/Data/liver'
path2 = 'C:/Users/wow00/Desktop/new_folder/out.vtk'


def read_dcm(names, raw=False):
    if raw:
        img = ReadImage(names)
    else:
        names = ImageSeriesReader_GetGDCMSeriesFileNames(names)
        img = ReadImage(names)
    return img


if __name__ == '__main__':
    img = read_dcm(path1)
    pre = read_dcm(path2, True)

    pre = Cast(pre, pre.GetPixelID())
    pre.CopyInformation(img)
    WriteImage(pre, 'new.vtk')

    pass
